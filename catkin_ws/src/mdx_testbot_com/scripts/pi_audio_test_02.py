#!/usr/bin/env python

#Import support libraries
from node_cluster import NodeCluster, ChunkStreamSimultaneousProcessor
import pi_signal
import pi_audio
import json
import time
import os


PACKAGE_NAME = "mdx_testbot_com"
ABS_FILE_PATH = os.path.dirname(os.path.realpath(__file__))
LOG_DIR = "{0}/{1}/logs/".format(ABS_FILE_PATH[:ABS_FILE_PATH.rfind("/{0}".format(PACKAGE_NAME))], PACKAGE_NAME)
SOUND_DIR = "{0}/{1}/sounds/".format(ABS_FILE_PATH[:ABS_FILE_PATH.rfind("/{0}".format(PACKAGE_NAME))], PACKAGE_NAME)

print "LOG_DIR",LOG_DIR
print "SOUND_DIR",SOUND_DIR

class NoteGroupOverTimeGraph(object):
	"""docstring for NoteGroupOverTimeGraph"""
	def __init__(self, log_filename="note_group_over_time_graph.log"):
		super(NoteGroupOverTimeGraph, self).__init__()

		self.__log_formatter = lambda data : "{0}\n\n".format(data)
		self.__log_filename = LOG_DIR + log_filename

		with open(self.__log_filename, 'w'):
			pass # Empty file

	def upload_data(self, data):
		if not data: return
		
		note_group = data[1]
		all_frequencies = []; all_intensities = []
		for note in note_group.notes:
			all_frequencies.append(note.freq)
			all_intensities.append(note.intensity)

		data = list(zip(all_frequencies, all_intensities))
		self.__log(json.dumps(data))

	def cleanup(self):
		pass

	def __log(self, data):
		with open(self.__log_filename, 'a') as f:
			f.write( self.__log_formatter(data) ); f.flush()


class DataPrinter(object):
	"""docstring for DataPrinter"""
	def __init__(self):
		super(DataPrinter, self).__init__()

	def upload_data(self, data):
		print data

	def cleanup(self):
		print "DataPrinter is clean"

class PrimaryPitchPrinter(object):
	"""docstring for PrimaryPitchPrinter"""
	def __init__(self):
		super(PrimaryPitchPrinter, self).__init__()

	def upload_data(self, data):
		pitch_note = data[0]
		print pitch_note.getasstr()

	def cleanup(self):
		print "PrimaryPitchPrinter is clean"

class NoteGroupChangeLog(object):
	"""docstring for NoteGroupChangeLog"""
	def __init__(self, log_filename="note_group_change.log"):
		super(NoteGroupChangeLog, self).__init__()
		
		self.__last_note_group = None
		self.__log_filename = LOG_DIR + log_filename
		self.__log_formatter = lambda data : "{0}\n{1}\n{2}\n\n".format(time.ctime(), time.time(), data)

	def upload_data(self, data):
		if not data: return

		note_group = data[1]
		if not self.__last_note_group:
			self.__last_note_group = note_group
			self.__log(note_group.get_string_repr())
			return

		for i in xrange(len(note_group)):
			new_note = note_group.notes[i]
			for j in xrange(len(self.__last_note_group)):
				old_note = self.__last_note_group.notes[j]

				if new_note.freq != old_note.freq:
					self.__last_note_group = note_group
					self.__log(note_group.get_string_repr())
					return

	def cleanup(self):
		pass

	def __log(self, data):
		with open(self.__log_filename, 'a') as f:
			f.write( self.__log_formatter(data) ); f.flush()

