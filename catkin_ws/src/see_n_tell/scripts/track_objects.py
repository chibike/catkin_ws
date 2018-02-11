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
import ImageStreamViewer
import pyobjects

#Import the necessary message formats needed
from see_n_tell.msg import Int32Array

class ObjectTracker(ImageStreamViewer.Viewer):
    def __init__(self, window_title="image"):
        super(self.__class__, self).__init__(window_title)

        #Set start frame to None
        self.next_frame = None
        self.curr_frame = None
        self.last_frame = None

        #Initialize this module as a rospy node
        rospy.init_node("track_objects", anonymous=True)

    def start(self):
        if not self.created:
            #Subscribe to ColorData_1 ros_topic
            rospy.Subscriber("ColorData_1", Int32Array, self.callback)

        super(self.__class__, self).start()

    def end(self):
        super(self.__class__, self).end()

    def run(self):
        while not rospy.is_shutdown() and self.created:
            if self.isValid(self.next_frame):
                self.frame = np.copy(self.next_frame)
                objects = pyobjects.objectify(self.next_frame)
                print len(objects)
                #self.frame = pyobjects.drawObjectsOnBlankImage(objects, (self.color_config[1], self.color_config[0], ))
            self.updateView(rgb_mode=False)

    def callback(self, data):
        #Retreive data and convert it to a numpy array
        self.next_frame = np.array(data.data, dtype=np.int32).astype(np.uint8)

        #Describe the shape of the data
        self.next_frame.shape = (self.color_config[1], self.color_config[0], 3)

    def isValid(self, frame):
        #Verify that the selected frame is valid
        try:
            if type(frame) == type(None):
                return False
            elif tuple(frame.shape) == (self.color_config[1], self.color_config[0], 3):
                return True
            elif tuple(frame.shape) == (self.color_config[1], self.color_config[0], 1):
                return True
            elif tuple(frame.shape) == (self.color_config[1], self.color_config[0]):
                return True
            else:
                return False
        except:
            return False
        
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
