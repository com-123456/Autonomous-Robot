#!/usr/bin/env python
import rospy
from sensor_msgs.msg import Imu, Range

class SensorIntegrationNode:
    def __init__(self):
        rospy.init_node('sensor_integration_node', anonymous=True)
        self.imu_sub = rospy.Subscriber('/imu/data', Imu, self.imu_callback)
        self.ultrasonic_sub = rospy.Subscriber('/ultrasonic', Range, self.ultrasonic_callback)

    def imu_callback(self, data):
        # Process IMU data
        rospy.loginfo("IMU data received")

    def ultrasonic_callback(self, data):
        # Process ultrasonic data
        rospy.loginfo("Ultrasonic data received")

if __name__ == '__main__':
    try:
        node = SensorIntegrationNode()
        rospy.spin()
    except rospy.ROSInterruptException:
        pass