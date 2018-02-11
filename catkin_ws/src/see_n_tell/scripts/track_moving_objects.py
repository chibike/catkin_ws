#!/usr/bin/env python

#Setup import files from the manifest file
PKG = "see_n_tell"
import roslib; roslib.load_manifest(PKG)
import rospy

#Import support libraries for buffer formatting and other specialists functions
import basic_header
import struct
import numpy as np
import cv2
import math

#Import the necessary message formats needed
from rospy.numpy_msg import numpy_msg
from std_msgs.msg import UInt8MultiArray
from std_msgs.msg import UInt16MultiArray
from see_n_tell.msg import ContourData

class ObjectTracker(object):
    def __init__(self, fps=10):
        #Create setup variables
        self._created = False
        self.color_config=(640,480,30)
        self.depth_config=(640,480,30)

        #Set start frames to None
        self.color_next_frame = None
        self.color_curr_frame = None
        self.color_last_frame = None
        self.depth_next_frame = None
        self.depth_curr_frame = None
        self.depth_last_frame = None

        #Define buffer format for data
        self.color_data_fmt = 'B'*(self.color_config[0]*self.color_config[1]*3)
        self.depth_data_fmt = 'H'*(self.depth_config[0]*self.depth_config[1])

        #Initialize this module as a rospy node
        rospy.init_node("track_moving_objects_color", anonymous=True)

        #Setup refresh rate variables
        self.fps = basic_header.constrainf(fps, 1, 30) #constrain the fps to 1-30 Hz
        self.rate = rospy.Rate(self.fps)

        #Setup publisher
        self.tracked_regions_pub = rospy.Publisher("TrackedRegions_1", ContourData, queue_size=10)

        #Create buffer for data to send
        self.tracked_regions_data_2_send = ContourData()

        
        #Setup the buffers for data to send
        self.tracked_regions_data_2_send.data_lengths = []
        self.tracked_regions_data_2_send.data = []

    def start(self):
        if not self._created:
            #Subscribe to ColorData_1 ros_topic
            rospy.Subscriber("ColorData_1", numpy_msg(UInt8MultiArray), self.color_callback)
            rospy.Subscriber("DepthData_1", numpy_msg(UInt16MultiArray), self.depth_callback)

        #Update the created variable
        self._created = True

    def end(self):
        #Update the created variable
        self._created = False

        #Exit program
        exit()

    def run(self):
        while not rospy.is_shutdown() and self._created:
            #Update frames
            self._updateFrames()
            
            #Get the difference bwt the previous frames
            color_frame_diff,depth_frame_diff = self._getFrameDiff( threshold=30 )

            #Extract the contour locations from the frame diff
            self._extractContourData(color_frame_diff,depth_frame_diff)

            #print "Publishing tracked data..."

            #Publish data
            self.publishTrackedData()

            #Maintain frame rate
            self.rate.sleep()
            
            #Goto next frame
            self._updateFrames()

    def publishTrackedData(self):
        #Exit function if the object has not created
        if not self._created or len(self.tracked_regions_data_2_send.data_lengths) <= 0:
            return None

        #print "Number of regions = ", len(self.tracked_regions_data_2_send.data_lengths)/2

        #Publish data
        self.tracked_regions_pub.publish(self.tracked_regions_data_2_send)

    def color_callback(self, data):
        #Retreive data and convert it to a numpy array
        self.color_next_frame = np.array(struct.unpack(self.color_data_fmt, data.data), dtype=np.uint8)

        #Describe the shape of the data
        self.color_next_frame.shape = (self.color_config[1], self.color_config[0], 3)

    def depth_callback(self, data):
        #Retreive data and convert it to a numpy array
        self.depth_next_frame = np.array(struct.unpack(self.depth_data_fmt, data.data), dtype=np.uint8)

        #Describe the shape of the data
        self.depth_next_frame.shape = (self.depth_config[1], self.depth_config[0])

    def _updateFrames(self):
        #Verify that the next frames are valid
        
        if self._isValid(self.color_next_frame, self.color_config):
            #Update the last frame
            self.color_last_frame = self.color_curr_frame

            #Convert the next_frame to grayscale
            #and update the current frame
            self.color_curr_frame = self._convertFrame2GRAY(self.color_next_frame)
            
        if self._isValid(self.depth_next_frame, self.depth_config):
            #Update the last frame
            self.depth_last_frame = self.depth_curr_frame
            
            #Update the current frame
            self.depth_curr_frame = self.depth_next_frame

        
    def _isValid(self, frame, config):
        #Verify that the current frame is valid
        #print "Checking..."
        try:
            if tuple(frame.shape) == (config[1], config[0], 3):
                #print "Passed !!!"
                return True
            elif tuple(frame.shape) == (config[1], config[0], 1):
                #print "Passed !!!"
                return True
            elif tuple(frame.shape) == (config[1], config[0]):
                #print "Passed !!!"
                return True
            else:
                #print "Failed !"
                #print "shape =",frame.shape, "vs",(self.color_config[1], self.color_config[0], 3)
                return False
        except:
            #print "Failed !"
            return False

    def _convertFrame2GRAY(self, frame):
        #Convert frame to hsv and return it
        return cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    def _getFrameDiff(self, threshold = 30):
        #Create buffers to store the difference between the frames
        color_frame_diff = None
        depth_frame_diff = None

        if self._isValid(self.color_curr_frame, self.color_config) and self._isValid(self.color_last_frame, self.color_config):
            #Blurify the image to exaggerate diff
            c_f = cv2.GaussianBlur(self.color_curr_frame, (5, 5), 0)
            l_f = cv2.GaussianBlur(self.color_last_frame, (5, 5), 0)

            #Calculate the positions of the pixels that changed bwt frames
            color_frame_diff = cv2.absdiff(c_f, l_f)
            color_frame_diff = cv2.threshold(color_frame_diff, threshold, 255, 0, cv2.THRESH_BINARY)[1]

            #Expand pixels to join them
            for i in range(3):
                color_frame_diff = cv2.dilate(color_frame_diff, (5,5))

            #Reduce pixels to make lines thinner
            for i in range(3):
                color_frame_diff = cv2.erode(color_frame_diff, (5,5))

        if self._isValid(self.depth_curr_frame, self.depth_config) and self._isValid(self.depth_last_frame, self.depth_config):
            #Blurify the image to exaggerate diff
            c_f = cv2.GaussianBlur(self.depth_curr_frame, (5, 5), 0)
            l_f = cv2.GaussianBlur(self.depth_last_frame, (5, 5), 0)

            #Calculate the positions of the pixels that changed bwt frames
            depth_frame_diff = cv2.absdiff(c_f, l_f)
            depth_frame_diff = cv2.threshold(depth_frame_diff, threshold, 255, 0, cv2.THRESH_BINARY)[1]

            #Expand pixels to join them
            for i in range(3):
                depth_frame_diff = cv2.dilate(depth_frame_diff, (5,5))

            #Reduce pixels to make lines thinner
            for i in range(3):
                depth_frame_diff = cv2.erode(depth_frame_diff, (5,5))

        #Returns an image with pixels that changed between frames indicated as white
        return color_frame_diff,depth_frame_diff
    
    def _extractContourData(self, color_frame_diff, depth_frame_diff):
        #Create buffer to store contour data
        colour_contours = []
        depth_contours = []

        #Verify that the color_frame_diff is valid
        if type(color_frame_diff) != type(None):
            colour_contours = cv2.findContours(
                color_frame_diff,
                mode=cv2.RETR_TREE,
                method=cv2.CHAIN_APPROX_SIMPLE,
                offset=(0, 0)
                )[1]

        #Verify that the depth_frame_diff is valid
        if type(depth_frame_diff) != type(None):
            depth_contours = cv2.findContours(
                depth_frame_diff,
                mode=cv2.RETR_TREE,
                method=cv2.CHAIN_APPROX_SIMPLE,
                offset=(0, 0)
                )[1]

        #Clear the data to send buffers
        self.tracked_regions_data_2_send.data_lengths = []
        self.tracked_regions_data_2_send.data = []

        #Add the contour information from the color data
        for contour in colour_contours:
            data = contour.ravel().tolist()
            self.tracked_regions_data_2_send.data_lengths.append(len(data))
            self.tracked_regions_data_2_send.data += data

        #Add the contour information from the depth data
        for contour in depth_contours:
            data = contour.ravel().tolist()
            self.tracked_regions_data_2_send.data_lengths.append(len(data))
            self.tracked_regions_data_2_send.data += data


def main():
    #Create a tracker object
    my_object_tracker = ObjectTracker()

    #Start the tracker
    my_object_tracker.start()

    #Run the tracker
    my_object_tracker.run()

    #End the tracker
    my_object_tracker.end()

#Run the main function if this program is running directly
if __name__ == "__main__":
    main()

