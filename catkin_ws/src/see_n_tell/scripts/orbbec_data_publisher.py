#!/usr/bin/env python

#Setup import files from the manifest file
PKG = "see_n_tell"
import roslib; roslib.load_manifest(PKG)
import rospy

#Import support libraries for the Camera, Microphone, and other generic functions
import numpy as np
import basic_header
import primesense
from orbbec_class import OrbbecDepthCamera
from microphone_n_speaker_class import Microphone


#Import the necessary message formats needed
from see_n_tell.msg import Int32Array
from see_n_tell.msg import Float32Array

class OrbbecAstraDataPublisher(object):
    def __init__(self, fps=10, block_duration=20):
        #Create started variable
        self._started = False
        
        #Setup device and image data properties
        self.depth_config=(640,480,30)
        self.color_config=(640,480,30)
        
        self.depth_data_width = self.depth_config[0]
        self.depth_data_height = self.depth_config[1]
        self.depth_data_channel = 1
        
        self.color_data_width = self.color_config[0]
        self.color_data_height = self.color_config[1]
        self.color_data_channel = 3

        #Setup sound properties
        self.sound_samplerate = 44100
        self.sound_channels = 2
        self._stream_sample_duration = block_duration
        self.sound_data_height = int(self.sound_samplerate * self._stream_sample_duration/1000.0)

        #Intialize Camera
        try:
            self.device = OrbbecDepthCamera(self.depth_config, self.color_config)
        except primesense.utils.OpenNIError:
            print "Error: No device detected"
            self.device = None

        #Intialize Mic with a callback function
        self.mic = Microphone(self.sound_channels, self.sound_samplerate, self.callback)

        #Initialize this module as a ros node
        rospy.init_node('orbbec_data_publisher')
        
        #Setup publishers
        self.depth_data_pub = rospy.Publisher("DepthData_1", Int32Array, queue_size=10)
        self.color_data_pub = rospy.Publisher("ColorData_1", Int32Array, queue_size=10)
        self.sound_data_pub = rospy.Publisher("SoundData_1", Float32Array, queue_size=10)

        #Setup refresh rate variables
        self.fps = basic_header.constrainf(fps, 1, 30) #constrain the fps to 1-30 Hz
        self.rate = rospy.Rate(self.fps)

        #Create buffers for data to send
        self.depth_data_2_send = Int32Array()
        self.color_data_2_send = Int32Array()
        self.sound_data_2_send = Float32Array()
        
    def start(self):
        #Start the device if it has not started
        if not self._started and type(self.device) != type(None):
            try:
                self.device.start()
            except primesense.utils.OpenNIError:
                self.device = None

        #Update the start variable
        self._started = True

    def end(self):
        #End the microphone and device if they are started
        if self._started:
            if type(self.device) != type(None):
                self.device.end()
            self.mic.stop()

        #Update the start variable
        self._started = False

    def publishDepthData(self):
        #Exit function if the device has not started
        if not self._started:
            return None
        
        #Store the incoming image data as a 1D array
        self.depth_data_2_send.data = self.device.getDepthFrame(format_shape = False).ravel().tolist()

        #print "Sending Depth ",self.depth_data_2_send.data

        #Publish data
        self.depth_data_pub.publish(self.depth_data_2_send)

    def publishColorData(self):
        #Exit function if the device has not started
        if not self._started:
            return None

        #Store the incoming image data as a 1D array
        self.color_data_2_send.data = self.device.getColorFrame(format_shape = False).ravel().tolist()

        #print "Sending Color ",self.color_data_2_send.data

        #Publish data
        self.color_data_pub.publish(self.color_data_2_send)

    def publishSoundData(self):
        #Exit function if the device has not started
        if not self._started:
            return None

        #Store the incoming sound data as a 1D array
        self.sound_data_2_send.data = self.mic.getRecording(duration=self._stream_sample_duration, blocking=True).ravel().tolist()

        #print "Sending Sound", sound_data

        #Publish data
        self.sound_data_pub.publish(self.sound_data_2_send)

    def publishBothData(self):
        #Publish colour and depth data
        self.publishColorData()
        self.publishDepthData()

    def run(self):
        #Start streaming sound data from the microphone
        self.mic.startStream(frame_width=self._stream_sample_duration)

        #Continue publishing data until ros is shutdown
        while not rospy.is_shutdown() and self._started:
            if type(self.device) != type(None):
                self.publishBothData()
            self.rate.sleep() # Maintain frame rate

        #Stop streaming sound data from the microphone
        self.mic.stopStream()

    def callback(self, indata, frame_length, time, status):
        #Store the incoming sound data as a 1D array
        self.sound_data_2_send.data = indata.ravel().tolist()
        
        #print len(self.sound_data_2_send.data)
        #print "Sending Sound", self.sound_data_2_send.data

        #Publish data
        self.sound_data_pub.publish(self.sound_data_2_send)

def main():
    #Create a publisher object with framerate = 5
    my_data_publisher = OrbbecAstraDataPublisher(5)

    #Start publisher
    my_data_publisher.start()

    #Run publisher
    my_data_publisher.run()

    #End publisher
    my_data_publisher.end()

#If code is running directly run the main function
if __name__ == '__main__':
    try:
        main()
    except rospy.ROSInterruptException:
        pass
