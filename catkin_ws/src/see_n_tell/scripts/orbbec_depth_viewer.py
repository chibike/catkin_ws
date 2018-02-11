#!/usr/bin/env python

#Setup import files from the manifest file
PKG = "see_n_tell"
import roslib; roslib.load_manifest(PKG)
import rospy

#Import support libraries for buffer formatting and other generic functions
import basic_header
import numpy as np
import cv2

#Import the necessary message formats needed
from see_n_tell.msg import Int32Array

class DepthViewer(object):
    def __init__(self, window_title="image"):
        #Create setup variables
        self._created = False
        self.depth_config=(640,480,30)
        self.title = window_title

        #Set start frame to a demo image :) Better than setting the start frame to all zeros
        self.frame = cv2.imread("pic_01.jpg")

        #Define this module as a rospy node
        rospy.init_node("orbbec_depth_viewer", anonymous=True)

        #Define a black gray scale image - To be used later to pad image
        self.zero_buffer = np.zeros(
            shape=(self.depth_config[1], self.depth_config[0], 1),
            dtype=np.uint8
            )

    def start(self):
        if not self._created:
            #Subscribe to DepthData_1 ros_topic
            rospy.Subscriber("DepthData_1", Int32Array, self.callback)

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
        while not rospy.is_shutdown() and self._created:
            #Update the image in the window
            basic_header.showFrame(self.title, self.frame)

            #Get keyboard input
            key = cv2.waitKey(200) #Specify timeout. Used to regulate loop speed

            #If key == ESC end program
            if key == 27:
                self.end()

    def callback(self, data):
        #Retreive data and convert it to a numpy array
        self.frame = np.array(data.data, dtype=np.int32)
        
        #print "Below:: Min, Max",min(self.frame),max(self.frame)
        
        self.frame = basic_header.mapf(
            self.frame.astype(np.float32).ravel(),
            0,
            33559,
            0,
            255
          ).astype(np.uint8)
          
        #print "After:: Min, Max",min(self.frame),max(self.frame)

        #Describe the shape of the data
        self.frame.shape = (self.depth_config[1], self.depth_config[0], 1)

        #Pad the data with two zero data
        '''
        frame = 0 + data + 0 ==> (r,g,b) use the data for the green channel
        '''
        self.frame = np.concatenate(
            (self.zero_buffer, self.frame, self.zero_buffer),
            axis = 2)

def main():
    #Create a viewer object with a window title <Depth Viewer>
    my_viewer = DepthViewer("Depth Viewer")

    #Start the viewer
    my_viewer.start()

    #Run the viewer
    my_viewer.run()

    #End the viewer
    my_viewer.end()

#Run the main function if this program is running directly
if __name__ == "__main__":
    main()
