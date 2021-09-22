#!/usr/bin/env python3
# license removed for brevity
import math
import random
import rospy
from controller_manager_msgs.srv import SwitchController
from sensor_msgs.msg import JointState
from std_msgs.msg import Float64
from vision_based_manipulation.srv import ctrl_srv_command, ctrl_srv_commandResponse

pub_q1_pos = rospy.Publisher('/vbmbot/joint1_position_controller/command', Float64, queue_size=10)
pub_q2_pos = rospy.Publisher('/vbmbot/joint2_position_controller/command', Float64, queue_size=10)
pub_q1_vel = rospy.Publisher('/vbmbot/joint1_velocity_controller/command', Float64, queue_size=10)
pub_q2_vel = rospy.Publisher('/vbmbot/joint2_velocity_controller/command', Float64, queue_size=10)
node_status = 0

def callback_init_pos(dt1):	
	global node_status
	q1_init_pos = dt1.position[0]
	q2_init_pos = dt1.position[1]    
	if (node_status == 2):
			q1_pos = 2.09
			q2_pos = 1.57 
			pub_q1_pos.publish(q1_pos)
			pub_q2_pos.publish(q2_pos)
			rospy.sleep(5)
			rospy.wait_for_service('/vbmbot/controller_manager/switch_controller')
			try:
				sc_service = rospy.ServiceProxy('/vbmbot/controller_manager/switch_controller', SwitchController)
				start_controllers = ['joint1_velocity_controller','joint2_velocity_controller']
				stop_controllers = ['joint1_position_controller','joint2_position_controller']
				strictness = 2
				start_asap = False
				timeout = 0.0
				res = sc_service(start_controllers,stop_controllers, strictness, start_asap,timeout)

			except rospy.ServiceException as e:
				print("Service Call Failed")
			
			rate = rospy.Rate(1)
			while not rospy.is_shutdown():
				q1_vel = random.uniform(-0.5, 0.5)
				q2_vel = random.uniform(-0.5, 0.5)
				pub_q1_vel.publish(q1_vel)
				pub_q2_vel.publish(q2_vel)
				rate.sleep()
		

def callback_command(dt2):
  global node_status
  command = dt2.input
  strRtn = "This node moves the arm with random velocity applied at the joints"
  if(node_status == 0 and command == 1):
	  node_status = 1
	  print('node_status = ', node_status)
	  print('[Controller Node] Node is ready to start')
  elif(node_status == 0 and command == 2):
	  print('[Controller Node] Start Command Received, Node not Ready - Please initialize node')  
  elif(node_status == 1 and command == 2):
	  node_status = 2
	  print("[Controller Node] Node has started")
  elif(node_status == 2 and command == 0):
	  node_status = 0
	  print("[Controller Node] Node has stopped running!")  
  else:
	  print('[Controller Node] Unrecognized Command - Please insert 0 to stop the node when the node is running or initialized, 1 to initialize the node, when the node is not running or 2 to start the node, when the node is initialized')

  return(strRtn)

if __name__ == '__main__':
	rospy.init_node('Controller_Node', anonymous=True)     
	sub_vel = rospy.Subscriber('/vbmbot/joint_states', JointState, callback_init_pos)
	srv_control_command = rospy.Service('control_pub_command', ctrl_srv_command, callback_command)  
	rospy.spin()
