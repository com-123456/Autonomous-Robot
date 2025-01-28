#!/usr/bin/env python
import rospy
from geometry_msgs.msg import Twist

class ControlNode:
    def __init__(self):
        rospy.init_node('control_node', anonymous=True)
        self.cmd_vel_pub = rospy.Publisher('/cmd_vel', Twist, queue_size=10)
        self.rate = rospy.Rate(10)  # 10Hz

    def move_robot(self, linear_x, angular_z):
        twist = Twist()
        twist.linear.x = linear_x
        twist.angular.z = angular_z
        self.cmd_vel_pub.publish(twist)
        self.rate.sleep()

if __name__ == '__main__':
    try:
        node = ControlNode()
        node.move_robot(0.5, 0.2)  # Example movement
    except rospy.ROSInterruptException:
        pass