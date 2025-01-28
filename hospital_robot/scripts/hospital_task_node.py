#!/usr/bin/env python
import rospy
from std_msgs.msg import String

class HospitalTaskNode:
    def __init__(self):
        rospy.init_node('hospital_task_node', anonymous=True)
        self.task_pub = rospy.Publisher('/hospital_task', String, queue_size=10)

    def perform_task(self, task):
        rospy.loginfo(f"Performing task: {task}")
        self.task_pub.publish(task)

if __name__ == '__main__':
    try:
        node = HospitalTaskNode()
        node.perform_task("Deliver medication to Room 101")
    except rospy.ROSInterruptException:
        pass