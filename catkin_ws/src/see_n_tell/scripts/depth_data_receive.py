#!/usr/bin/env python
PKG = "see_n_tell"
import roslib; roslib.load_manifest(PKG)

import rospy
from basic_header import *
from rospy.numpy_msg import numpy_msg
from rospy_tutorials.msg import Floats
from std_msgs.msg import UInt16MultiArray
from std_msgs.msg import MultiArrayDimension

def callback(data):
    #rospy.loginfo(rospy.get_caller_id() + "I heard %s", data.data)
    print rospy.get_name(), "I heard %s"%str(data.data)
    
def listener():
    rospy.init_node("depth_data_receive", anonymous=True)
    rospy.Subscriber("DepthCameraData", numpy_msg(UInt16MultiArray), callback)
    rospy.spin()

if __name__ == '__main__':
    listener()
