# Turtle_Regulation_Jameel_Edoo
ROBO TP Note Regulation 2023

**Installation Guide:

1. Clone repository within the src folder of a catkin workspace.

2. Source the catkin workspace directory within .bashsrc file.

3. Run the catkin build command to build the catkin workspace.

4. Open two terminals; in terminal 1, run the command:
       roslaunch turtle_regulation_jameel_edoo set_way_point.launch Kp:=2
   to initiate the node. The Kp value must be determined within this command as well.

5. In terminal 2, run the command:
       rosrun turtlesim turtlesim_node
   to observe the node.



**The Kp value determines the speed at which the turtle will adjust its course (correct the error) towards the predetermined waypoint with coordinates (7,7).

Examples of Kp values and their observation:

1. A low Kp value of 0.1; turtle will adjust course slowly.

2. An average  Kp value of 2; turtle will adjust course in a smooth way.

3. A high Kp value of 10; turtle will adjust course very quickly.

