#!/usr/bin/env python

#Setup import files from the manifest file
import rospy

#Import support libraries
import time
import pi_audio
import pi_signal

#Import the necessary message format needed
from mdx_testbot_com.msg import AudioData

FREQUENCY = 44100
CHUNK_SIZE = 882

class AudioSubscriber(object):
    def __init__(self, chunk_size=CHUNK_SIZE, rate=FREQUENCY):
        #Create started variable
        self._started = False

        #Initialize this module as a ros node
        rospy.init_node('audio_subscriber', anonymous=True)

        #Initialize speaker
        self.audio_output = pi_audio.Speaker()

        #Create Data buffer
        self.left_data = []
        self.right_data = []

        #Create signal processing object
        self.chunk_size = chunk_size; self.rate = rate
        self.fft_object = pi_signal.fft_object(self.chunk_size, self.rate)

    def start(self):
        if not self._started:
            self.audio_output.start_stream()
            rospy.Subscriber("AudioData_01", AudioData, self.callback)

        #Update the start variable
        self._started = True

    def stop(self):
        if self._started:
            self.audio_output.stop_stream()

        #Update the start variable
        self._started = False
        exit()

    def run(self):
        mbuffer = []
        msize = 500
        while not rospy.is_shutdown():
            ldata = []; rdata = []
            if len(self.left_data) > self.chunk_size and len(self.right_data) > self.chunk_size:
                ldata = self.left_data[0:882]; rdata = self.right_data[0:882]
                self.left_data = self.left_data[882:]; self.right_data = self.right_data[882:]
            else:
                continue
            
            left_pitch = self.fft_object.get_group_note_for_data(ldata)[0]
            right_pitch = self.fft_object.get_group_note_for_data(rdata)[0]
            bar = tuple(left_pitch.getasstr().split(' '))

            bar_string = "K:{0} P:{1} C:{2}".format(bar[0],bar[1],bar[2])
            
            mbuffer.append(bar)
            if len(mbuffer) > msize:mbuffer = mbuffer[1:]
            max_index = 0;max_count = 0

            #Get unique bar elements only
            foo = tuple(set(mbuffer))
            
            for index in xrange(len(foo)):
                count = mbuffer.count(foo[index])
                if count > max_count:
                    max_count = count
                    max_index = index

            mdata_string = "K:{0} P:{1} C:{2} C:{3}".format(foo[max_index][0], foo[max_index][1], foo[max_index][2], max_count)
            print "{0} - {1}".format(mdata_string, bar_string)
            
            

    def callback(self, data):
        #print "caller_id = {0}".format(rospy.get_caller_id())
        self.left_data += data.left_data
        self.right_data += data.right_data

def main():
    #Create a subscriber
    audio_sub = AudioSubscriber()

    #Start subscriber
    audio_sub.start()

    #Run subscriber
    audio_sub.run()

    #Stop subscriber
    audio_sub.stop()

if __name__ == '__main__':
    main()