class NoteFrequencyTracker(object):
	"""docstring for NoteFrequencyTracker"""
	def __init__(self, track_time=1.0, log_filename="note_frequency_tracker.log"):
		super(NoteFrequencyTracker, self).__init__()
		self.__log_filename = LOG_DIR + log_filename
		self.__log_formatter = lambda data : "{0}\n{1}\n{2}\n\n".format(time.ctime(), time.time(), data)

		self.__data_bank = dict()
		self.__track_time_limit = track_time

	def upload_data(self, data):
		if not data: return
		
		self.__data_bank[time.time()] = data[1]
		data_keys = self.__data_bank.keys(); data_keys.sort(); data_keys.reverse()
		
		for k in data_keys:
			time_diff = time.time() - k
			if time_diff >= self.__track_time_limit:
				self.__data_bank.pop(k)

		all_notes_as_str = []
		for note_group in self.__data_bank.values():
			for note in note_group.notes:
				all_notes_as_str.append(str(note))

		notes_as_str = list(set(all_notes_as_str))
		cost = [round(all_notes_as_str.count(note_as_str)/float(len(all_notes_as_str)), 2) for note_as_str in notes_as_str]
		
		filter_func = lambda item : item[1]
		foo = list(zip(notes_as_str, cost))
		
		data = sorted(foo, key=filter_func, reverse=True)

		self.__log(data)

	def cleanup(self):
		pass

	def __log(self, data):
		with open(self.__log_filename, 'a') as f:
			f.write( self.__log_formatter(data) ); f.flush()


class SpeakerStreamer(object):
	"""docstring for SpeakerStreamer"""
	def __init__(self):
		super(SpeakerStreamer, self).__init__()
		self.__speaker = pi_audio.Speaker();self.__speaker.start_stream()

	def upload_data(self, data):
		self.__speaker.push_data(data)

	def cleanup(self):
		self.__speaker.stop_stream()
		

def test_1():
	mic = pi_audio.Microphone();mic.start_stream()

	sample_frequency = mic.rate
	number_of_sample_points = mic.chunk_size
	fft = pi_signal.fft_object(number_of_sample_points, sample_frequency)

	def __generate_data():
		data = mic.get_recent_chunked_stream_buffer()
		if data:
			data = fft.get_group_note_for_data(data)
			return data
		return None

	cluster = NodeCluster()
	
	cluster.add_parallel_node(
		PrimaryPitchPrinter()
		)
	
	cluster.add_parallel_node(
		NoteGroupChangeLog()
		)
	
	cluster.add_parallel_node(
		NoteFrequencyTracker()
		)

	cluster.add_parallel_node(
		NoteGroupOverTimeGraph()
		)

	cluster.add_parallel_node(
		pi_signal.NoteClustifier(LOG_DIR + "note_clusters_over_time.log")
		)

	task_processor = ChunkStreamSimultaneousProcessor()
	task_processor.add_data_inline_process(__generate_data, cluster)
	task_processor.start_processing() # blocking
	task_processor.stop_processing()


def test_2():
	sound_file = pi_audio.SoundFile(filename=SOUND_DIR + "name-01.wav");sound_file.start_stream()

	sample_frequency = sound_file.rate
	number_of_sample_points = sound_file.chunk_size
	fft = pi_signal.fft_object(number_of_sample_points, sample_frequency)
	data = None

	def __generate_data():
		global data
		data = sound_file.get_stream_buffer()
		if data:
			return fft.get_group_note_for_data(data)
		return None

	def __generate_data_2():
		return "Progress {0}%".format( sound_file.current_index / float(sound_file.data_length) * 100.0 )

	cluster = NodeCluster()
	
	cluster.add_parallel_node(
		PrimaryPitchPrinter()
		)
	
	cluster.add_parallel_node(
		NoteGroupChangeLog()
		)
	
	cluster.add_parallel_node(
		NoteFrequencyTracker()
		)

	cluster.add_parallel_node(
		NoteGroupOverTimeGraph()
		)

	cluster_2 = NodeCluster()
	cluster_2.add_parallel_node(
		DataPrinter()
		)

	task_processor = ChunkStreamSimultaneousProcessor()
	task_processor.add_data_inline_process(__generate_data, cluster)
	#task_processor.add_data_inline_process(__generate_data_2, cluster_2)

	task_processor.start_processing() # blocking
	task_processor.stop_processing()

if __name__ == '__main__':
	test_1()