#!/usr/bin/env python

import json
import math
import numpy as np
import scipy.fftpack
import matplotlib.pyplot as plt

def cosf(deg):
    return math.cos(math.radians(deg))

def sinf(deg):
    return math.sin(math.radians(deg))

def tanf(deg):
    return math.tan(math.radians(deg))

class Note(object):
    def __init__(self, freq=None, note=None, note_pitch=None, cents=None, intensity=0):
        self.freq=freq
        self.note=note.strip()
        self.cents=cents
        self.note_pitch = note_pitch
        self.intensity = intensity

    def __sub__(self, note):
        if not isinstance(note, Note):
            return NotImplemented
        else:
            A = self.intensity; B = note.intensity
            a = self.freq; b = note.freq

            diff = ( (A-B) + (B*cosf(2.0*b))-(A*cosf(2.0*a)) ) /2.0
            return -diff

    def __str__(self):
        return self.getasstr()

    def getasstr(self):
        return "{0} {1} {2}".format(self.note, self.note_pitch, self.cents)

class NoteGroup(object):
    def __init__(self, notes):
        self.notes = notes

    def __sub__(self, note_group):
        if not isinstance(note_group, NoteGroup):
            return NotImplemented
        else:
            other_notes = note_group.notes
            diff_array = []
            for i in range( min(len(self.notes), len(other_notes)) ):
                note1 = self.notes[i]; note2 = other_notes[i]
                diff_array.append(note1 - note2)
            return diff_array

    def __len__(self):
        return len(self.notes)

    def __str__(self):
        return str(self.get_string_repr())

    def get_notes(self):
        return self.notes

    def get_frequencies(self):
        return np.array([note.freq for note in self.notes])

    def get_intensities(self):
        return np.array([note.intensity for note in self.notes])

    def get_string_repr(self):
        return [note.getasstr() for note in self.notes]

class NoteCluster(NoteGroup):
    """docstring for NoteCluster"""
    def __init__(self, notes=[]):
        super(NoteCluster, self).__init__(notes)
        
        self.notes = []
        self.music_note = None
        self.cents = 0
        self.frame_id = 0

        self.__update()

    def __update(self):
        if len(self.notes) <= 0:
            return

        self.music_note = self.notes[0].note
        self.cents = float(sum([note.cents for note in self.notes]))/len(self.notes)

    def append(self, note, frame_id=0):
        if not isinstance(note, Note): return False
        self.notes.append(note)

        if len(self.notes) == 1:
            self.__update()
        else:
            self.cents = (self.cents + note.cents)/2.0

        self.frame_id = frame_id
        return True

    def merge(self, note_cluster):
        if not isinstance(note_cluster, type(self)): return False

        self.notes += note_cluster.notes
        self.__update()

        self.frame_id = max(note_cluster.frame_id, self.frame_id)
        return True

    def bluck_append(self, notes, frame_id=0):
        self.notes += notes
        self.__update()
        self.frame_id = frame_id

    def check_fit(self, obj, cents_padding=100):
        if isinstance(obj, Note):
            if len(self.notes) <= 0: return True
            if not (obj.note == self.music_note): return False
            if float(abs(obj.cents - self.cents))/self.cents > cents_padding: return False
            return True
        elif isinstance(obj, type(self)):
            if len(self.notes) <= 0: return True
            if not (obj.music_note == self.music_note): return False
            if float(abs(obj.cents - self.cents))/self.cents > cents_padding: return False
            return True
        return False

    def filter_notes(self, notes, cents_padding=100, frame_id=0):
        bad = []

        if len(notes) <= 0: return bad

        if len(self.notes) <= 0:
            self.append(notes[0], frame_id)
            self.frame_id = frame_id
            notes = notes[1:]

        for note in notes:
            if self.check_fit(note, cents_padding):
                self.notes.append(note)
                self.cents = (self.cents + note.cents)/2.0
                self.frame_id = frame_id
            else:
                bad.append(note)

        return bad

    def filter_clusters(self, clusters, cents_padding=100):
        bad = []

        if len(clusters) <= 0: return bad

        if len(self.notes) <= 0:
            self.merge(clusters[0])
            clusters = clusters[1:]

        for cluster in clusters:
            if self.check_fit(cluster, cents_padding):
                self.merge(cluster)
            else:
                bad.append(cluster)

        return bad

