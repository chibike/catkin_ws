#!/usr/bin/env python

#Setup import files from the manifest file
import rospy

#Import support libraries
import pi_video
import numpy as np

#Import the necessary message format needed
from mdx_testbot_com.msg import VideoData

class VideoSubscriber(object):
    def __init__(self):
        #Create started variable
        self._started = False

        #Initialize this module as a ros node
        rospy.init_node('video_subscriber', anonymous=True)

        #Initialize speaker
        self.viewer = pi_video.Viewer(fps=10, title="viewer")

        #Create Data buffer
        self.left_frame = None
        self.right_frame = None

        #Create frame analyzer
        my_analyzer = pi_video.FrameAnalyzer(num_of_trails=2)

    def start(self):
        if not self._started:
            rospy.Subscriber("VideoData_01", VideoData, self.callback)
            self.viewer.start()

        #Update the start variable
        self._started = True

    def stop(self):
        if self._started:
            self.viewer.stop()

        #Update the start variable
        self._started = False
        exit()

    def run(self):
        while type(self.left_frame) == type(None):continue
        while True:
            frame = np.copy(self.left_frame)
            frame.shape = (480, 640, 3)
            #print frame
            if self.viewer.show_frame(frame.astype(np.uint8)): break
        return self._started

    def callback(self, data):
        self.left_frame = np.array(data.left_data)

def main():
    #Create a subscriber
    video_sub = VideoSubscriber()

    #Start subscriber
    video_sub.start()

    #Run subscriber
    video_sub.run()

    #Stop subscriber
    video_sub.stop()

if __name__ == '__main__':
    main()
