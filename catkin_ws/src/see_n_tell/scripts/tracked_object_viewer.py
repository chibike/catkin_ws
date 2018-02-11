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

class TrackedObjectViewer(object):
    def __init__(self, window_title="image"):
        #Create setup variables
        self._created = False
        self.color_config=(640,480,30)
        self.title = window_title

        #Set start frame to a demo image :) Better than setting the start frame to all zeros
        self.frame = cv2.imread("pic_01.jpg")

        #Define buffer format for data
        self.fmt = 'B'*(self.color_config[0]*self.color_config[1]*3)

        #Define this module as a rospy node
        rospy.init_node("tracked_object_viewer", anonymous=True)

        #Define pixel regions
        self.pixel_regions = []

    def start(self):
        if not self._created:
            #Subscribe to ColorData_1 ros_topic
            rospy.Subscriber("ColorData_1", numpy_msg(UInt8MultiArray), self.color_callback)
            rospy.Subscriber("TrackedRegions_1", ContourData, self.tracked_object_callback)

            #Create a window to display the image
            basic_header.createNormalWindow(self.title)

        #Update the created variable
        self._created = True

    def end(self):
        #Update the created variable
        self._created = False

        #Close Window
        basic_header.destroyWindows()

        #Exit program
        exit()

    def run(self):
        contour_colour = (0,255,0)
        while not rospy.is_shutdown() and self._created:
            #Draw pixel regions on the image
            self.drawPixelRegions(self.pixel_regions)

            #Empty pixel regions buffer
            self.pixel_regions = []
            
            #Update the image in the window
            basic_header.showFrame(self.title, self.frame)

            #Get keyboard input
            key = cv2.waitKey(300) #Specify timeout. Used to regulate loop speed

            #If key == ESC end program
            if key == 27:
                self.end()

    def color_callback(self, data):
        #Retreive data and convert it to a numpy array
        self.frame = np.array(struct.unpack(self.fmt, data.data), dtype=np.uint8)

        #Describe the shape of the data
        self.frame.shape = (self.color_config[1], self.color_config[0], 3)

    def tracked_object_callback(self, data):
        #Retreive data
        data_lengths = data.data_lengths
        data = data.data

        #Empty contours buffer
        self.pixel_regions = []

        #Reconstruct contour data object
        start_index = 0
        for i in range(len(data_lengths)):
            end_index = start_index + data_lengths[i]
            contour = np.array(data[start_index:end_index])
            contour.shape = (data_lengths[i]/2,1,2)
            start_index = end_index

            pixel_region = PixelRegion()
            pixel_region.addContour(contour)
            self.pixel_regions.append(pixel_region)

    def drawPixelRegions(self, pixel_regions):
        while len(pixel_regions) > 0:
            pixel_region = pixel_regions[0]
            pixel_regions = pixel_region.addPixelRegions(pixel_regions[1:])
            
            self.frame = pixel_region.drawLocation(self.frame, True)
            

def main():
    #Create a viewer object with a window title <Color Viewer>
    my_viewer = TrackedObjectViewer("Color Viewer")

    #Start the viewer
    my_viewer.start()

    #Run the viewer
    my_viewer.run()

    #End the viewer
    my_viewer.end()

#Run the main function if this program is running directly
if __name__ == "__main__":
    main()


'''
def restructureContourData(data, data_lengths):
    contours = []
    start_index = 0
    
    for i in range(len(data_lengths)):
        end_index = start_index + data_lengths[i]
        contour = np.array(data[start_index:end_index])
        contour.shape = (data_lengths[i]/2,1,2)
        start_index = end_index
        
        contours.append(contour)

    return contours

def flattenContourData(contours):
    cs_lengths = []
    cs_data = []
    
    for contour in contours:
	data = contour.ravel().tolist()
	cs_lengths.append(len(data))
	cs_data += data

    return (cs_data, cs_lengths)
'''
