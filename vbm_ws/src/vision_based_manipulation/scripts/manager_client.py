#!/usr/bin/env python3

import rospy
import roslaunch
import numpy as np
import math
import time
import sys
import os
from gazebo_msgs.msg import *
from gazebo_msgs.srv import *
from vision_based_manipulation.srv import ctrl_srv_command, ctrl_srv_commandResponse

   	
def controller_client(b):
     rospy.wait_for_service('control_pub_command')
     try:
         control_pub_command = rospy.ServiceProxy('control_pub_command', ctrl_srv_command)
         resp2 = control_pub_command(b)
         return resp2.output
     except rospy.ServiceException as e:
         print("Control Service call failed")

def usage():
     return "%s [a]"%sys.argv[0]
 
if __name__ == "__main__":
  rospy.sleep(1)
  controller_client(1)
  rospy.sleep(5)
  controller_client(2)
  rospy.sleep(5)
  controller_client(0)

