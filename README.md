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
-- server node waits for manager's numeric input, to publish joint positions and move from home position to target, and then switches controller to publish random joint velocities
