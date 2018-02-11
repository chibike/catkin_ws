#!/usr/bin/env python
## Simple talker demo that listens to std_msgs/Strings published
## to the 'chatter' topic

import rospy
from sensor_msgs.msg import Image

def callback(data):
    #rospy.loginfo(rospy.get_caller_id() + 'I heard %s', data.data)
    print "Image height: {0}".format(data.height)
    print "Image width: {0}".format(data.width)
    print "Pixel Encoding: {0}".format(data.encoding)
    print "Is data big endian: {0}".format(data.is_bigendian)
    print "Image height: {0}".format(data.step)

def image_viewer():
    rospy.init_node('image_viewer', anonymous=True)
    rospy.Subscriber('camera/rgb/image_raw', Image, callback)

    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()

if __name__ == '__main__':
    image_viewer()