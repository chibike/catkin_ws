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
from see_n_tell.msg import ContourData

class ObjectTracker(object):
    def __init__(self, fps=10):
        #Create setup variables
        self._created = False
        self.color_config=(640,480,30)

        #Set start frame to None
        self.next_frame = None
        self.curr_frame = None
        self.last_frame = None

        #Define buffer format for data
        self.fmt = 'B'*(self.color_config[0]*self.color_config[1]*3)

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
            rospy.Subscriber("ColorData_1", numpy_msg(UInt8MultiArray), self.callback)

        #Update the created variable
        self._created = True

    def end(self):
        #Update the created variable
        self._created = False

        #Exit program
        exit()

    def publishTrackedData(self):
        #Exit function if the object has not created
        if not self._created or len(self.tracked_regions_data_2_send.data_lengths) <= 0:
            return None

        #print "Number of regions = ", len(self.tracked_regions_data_2_send.data_lengths)/2

        #Publish data
        self.tracked_regions_pub.publish(self.tracked_regions_data_2_send)

    def run(self):
        while not rospy.is_shutdown() and self._created:
            #Verify that the current frame is valid
            if not (self._isValid(self.curr_frame) and self._isValid(self.last_frame)):
                self._updateFrames() #goto next frame
                continue
            
            #Get the difference bwt the previous frames
            frame_diff = self._getFrameDiff( threshold=30 )

            #print "Grouping points..."

            #Extract the contour locations from the frame diff
            self._extractContourData(frame_diff)

            #print "Publishing tracked data..."

            #Publish data
            self.publishTrackedData()

            #Maintain frame rate
            self.rate.sleep()
            
            #Goto next frame
            self._updateFrames()

    def callback(self, data):
        #Retreive data and convert it to a numpy array
        self.next_frame = np.array(struct.unpack(self.fmt, data.data), dtype=np.uint8)

        #Describe the shape of the data
        self.next_frame.shape = (self.color_config[1], self.color_config[0], 3)

    def _updateFrames(self):
        #Verify that the next frame is valid
        if not self._isValid(self.next_frame):
            return None
        
        #Update the last frame
        self.last_frame = self.curr_frame

        #Convert the next_frame to grayscale
        #and update the current frame
        self.curr_frame = self._convertFrame2GRAY(self.next_frame)

    def _isValid(self, frame):
        #Verify that the current frame is valid
        #print "Checking..."
        try:
            if tuple(frame.shape) == (self.color_config[1], self.color_config[0], 3):
                #print "Passed !!!"
                return True
            elif tuple(frame.shape) == (self.color_config[1], self.color_config[0], 1):
                #print "Passed !!!"
                return True
            elif tuple(frame.shape) == (self.color_config[1], self.color_config[0]):
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
        #Blurify the image to exaggerate diff
        c_f = cv2.GaussianBlur(self.curr_frame, (5, 5), 0)
        l_f = cv2.GaussianBlur(self.last_frame, (5, 5), 0)

        #Calculates the positions of the pixels that changed bwt frames
        frame_diff = cv2.absdiff(c_f, l_f)
        frame_diff = cv2.threshold(frame_diff, threshold, 255, 0, cv2.THRESH_BINARY)[1]

        #Expand pixels to join them
        for i in range(3):
            frame_diff = cv2.dilate(frame_diff, (5,5))

        #Reduce pixels to make lines thinner
        for i in range(3):
            frame_diff = cv2.erode(frame_diff, (5,5))

        #Returns an image with pixels that changed between frames indicated as white
        return frame_diff
    
    def _extractContourData(self, frame_diff):
        im2, contours, hierarchy = cv2.findContours(frame_diff, mode=cv2.RETR_TREE, method=cv2.CHAIN_APPROX_SIMPLE, offset=(0, 0))
        if len(contours) > 0:
            self.tracked_regions_data_2_send.data_lengths = []
            self.tracked_regions_data_2_send.data = []

            for contour in contours:
                data = contour.ravel().tolist()
                self.tracked_regions_data_2_send.data_lengths.append(len(data))
                self.tracked_regions_data_2_send.data += data
        else:
            self.tracked_regions_data_2_send.data_lengths = []
            self.tracked_regions_data_2_send.data = []


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

