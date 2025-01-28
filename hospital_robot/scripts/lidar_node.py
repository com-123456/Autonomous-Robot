#!/usr/bin/env python
import rospy
from sensor_msgs.msg import LaserScan

class LidarNode:
    def __init__(self):
        rospy.init_node('lidar_node', anonymous=True)
        self.lidar_sub = rospy.Subscriber('/scan', LaserScan, self.scan_callback)

    def scan_callback(self, data):
        # Process LiDAR data for obstacle detection
        rospy.loginfo("LiDAR data received")

if __name__ == '__main__':
    try:
        node = LidarNode()
        rospy.spin()
    except rospy.ROSInterruptException:
        pass