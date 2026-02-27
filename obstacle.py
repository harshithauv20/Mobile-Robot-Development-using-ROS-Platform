#!/usr/bin/env python3

import rospy
from sensor_msgs.msg import LaserScan
from geometry_msgs.msg import Twist
import math

OBSTACLE_DIST=0.5
FORWARD_SPEED=0.3
TURN_SPEED=0.5

pub None

def safe_min(ranges, start, end):
    values=[r for r in ranges[start:end]
    	if not math.isinf(r) and not math.isnan(r)]
    return min(values) if values else 10.0
    
def callback(msg):
    front_L=safe_min(msg.ranges, 0, 130)
    front_R=safe_min(msg.ranges, 721, 850)
    fleft=safe_min(msg.ranges, 131, 230)
    fright=safe_min(msg.ranges, 621, 720)
    
    front=min(front_L ,front_R)
    
    twist=Twist()
    
    if front>OBSTACLE_DIST:
    	twist.linear.x=FORWARD_SPEED
    	twist.angular.z=0.0
    	rospy.loginfo("MOVING FORWARD | Front:%.2f m" % front)
    	
    elif fleft>fright:
    	twist.linear.x=0.0
    	twist.angular.z=TURN_SPEED
    	rospy.loginfo("TURNING LEFT | Front:%.2f m | Fleft: %.2f m | Fright: %.2f m" % (front, fleft, fright))
    	
    else:
   	twist.linear.x=0.0
    	twist.angular.z=TURN_SPEED
    	rospy.loginfo("TURNING LEFT | Front:%.2f m | Fleft: %.2f m | Fright: %.2f m" % (front, fleft, fright))
    	
    pub.publish(twist)
    
def main():
	global pub
	rospy.init_node('obstacle')
	pub=rospy.Publisher('/cmd_vel', Twist, queue_size=10)
	rospy.Subscriber('/scan', LaserScan, callback)
	rospy.loginfo("Obstacle running - moving forward by default")
	rospy.spin()
    	
if__name__ = '__main__':
	main()
    	
    
    	
