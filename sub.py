#!/usr/bin/env python3
import rospy
from std_msgs.msg import String
def callback(msg):
	rospy.loginfo("Recieved: " + msg.data)
rospy.init_node('Simple_subscriber')
rospy.Subscriber('/robot_msg', String, callback)
rospy.spin()
