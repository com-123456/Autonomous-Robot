#!/usr/bin/env python
import rospy
from move_base_msgs.msg import MoveBaseAction, MoveBaseGoal
import actionlib

class NavigationNode:
    def __init__(self):
        rospy.init_node('navigation_node', anonymous=True)
        self.client = actionlib.SimpleActionClient('move_base', MoveBaseAction)
        self.client.wait_for_server()

    def move_to_goal(self, x, y, w):
        goal = MoveBaseGoal()
        goal.target_pose.header.frame_id = "map"
        goal.target_pose.pose.position.x = x
        goal.target_pose.pose.position.y = y
        goal.target_pose.pose.orientation.w = w
        self.client.send_goal(goal)
        self.client.wait_for_result()

if __name__ == '__main__':
    try:
        node = NavigationNode()
        node.move_to_goal(2.0, 3.0, 1.0)  # Example goal
    except rospy.ROSInterruptException:
        pass