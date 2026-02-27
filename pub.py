#!/usr/bin/env python3
import rospy
from std_msgs.msg import String
rospy.init_node('Simple_publisher')
pub=rospy.Publisher('/robot_msg', String, queue_size=10)
rate=rospy.Rate(1)
while not rospy.is_shutdown():
	msg="Hello from Robot!"
	pub.publish(msg)
	rospy.loginfo("Published: " + msg)
	rate.sleep() 