class NoteClustifier(object):
    """docstring for NoteClustifier"""
    def __init__(self, log_filename="note_clusters_over_time.log"):
        super(NoteClustifier, self).__init__()

        self.__log_formatter = lambda data : "{0}\n\n".format([i.get_string_repr() for i in data])
        self.__log_filename = log_filename

        self.frame_id = 0
        self.note_clusters = []

        self.max_break_interval = 10
        self.filter_function = lambda note_cluster: (self.frame_id - note_cluster.frame_id) <= self.max_break_interval
        self.inv_filter_function = lambda note_cluster: not self.filter_function(note_cluster)

        with open(self.__log_filename, 'w'):
            pass # Empty file

    def upload_data(self, data):
        if not data: return

        tmp_note_clusters = []
        notes = data[1].notes
        while len(notes) > 0:
            note_cluster = NoteCluster()

            bad_notes = note_cluster.filter_notes(notes, self.frame_id)

            if len(note_cluster.notes) > 0:
                tmp_note_clusters.append(note_cluster)
            
            notes = bad_notes

        self.merge_cluster(tmp_note_clusters)
        self.frame_id += 1

    def merge_cluster(self, tmp_note_clusters):
        if len(self.note_clusters) <= 0:
            self.note_clusters = tmp_note_clusters

        recent_note_cluster = filter(self.filter_function, self.note_clusters)
        old_note_cluster = filter(self.inv_filter_function, self.note_clusters)

        index = 0;
        p = len(tmp_note_clusters)
        while True:
            if len(tmp_note_clusters) <= 0:
                break

            if index >= len(recent_note_cluster):
                break

            tmp_note_clusters = recent_note_cluster[index].filter_clusters(tmp_note_clusters)
            index += 1
        q = len(tmp_note_clusters)

        bar = round(float(p-q)/p * 100.0, 2)
        if bar > 0:
            print "merged: {0}%".format(bar)

        self.note_clusters = recent_note_cluster + old_note_cluster + tmp_note_clusters
        #self.__log(self.note_clusters)

    def cleanup(self):
        with open(self.__log_filename, 'w'):
            pass # Empty file

        self.__log(self.note_clusters)

    def __log(self, data):
        with open(self.__log_filename, 'w') as f:
            f.write( self.__log_formatter(data) ); f.flush()

class MusicNoteConverter():
    def __init__(self):
        pass

    def lognote(self, freq):
        return ((math.log(freq) - math.log(440)) / math.log(2)) + 4.0

    def alognote(self, lnote):
        return math.exp(((lnote - 4.0)*math.log(2)) + math.log(440))

    def get_note(self, freq_n_intensity):
        freq, intensity = freq_n_intensity
        if freq == 0:
            return Note(freq, "#", 0, 0)
        
        lnote = self.lognote(freq)
        foo = math.floor( lnote )
        cents = 1200 * ( lnote - foo )
        note_table = "A A#B C C#D D#E F F#G G#"
        offset = 50.0
        x = 2
        if ( cents < 50 ): note = "A "
        elif ( cents >= 1150 ):
            note = "A "
            cents -= 1200
            foo += 1
        else:
            for j in range(1, 12):
                if ( cents >= offset and cents < (offset + 100 ) ):
                    note = note_table[x] + note_table[x+1]
                    cents -= ( j * 100 )
                    break
                offset += 100
                x += 2
        cents = round ( cents, 2 )
        return Note(freq, note, int(foo), cents, intensity)

    def convert_to_notes(self, freq_n_intensity):
        return [self.get_note((freq, intensity)) for freq,intensity in freq_n_intensity]

    def get_freq(self, note):
        if note.note.startswith('#'):
            return 0
        
        p = note.split(' ')
        cents = p[2]
        note = p[0] + ' ' + p[1]
        
        key,foo = note.split(' ')
        foo = float(foo)
        note_table = "A A#B C C#D D#E F F#G G#"
        x = note_table.find(key)
        n = int((x-2)/2) + 1
        if not note.startswith("A "):
            for j in range(n):
                cents += 100
        elif cents >= 50:
            cents += 1200
            foo -= 1
        lnote = (cents/1200.0) + foo
        freq = self.alognote( lnote )
        return freq

    def differentiate(self, notes):
        d_notes = []
        for i in range(len(notes)-1):
            d_notes.append( notes[i+1]-notes[i] )
        return d_notes

    def test(self, start=1, stop=22000, step=10):
        found_err = False
        freq = start
        while freq < stop:
            note = self.get_note((freq, 0))
            if round(get_freq(note)) != round(freq):
                print "Error = freq({0} not note({1}))".format(freq, note)
                found_err = True
            freq += step
        return not found_err

