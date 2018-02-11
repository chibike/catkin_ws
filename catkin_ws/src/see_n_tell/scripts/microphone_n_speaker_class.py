#!/usr/bin/env python

#Import support library for sound IO devices
import sounddevice as sd

class Microphone(object):
    def __init__(self, channels=2, sample_rate=44100, stream_callback_function=None):
        #Initialize variables
        self._ch = channels
        self._fs = sample_rate
        self._dev = None
        self._stream = None
        self._stream_cf = stream_callback_function

    def _setDevice(self, name = u'ASTRA S: USB Audio (hw:2,0)'):
        #Get list of avaliable devices
        devices = sd.query_devices()

        #Find device with the appropriate name
        for index in range(len(devices)):
            if devices[index]['name'] == name:
                self._dev = index
                break

        #Verify that the device is valid
        if self._dev:
            #set device to this
            sd.default.device = self._dev
            print 'New device =', self._dev
        else:
            print 'Old device remains'

    def printDevices(self):
        print '--- Devices ---'
        print sd.query_devices()

    def stop(self):
        self.stopStream()
        sd.stop()

    def getRecording(self, duration=5000.0, blocking=False):
        #Convert duration from milli seconds to seconds
        duration = duration/1000.0

        #Return record response
        return sd.rec(
            int(duration*self._fs),
            self._fs,
            channels=self._ch,
            dtype='float64',
            blocking=blocking
            )

    def callback(self, indata, frame_length, time, status):
        if self._stream_cf:
            self._stream_cf(indata, frame_length, time, status)

    def startStream(self, duration=-1, frame_width=20):
        #Convert frame_width from milli seconds to seconds
        frame_width = frame_width / 1000.0 #ms

        #Calculate the blocksize based on the time window
        blocksize=int(self._fs*frame_width)

        #Return input stream
        self._stream = sd.InputStream(
            samplerate=self._fs,
            blocksize=blocksize,
            channels=self._ch,
            callback=self.callback
            )

        #Start stream
        self._stream.start()
        if duration > 0:
            sd.sleep(int(duration))
            self.stopStream()
        else:
            pass

    def stopStream(self):
        if self._stream:
            self._stream.close()

class Speaker(object):
    def __init__(self, sample_rate=44100):
        self._fs = sample_rate

    def playSound(self, sound=[], blocking=False):
        sd.play(sound, samplerate=self._fs, blocking=blocking)

    def playFromInputStream(self, indata, frame_length, time, status):
        if type(indata) != type(None):
            self.playSound(indata)
        else:
            print "invalid data"

    def waitUntilFinished(self):
        return sd.wait()

    def stop(self):
        sd.stop()

def main():
    speaker = Speaker()
    mic = Microphone()
    print 'Speak now...'
    speaker.playSound(mic.getRecording(5000, True), True)

if __name__ == '__main__':
    print "Staring Mic and Speaker Test..."
    main()
