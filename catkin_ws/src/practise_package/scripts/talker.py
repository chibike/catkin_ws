#!/usr/bin/env python

import rospy
from std_msgs.msg import String

def talker():
	my_name = 'talker'
	
	# Setup publisher
	publisher = rospy.Publisher('chatter', String, queue_size=10)
	
	# Initialize myself as a node
	rospy.init_node(my_name, anonymous=True)
	rate = rospy.Rate(10) # in hertz

	# Keep running until roscore shuts down
	while not rospy.is_shutdown():
		time_now = rospy.get_time()
		hello_str = "Hello, I am a Mr. {1}, and the time is {0}".format(time_now, my_name.capitalize())
		
		publisher.publish(hello_str)
		rate.sleep()

talker()