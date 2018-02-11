#!/usr/bin/env python
import signal
import thread
import time

class NodeCluster(object):
	def __init__(self):
		self.__num_of_nodes = 0
		self.nodes = list()

	def get_num_of_nodes(self):
		return self.__num_of_nodes

	def add_parallel_node(self, node):
		if node:
			self.nodes.append(node)
			self.__num_of_nodes += 1
		return True

	def upload_data(self, data):
		for node in self.nodes:
			try:
				thread.start_new_thread(node.upload_data, (data,))
			except Exception as e:
				node.cleanup()
				print "Unable to start thread for node {0}".format(node)
				print "Exception : {0}".format(e)

	def cleanup(self):
		for node in self.nodes:
			node.cleanup()


class ChunkStreamSimultaneousProcessor(object):
	def __init__(self, fps=0.05):
		self.fps = fps
		self.__clusters = []
		self.__data_generators = []
		self.__num_of_simultaneous_process = 0

	def add_data_inline_process(self, data_generator, cluster):
		if data_generator and cluster:
			self.__clusters.append(cluster)
			self.__data_generators.append(data_generator)
			self.__num_of_simultaneous_process += 1

	def start_processing(self):
		try:
			while True:
				time.sleep(self.fps)

				for i in range(self.__num_of_simultaneous_process):
					try:
						data_generator = self.__data_generators[i]
						data = data_generator()

						if data:
							cluster = self.__clusters[i]
							thread.start_new_thread(cluster.upload_data, (data,))
					except Exception as e:
						print "Exception : {0}".format(e)

		except KeyboardInterrupt:
			print "\n\nInterrupt received, stopping..."
			self.stop_processing()
		except Exception as e:
			self.stop_processing()
			print "Exception : {0}".format(e)

	def stop_processing(self):
		for cluster in self.__clusters:
			cluster.cleanup()
		thread.exit()