#!/usr/bin/env python3

import rospy
import math
from turtlesim.msg import Pose  # Import the Pose message type
from geometry_msgs.msg import Twist

# Global variable to store the waypoint
waypoint = None

# Callback function to update waypoint
def pose_callback(data):
    global waypoint
    # Update the waypoint variable with the desired coordinates (7,7)
    waypoint = (7, 7)
    rospy.loginfo("Waypoint updated to (%.2f, %.2f)", waypoint[0], waypoint[1])

if __name__ == "__main__":
    # Initialize the ROS node
    rospy.init_node("set_way_point")

    # Subscribe to the "pose" topic
    rospy.Subscriber("pose", Pose, pose_callback)

    # Create a Twist message for cmd_vel
    cmd_vel_msg = Twist()

    # Define the proportional constant Kp as a private parameter (you can set it in the launch file)
    Kp = rospy.get_param("~Kp", 1.0)

    # Create a Publisher for cmd_vel
    cmd_vel_pub = rospy.Publisher("cmd_vel", Twist, queue_size=10)

    # Keep the node running
    rate = rospy.Rate(10)  # 10 Hz
    while not rospy.is_shutdown():
        if waypoint is not None:  # Check if waypoint is set
            # Calculate the desired angle (in radians) using atan2
            desired_angle = math.atan2(waypoint[1] - data.y, waypoint[0] - data.x)

            # Calculate the error e
            e = math.atan(math.tan((desired_angle - data.theta) / 2))

            # Calculate the control command u
            u = Kp * e

            # Set angular velocity in cmd_vel
            cmd_vel_msg.angular.z = u

            # Publish cmd_vel
            cmd_vel_pub.publish(cmd_vel_msg)

        rate.sleep()  # Maintain the loop rate

