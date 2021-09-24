# Vision_Based_Manipulation
Skeleton Code for VB Manip class

vbmbot.xacro - Robot description file for 2 link planar manipulator 
vbmbot.gazebo - References for xacro
materials.xacro - common gazebo material descriptions

Nodes - 
vbmbot_joint_controller.py - launches with vb_joint_vel_and_pos_pub.launch
vbmbot_joint_controller_service.py and manager_client.py - launches with vb_manager.launch
 

Run this project by launching the following - 
`roslaunch vision_based_manipulation vb_joint_vel_and_pos_pub.launch`
-- Node publishes joint position first and switches controller to publish joint velocity

`roslaunch vision_based_manipulation vb_manager.launch`
-- server node has the controller. Manager nodes send a numeric input that asks the controller to wait (input 1), to start (input 2) or to stop (input 0). The arm position is in the home position. The server node receives the start command from manager, and the position controller changes the joint position to a target position. After that the switchcontroller service is called in the server node that switches the controller from position to velcity and the velocity command are published to randonly move the arm 
