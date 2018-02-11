#!/usr/bin/env python

import numpy as np
import scipy.misc
import random
import json
import sys
import os

PACKAGE_NAME = "mdx_testbot_com"
ABS_FILE_PATH = os.path.dirname(os.path.realpath(__file__))
LOG_DIR = "{0}/{1}/logs/".format(ABS_FILE_PATH[:ABS_FILE_PATH.rfind("/{0}".format(PACKAGE_NAME))], PACKAGE_NAME)
IMAGE_DIR = "{0}/{1}/images/".format(ABS_FILE_PATH[:ABS_FILE_PATH.rfind("/{0}".format(PACKAGE_NAME))], PACKAGE_NAME)
print "LOG_DIR",LOG_DIR

FILENAME = LOG_DIR + "note_group_over_time_graph.log"
IMAGE_NAME = IMAGE_DIR + "note_group_over_time_graph.jpg"

def data_from_file(filename=FILENAME):
	data = []

	file = open(filename, 'r')
	while True:
		line = file.readline();file.readline();
		if len(line) <= 0:
			break
		elif len(line) > 1:
			data.append(json.loads(line[:-1]))
	file.close()

	return data

def get_properties(filename=FILENAME):
	min_intensity = None; max_intensity = None
	min_frequency = None; max_frequency = None
	length_of_data = 0

	file = open(filename, 'r')
	while True:
		line = file.readline();file.readline();
		if len(line) <= 0: break
		elif len(line) > 1:
			frequencies,intensities = list(zip(*json.loads(line[:-1])))
			length_of_data += 1

			if min_intensity == None:
				min_intensity = min(intensities)
			elif min(intensities) < min_intensity:
				min_intensity = min(intensities)

			if max_intensity == None:
				max_intensity = max(intensities)
			elif max(intensities) > max_intensity:
				max_intensity = max(intensities)

			if min_frequency == None:
				min_frequency = min(frequencies)
			elif min(frequencies) < min_frequency:
				min_frequency = min(frequencies)

			if max_frequency == None:
				max_frequency = max(frequencies)
			elif max(frequencies) > max_frequency:
				max_frequency = max(frequencies)
	file.close()

	return length_of_data, (min_intensity,max_intensity),(min_frequency, max_frequency)

def generate_numpy_array(filename=FILENAME):
	length_of_data, (min_intensity,max_intensity),(min_frequency, max_frequency) = get_properties(filename)

	num_of_rows = int((max_frequency - min_frequency) + 1)
	num_of_columns = length_of_data

	array = np.zeros((num_of_rows, num_of_columns))

	index = 0
	file = open(filename, 'r')
	while True:
		line = file.readline();file.readline();
		if len(line) <= 0: break
		elif len(line) > 1:
			frequencies,intensities = list(zip(*json.loads(line[:-1])))

			#frequencies = list(range(int(min_frequency), int(max_frequency), 10))
			#intensities = [random.randint(int(min_intensity), int(max_intensity)) for i in frequencies]
			for i in xrange(len(frequencies)):
				frequency = int(frequencies[i] - min_frequency)
				intensity = intensities[i] - min_intensity
				
				array[frequency, index] = intensity

			index += 1
	file.close()

	return array

def save_as_image(filename=FILENAME, image_name=IMAGE_NAME):
	array = generate_numpy_array(filename)
	scipy.misc.toimage(array).save(image_name)

print get_properties()

save_as_image()