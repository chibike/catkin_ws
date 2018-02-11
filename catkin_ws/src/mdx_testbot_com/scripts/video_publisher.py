#!/usr/bin/env python

#Setup import files from the manifest file
import rospy

#Import support libraries
import cv2
import pi_video
import numpy as np

#Import the necessary message format needed
from mdx_testbot_com.msg import VideoData

class VideoPublisher(object):
    def __init__(self, fps=10, left_device_id=1, right_device_id=2):
        #Create started variable
        self._started = False

        #Setup publisher - Setup pub before init !Order Matters!
        self.video_data_pub = rospy.Publisher('VideoData_01', VideoData, queue_size=10)
        
        #Initialize this module as a ros node
        rospy.init_node('video_publisher', anonymous=True)

        #Setup refresh rate variables
        self.fps = min(max(fps, 1), 30) #constrain bwt 1 and 30
        self.rate = rospy.Rate(self.fps)

        #Create data buffer
        self.video_data_buffer = VideoData()

        #Create camera object
        self.left_camera  = pi_video.Camera(left_device_id)
        #self.right_camera = pi_video.Camera(right_device_id)
        
    def start(self):
        if not self._started:
            self.left_camera.start()
            #self.right_camera.start()

        #Update the start variable
        self._started = True
        return self._started

    def stop(self):
        if self._started:
            self.left_camera.stop()
            #self.right_camera.stop()
            
        #Update the start variable
        self._started = False
        return self._started

    def publish_data(self):
        #Ensure the object has started
        if not self._started: return False

        #Update data variable
        left_data  = self.left_camera.get_next_frame().ravel().tolist()
        #right_data = self.right_camera.get_next_frame()
        
        self.video_data_buffer.left_data = left_data
        self.video_data_buffer.right_data = left_data

        #Publish data
        self.video_data_pub.publish(self.video_data_buffer)
        return self._started

    def run(self):
        #Ensure the object has started
        if not self._started: return False
        
        while not rospy.is_shutdown():
            self.publish_data()
            self.rate.sleep()
        return self._started

def main():
    #Create a publisher
    video_pub = VideoPublisher()

    #Start publisher
    video_pub.start()

    #Run publisher
    video_pub.run()

    #Stop publisher
    video_pub.stop()
    
if __name__=='__main__':
    main()
