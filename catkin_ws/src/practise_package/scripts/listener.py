#!/usr/bin/env python

import rospy
from std_msgs.msg import String

def callback(received_data):
	caller_id = rospy.get_caller_id()
	print "I heard : {1} from user {0}".format(caller_id, received_data.data)


def listener():
	my_name = 'listener'
	rospy.init_node(my_name, anonymous=True)
	rospy.Subscriber('chatter', String, callback)
	rospy.spin()

try:
	listener()
except Exception():
	print "Could not run because of an internal Err.\nPlease check your code."