#!/usr/bin/env python
PKG = "see_n_tell"
import roslib; roslib.load_manifest(PKG)
import rospy

from microphone_n_speaker_class import Speaker
from basic_header import *
import struct

from rospy.numpy_msg import numpy_msg
from std_msgs.msg import Float64MultiArray
from std_msgs.msg import MultiArrayDimension

class SoundAnalyzer(object):
    def __init__(self, channels=2, sample_rate=44100, block_duration=20):
        #Intialize variables
        self._created = False
        self._ch = channels
        self._fs = sample_rate
        self._bk_d = block_duration
        self._bk_w = int((self._bk_d/1000.0) * self._fs)
        self.frames = None

        #Define structure format for incoming data
        self.fmt = 'd'*self._bk_w

        #Setup speaker object
        self.speaker = Speaker(sample_rate)

        #Intialize ros
        rospy.init_node("sound_stream_analzer_listener", anonymous=True)

    def start(self):
        if not self._created:
            print "Starting subscription ..."
            rospy.Subscriber("SoundData_1", numpy_msg(Float64MultiArray), self.callback)
            print "Done."
        self._created = True

    def end(self):
        self._created = False
        self.speaker.stop()
        exit()

    def run(self):
        #Calculate Playback buffer length
        time_interval = 20
        block_width = time_interval/1000.0 * self._fs
        while not rospy.is_shutdown() and self._created:
            if type(self.frames) == type(None):
                continue
            elif len(self.frames) >= block_width:
                #Get sound frame
                frame = self.frames
                self.frames = None
                
                direction = self.getSoundDirection(frame)
                if direction < 0:
                    print "Dir =", 'Right', p
                elif direction > 0:
                    print "Dir =", 'Left', p
                
    def callback(self, data):
        #Get Data
        frame = data.data
        frame.shape = (self._bk_w, self._ch)

        #print len(frame),frame[0]

        #Save sound frame
        if type(self.frames) == type(None):
            self.frames = frame
        else:
            self.frames = np.concatenate((self.frames,frame))

    def getSoundDirection(self, frame):
        direction = getLeadIndexf(frame, nom_min=-1, nom_max=1, max_index=100)[0]
        if direction >= 0:
            return -1
        else:
            return 1


def main():
    my_analyzer = SoundAnalyzer()
    my_analyzer.start()
    my_analyzer.run()
    my_analyzer.end()

if __name__ == '__main__':
    print "Starting..."
    main()
