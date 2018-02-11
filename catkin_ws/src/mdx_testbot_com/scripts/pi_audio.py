#!/usr/bin/env python

import sys
import wave
import time
import array
import struct
import pyaudio
import numpy as np
import scipy.io.wavfile as scipy_wavfile

FREQUENCY = 44100
CHUNK_SIZE = 882

class SoundFile(object):
    """docstring for SoundFile"""
    def __init__(self, filename="test_sound.wav", chunk_size=CHUNK_SIZE, default_channel=2):
        super(SoundFile, self).__init__()
        
        self.__filename = filename
        self.__default_channel = default_channel
        self.__rate = 44100
        self.__chunk_size = chunk_size
        self.current_index = -1
        self.data_length = 0
        self.__wav_data = None

        self.rate = self.__rate
        self.chunk_size = self.__chunk_size

    def start_stream(self):
        self.__rate, self.__wav_data = scipy_wavfile.read(self.__filename, True)
        self.data_length = np.shape(self.__wav_data)[0]
        if self.data_length > 0:
            self.current_index = 0

    def get_stream_buffer(self):
        end_index = self.current_index + self.__chunk_size
        
        if end_index >= self.data_length:
            return []
        elif self.current_index >= 0:
            data = self.__wav_data[self.current_index:end_index, self.__default_channel-1]
            self.current_index += self.__chunk_size
            return data.tolist()
        else:
            return []

    def stop_stream(self):
        self.current_index = -1

class Microphone(object):
    def __init__(self, input_device_index=None, threshold=500, chunk_size=CHUNK_SIZE, fmt=pyaudio.paInt16, rate=FREQUENCY):
        self.threshold = 500
        self.chunk_size = chunk_size
        self.fmt = fmt
        self.rate = rate

        self.p = None
        self.stream = None
        self.data = array.array('h')
        self.reset_chunked_stream_buffer()
        self.input_device_index = input_device_index

    def _normalize(self):
        MAXIMUM = 16384
        times = float(MAXIMUM)/max(abs(i) for i in self.data)
        rbuffer = array.array('h')
        for i in self.data:
            rbuffer.append(int(i*times))
        self.data = rbuffer
        return self.data

    def _trim(self):
        def __trim(data):
            started = False
            rbuffer = array.array('h')

            for i in data:
                if not started and abs(i)>self.threshold:
                    started = True; rbuffer.append(i)
                elif started:
                    rbuffer.append(i)
            return rbuffer
        #Trim to the left
        self.data = __trim(self.data)
        #Trim to the right
        self.data.reverse(); self.data = __trim(self.data)
        self.data.reverse()
        return self.data

    def _add_silence(self, seconds):
        rbuffer = array.array('h', [0 for i in xrange(int(seconds*self.rate))])
        rbuffer.extend(self.data)
        rbuffer.extend([0 for i in xrange(int(seconds*self.rate))])
        self.data = rbuffer
        return self.data

    def record(self, seconds):
        self.start_stream()
        self.data = array.array('h')
        start_time = time.time()
        
        while time.time() - start_time < seconds:
            # little endian, signed short
            rbuffer = array.array('h', self.stream.read(self.chunk_size))
            if sys.byteorder == 'big': rbuffer.byteswap()
            self.data.extend(rbuffer)

        #Get this before closing the stream
        sample_width = self.p.get_sample_size(self.fmt)
        self.stop_stream()

        #Process data
        self._normalize(); self._trim(); self._add_silence(0.5)
        return (sample_width, self.data)

    def start_stream(self):
        self.p = pyaudio.PyAudio()
        if type(self.input_device_index) == type(None):
            self.stream = self.p.open(format=self.fmt, channels=1, rate=self.rate,
                                      input=True, frames_per_buffer=self.chunk_size)
        else:
            try:
                self.stream = self.p.open(format=self.fmt, channels=1, rate=self.rate,
                                          input=True, input_device_index=self.input_device_index, frames_per_buffer=self.chunk_size)
            except:
                self.input_device_index = None
        return not isinstance(self.stream, type(None))

    def get_stream_buffer(self):
        self.data = array.array('h', self.stream.read(self.stream.get_read_available()))
        if sys.byteorder == 'big': self.data.bytesswap()

        #Get this before closing the stream
        sample_width = self.p.get_sample_size(self.fmt)

        #Process data
        #self._normalize(); self._trim();
        return self.data.tolist()

    def get_chunked_stream_buffer(self):
        data = []
        
        self.chunked_data += self.get_stream_buffer()
        if len(self.chunked_data) >= self.chunk_size:
            data = self.chunked_data[0:self.chunk_size]
            self.chunked_data = self.chunked_data[self.chunk_size:]
        
        return data

    def get_recent_chunked_stream_buffer(self):
        data = []
        
        self.chunked_data += self.get_stream_buffer()
        if len(self.chunked_data) >= self.chunk_size:
            data = self.chunked_data[-self.chunk_size:]
            self.chunked_data = []
        
        return data

    def reset_chunked_stream_buffer(self):
        self.chunked_data = []

    def stop_stream(self):
        self.stream.stop_stream()
        self.stream.close()
        self.p.terminate()
        self.p = None; self.stream = None
        return True

    def record_to_file(self, path):
        self.record()
        return self.save_to_file(path=path)

    def save_to_file(self, path, sample_width=2):
        data = struct.pack('<' + ('h'*len(self.data)), *self.data)
        wf = wave.open(path, 'wb')
        wf.setnchannels(1)
        wf.setsampwidth(sample_width)
        wf.setframerate(self.rate)
        wf.writeframes(data)
        wf.close()
        return True


class Speaker(object):
    def __init__(self, fmt=pyaudio.paInt16, num_channels=1, rate=FREQUENCY):
        self.fmt = fmt
        self.num_channels = num_channels
        self.rate = rate
        self.data = None

    def start_stream(self):
        self.p = pyaudio.PyAudio()
        self.stream = self.p.open(format=self.fmt, channels=self.num_channels, rate=self.rate, output=True)
        return True
        
    def push_data(self, data):
        data = array.array('h',data)
        self.data = struct.pack('<' + ('h'*len(data)), *data)
        self.stream.write(self.data)
        return True

    def stop_stream(self):
        self.p.terminate()
        self.stream.stop_stream()
        self.stream.close()
        return True
       
    def save_to_file(self, data, path):
        data = array.array('h',data)
        data = struct.pack('<' + ('h'*len(data)), *data)
        wf = wave.open(path, 'wb')
        wf.setnchannels(1)
        wf.setsampwidth(2)
        wf.setframerate(self.rate)
        wf.writeframes(data)
        wf.close()
        return True

    def close(self):
        self.p.terminate()

if __name__ == '__main__':
    print "--Recording--"
    m = Microphone()
    m.record(5)
    print "--  Done   --"

    print "-- Playing --"
    s = Speaker()
    s.start_stream()
    s.push_data(m.data.tolist())
    print "--  Done   --"
    s.stop_stream()

