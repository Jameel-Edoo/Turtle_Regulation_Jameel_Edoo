#!/usr/bin/env python3

import rospy
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose
from std_msgs.msg import Bool
import math

def pose_callback(data):
    global Kpl, distance_tolerance, waypoint, cmd_vel_pub, is_moving_pub

    # Calculate Euclidean distance
    distance = math.sqrt((waypoint[1] - data.y) ** 2 + (waypoint[0] - data.x) ** 2)

    # Calculate linear error
    el = distance - distance_tolerance

    # Check if linear error is above distance tolerance
    if el >= distance_tolerance:
        # Calculate angular control (fixed Kp value)
        Kp = 1.0  # You can set this value as needed
        u = Kp * math.atan2(waypoint[1] - data.y, waypoint[0] - data.x)

        # Calculate linear control (dynamic Kpl)
        v = Kpl * el

        # Create and publish Twist message with both angular and linear velocities
        cmd_vel_msg = Twist()
        cmd_vel_msg.angular.z = u
        cmd_vel_msg.linear.x = v
        cmd_vel_pub.publish(cmd_vel_msg)

        # Publish True on 'is_moving' topic
        is_moving_pub.publish(True)
    else:
        # Stop the turtle by sending zero velocity
        cmd_vel_msg = Twist()
        cmd_vel_pub.publish(cmd_vel_msg)
        is_moving_pub.publish(False)

if __name__ == "__main__":
    rospy.init_node("set_way_point")

    # Load parameters
    Kpl = rospy.get_param("~Kpl", 1.0)  # Proportional gain for linear control (dynamic)
    distance_tolerance = 0.3  # Fixed distance tolerance
    waypoint = (7, 7)  # Define your waypoint coordinates

    # Create subscribers and publishers
    rospy.Subscriber("/turtle1/pose", Pose, pose_callback)
    cmd_vel_pub = rospy.Publisher("/turtle1/cmd_vel", Twist, queue_size=10)
    is_moving_pub = rospy.Publisher("/is_moving", Bool, queue_size=10)

    # Main control loop
    rospy.spin()


