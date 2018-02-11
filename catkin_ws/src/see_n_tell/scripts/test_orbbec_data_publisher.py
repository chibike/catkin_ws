#!/usr/bin/env python
import rospy
from std_msgs.msg import String
from orbbec_class import OrbbecDepthCamera

def talker():
    pub = rospy.Publisher("DepthCameraData", String, queue_size=10)
    rospy.init_node('orbbec_data_publisher', anonymous=True)
    rate = rospy.Rate(10)
    while not rospy.is_shutdown():
        hello_str = "hello world %s" % rospy.get_time()
        rospy.loginfo(hello_str)
        pub.publish(hello_str)
        rate.sleep()


if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass
