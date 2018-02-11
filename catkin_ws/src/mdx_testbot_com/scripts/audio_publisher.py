#!/usr/bin/env python

#Setup import files from the manifest file
import rospy

#Import support libraries
import pi_audio

#Import the necessary message format needed
from mdx_testbot_com.msg import AudioData

#####rospy.get_time()
class AudioPublisher(object):
    def __init__(self, fps=30, left_channel_index=2, right_channel_index=3):
        #Create started variable
        self._started = False

        #Setup publisher - Setup pub before init !Order Matters!
        self.audio_data_pub = rospy.Publisher('AudioData_01', AudioData, queue_size=10)
        
        #Initialize this module as a ros node
        rospy.init_node('audio_publisher', anonymous=True)

        #Setup refresh rate variables
        self.fps = min(max(fps, 1), 30) #constrain bwt 1 and 30
        self.rate = rospy.Rate(self.fps)

        #Setup Microphone Device index
        self.left_device_index = left_channel_index
        self.right_device_index = right_channel_index

        #Create data buffer
        self.audio_data_buffer = AudioData()

        #Create Mic Object
        self.left_microphone = pi_audio.Microphone()
        #self.right_microphone = pi_audio(input_device_index = self.right_device_index)

    def start(self):
        if not self._started:
            self.left_microphone.start_stream()
            #self.right_microphone.start_stream()

        #Update the start variable
        self._started = True
        return self._started

    def stop(self):
        if self._started:
            self.left_microphone.stop_stream()
            #self.right_microphone.stop_stream()
            
        #Update the start variable
        self._started = False
        return self._started

    def publish_data(self):
        #Ensure the object has started
        if not self._started: return False

        #Update data variable
        data = self.left_microphone.get_stream_buffer()
        self.audio_data_buffer.left_data = data
        self.audio_data_buffer.right_data = data

        #Publish data
        self.audio_data_pub.publish(self.audio_data_buffer)
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
    audio_pub = AudioPublisher()

    #Start publisher
    audio_pub.start()

    #Run publisher
    audio_pub.run()

    #Stop publisher
    audio_pub.stop()
    
if __name__=='__main__':
    main()