class fft_object():
    def __init__(self, number_of_sample_points, sample_frequency):
        self.N = number_of_sample_points
        self.T = 1.0/float(sample_frequency) # === sample_spacing/sample_interval
        self.xf = np.linspace(0.0, 1.0/(2.0*self.T), self.N/2)

        self.note_converter = MusicNoteConverter()

    def calculate(self, data):
        self.yf = scipy.fftpack.fft(data)
        self.graph_data = 2.0/self.N * np.abs(self.yf[:self.N//2])
        return self.graph_data

    def locate_peaks(self, data):
        #locate peaks by comparing current position with it's right and left partner
        data = self.calculate(data)

        ls = np.copy(data)
        rs = np.copy(data)

        ls = np.roll(ls, -1)
        ls[-1] = 0

        rs = np.roll(rs, 1)
        rs[0] = 0
        
        data[np.logical_not(np.logical_and(ls < data, data > rs))] = 0
        
        frequencies = self.xf[np.where(data>0)].ravel()
        intensities = data[np.where(data>0)].ravel()
        peak_locations = self.filter_peaks(frequencies, intensities)

        #Select the location with the minimum freq out of the locations with the maximum intensity
        pitch = peak_locations[np.where(peak_locations[:,1] == max(peak_locations[:,1]))] #Select by maximum intensity
        pitch = pitch[np.where(pitch[:, 0] == min(pitch[:,0]))][0] #Select by minimum freq
        self.graph_data = data
        return (data, peak_locations, pitch)

    def filter_peaks(self, frequencies, intensities):
        intensity_min_cut_off_threshold = np.average(intensities)*0.3
        frequency_min_cut_off_threshold = 30
        frequency_max_cut_off_threshold = 21000

        intensities[np.where(intensities < intensity_min_cut_off_threshold)] = 0
        intensities[np.where(frequencies < frequency_min_cut_off_threshold)] = 0
        intensities[np.where(frequencies > frequency_max_cut_off_threshold)] = 0

        frequencies = frequencies[np.where(intensities > 0)]
        intensities = intensities[np.where(intensities > 0)]
        
        return np.array(tuple(zip(frequencies, intensities)))

    def get_group_note_for_data(self, data):
        peaks,pitch = self.locate_peaks(data)[1:3]
        #print "peaks = ",peaks[:,0].tolist()
        notes_buffer = self.note_converter.convert_to_notes(peaks)
        pitch_as_note = self.note_converter.get_note(pitch)
        return (pitch_as_note, NoteGroup(notes_buffer))

    def show_plot(self, title="FFT Plot"):
        fig, ax = plt.subplots()
        ax.plot(self.xf, self.graph_data)
        ax.grid()
        ax.set_xlabel('frequency')
        ax.set_ylabel('amplitude')
        ax.set_title(title)
        plt.show()

def getSinWave(N, T, properties):
    x = np.linspace(0.0, N*T, N)
    data = []
    for prop in properties:
        if len(data) <= 0:
            data.append( float(prop[0])*np.sin( float(prop[1])*2.0*np.pi*x ) )
        else:
            data[0] = data[0] + float(prop[0])*np.sin( float(prop[1])*2.0*np.pi*x )
    return data[0]
