#! /usr/bin/env python
import time
from drivers_pkg.drivers_subpkg.PCA9685 import PCA9685
from drivers_pkg.servo import Servo
import rospy
from std_msgs.msg import Int32

pwm = Servo()

def setAngle(angle):
	pwm.setServoPwm(0, angle)

def CommandCallback(msg):
	angle = msg.data
	rospy.loginfo(f'Turning the camera at: {angle} degrees')
	setAngle(angle)

if __name__ =='__main__':
	try:
		rospy.init_node('ServoCameraNode')
		rospy.loginfo('Initializing servo camera node')
		
		subscriber = rospy.Subscriber('servoCamera', Int32, CommandCallback)

		rospy.spin()
	except KeyboardInterupt:
		print('Closing servo camera node')
		destroy()
