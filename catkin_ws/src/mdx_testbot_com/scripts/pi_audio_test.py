#!/usr/bin/env python

#Import support libraries
import time
import pi_audio
import pi_signal

FREQUENCY = 44100
CHUNK_SIZE = 882

def main():
    print "--Recording--"
    m = pi_audio.Microphone()
    m.record(5)
    print "--  Done   --"

    print "-- Playing --"
    s = pi_audio.Speaker()
    s.start_stream()
    s.push_data(m.data.tolist())
    print "--  Done   --"
    s.stop_stream()


# Ensure mic is working properly
def main_1():
    print "Getting mic ..."
    m = pi_audio.Microphone()

    print "Starting stream ...",
    print m.start_stream()

    gdn = None
    
    for i in xrange(3):
        print "Getting stream ...",
        data = m.get_stream_buffer()
        print len(data)
        if len(data) > 0:
            fft = pi_signal.fft_object(CHUNK_SIZE, FREQUENCY)
            gdn = fft.get_group_note_for_data(data)

    print "Stoping stream ..."
    m.stop_stream()
    return m,gdn

# Real time sound analysis
def main_2():
    short_term_mem = []
    data_cache = dict()
    
    m = pi_audio.Microphone(); m.start_stream()
    fft = pi_signal.fft_object(CHUNK_SIZE, FREQUENCY)
    count = 0
    data = list()
    while True:
        data += m.get_stream_buffer()
        if len(data) >= CHUNK_SIZE:
            bar = fft.get_group_note_for_data(data[0:CHUNK_SIZE])[0].getasstr()
            if bar in data_cache.keys():
                data_cache[bar] = [time.time(), data_cache[bar][1]+1];
            else:
                data_cache[bar] = [time.time(), 1];

            # FIFO buffer as short-term memory
            if bar in short_term_mem:
                short_term_mem.remove(bar)
            short_term_mem = [bar] + short_term_mem
                
            print "{0} @ {2} | {1} vs {3}".format(bar, count, data_cache[bar], len(data_cache.keys()))
            #time.sleep(.2)
            count += 1

            # Delete used data portion
            data = data[CHUNK_SIZE:]
    return short_term_mem, data_cache, mic

# Memory real time sound analysis
def main_25():
    MAX_MEM_WORD_LENGTH = 20
    
    short_term_mem = []
    data_cache = dict()
    
    m = pi_audio.Microphone(); m.start_stream()
    fft = pi_signal.fft_object(CHUNK_SIZE, FREQUENCY)
    count = 0
    data = list()
    word = list(); words = list(); heard_time = list(); word_freq_count = list()
    while True:
        data += m.get_stream_buffer()
        if len(data) >= CHUNK_SIZE:
            bar = fft.get_group_note_for_data(data[0:CHUNK_SIZE])[0].getasstr()
            word.append(bar)

            if len(word) <= 0:
                pass
            elif word in words:
                index = words.index(word)
                heard_time[index] = time.time()
                word_freq_count[index] += 1
            elif not word in words:
                words.append(word)
                heard_time.append(time.time())
                word_freq_count.append(1)
            elif (len(word) >= MAX_MEM_WORD_LENGTH):
                word = list()
                
            print "word = {0}".format(word)
            
            # Delete used data portion
            data = data[CHUNK_SIZE:]
    return words, heard_time, word_freq_count, mic

# Dynamic real time sound analysis
def main_3():
    short_term_mem = []
    data_cache = dict()
    
    m = pi_audio.Microphone(); m.start_stream()
    count = 0
    data = list()
    while True:
        data += m.get_stream_buffer()
        if len(data) > 0:
            fft = pi_signal.fft_object(len(data), FREQUENCY)
            bar = fft.get_group_note_for_data(data[0:CHUNK_SIZE])[0].getasstr()
            if bar in data_cache.keys():
                data_cache[bar] = [time.time(), data_cache[bar][1]+1];
            else:
                data_cache[bar] = [time.time(), 1];

            # FIFO buffer as short-term memory
            if bar in short_term_mem:
                short_term_mem.remove(bar)
            short_term_mem = [bar] + short_term_mem
                
            print "{0} @ {2} | {1} vs {3}".format(bar, count, data_cache[bar], len(data_cache.keys()))
            time.sleep(.1)
            count += 1
    return short_term_mem, data_cache, mic

if __name__ == '__main__':
    short_term_mem, data_cache, mic = main_2()
##    #words, time, word_freq_count, mic = main_25()
##    MAX_MEM_WORD_LENGTH = 20
##    
##    short_term_mem = []
##    data_cache = dict()
##    
##    m = pi_audio.Microphone(); m.start_stream()
##    fft = pi_signal.fft_object(CHUNK_SIZE, FREQUENCY)
##    count = 0
##    data = list()
##    word = list(); words = list(); heard_time = list(); word_freq_count = list()
##    while True:
##        data += m.get_stream_buffer()
##        if len(data) >= CHUNK_SIZE:
##            bar = fft.get_group_note_for_data(data[0:CHUNK_SIZE])[0].getasstr()
##            word.append(bar)
##
##            if len(word) <= 0:
##                pass
##            elif word in words:
##                index = words.index(word)
##                heard_time[index] = time.time()
##                word_freq_count[index] += 1
##            elif not word in words:
##                words.append(word)
##                heard_time.append(time.time())
##                word_freq_count.append(1)
##
##            if (len(word) >= MAX_MEM_WORD_LENGTH):
##                word = list()
##
##            max_word_index = word_freq_count.index(max(word_freq_count))
##            print "mode word = {0}\nlength={1} \n".format(words[max_word_index], word_freq_count[max_word_index])
##            
##            # Delete used data portion
##            data = data[CHUNK_SIZE:]
##        
