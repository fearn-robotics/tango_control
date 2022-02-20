#!/usr/bin/env python3

# Modified for use on Tango
# Contains relay safety switching for motors - this file must be opened for
# the robot to move.

# Tomos Fearn
# tof7@aber.ac.uk


import rospy
import time
from geometry_msgs.msg import Twist
from tango_msgs.msg import relays
import sys, select, os
from actionlib_msgs.msg import GoalID
from std_msgs.msg import String
from std_msgs.msg import Bool
if os.name == 'nt':
    import msvcrt
else:
    import tty, termios

def getKey():
    if os.name == 'nt':
      return msvcrt.getch()

    tty.setraw(sys.stdin.fileno())
    rlist, _, _ = select.select([sys.stdin], [], [], 0.1)
    if rlist:
        key = sys.stdin.read(1)
    else:
        key = ''

    termios.tcsetattr(sys.stdin, termios.TCSADRAIN, settings)
    return key

def opening_safety():
    print ("relays enabled - ENGAGED")
    lidar_msg = relays()
    #if (count < 2) :
    for i in range(0,5):
        lidar_msg.number = 5
        lidar_msg.state = 1
        safety_pub.publish(lidar_msg)
        rospy.sleep(0.5)
    #print("starting up")

def closing_safety():
    print ("relays disabled - DISENGAGED")
    lidar_msg = relays()
    #if (count < 2) :
    for i in range(0,5):
        lidar_msg.number = 5
        lidar_msg.state = 0
        safety_pub.publish(lidar_msg)
        rospy.sleep(0.5)
    #print("shutting down")
    

if __name__=="__main__":
    if os.name != 'nt':
        settings = termios.tcgetattr(sys.stdin)

    rospy.init_node('tango_slam_relay')
    time.sleep(1)

    safety_pub = rospy.Publisher("/tango_msgs/relays", relays, queue_size=100)
    opening_safety()
    try:
        while(1):
            key = getKey()
            if (key == '\x03'):
                break

    except:
        print (e)


    if os.name != 'nt':
        termios.tcsetattr(sys.stdin, termios.TCSADRAIN, settings)

    rospy.on_shutdown(closing_safety)

