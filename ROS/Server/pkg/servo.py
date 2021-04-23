#! /usr/bin/env python
import time
from drivers_pkg.drivers_subpkg.PCA9685 import PCA9685

class Servo:
	def __init__(self):
		# The servo is on adress 0x40
		self.PwmServo = PCA9685(0x40, debug=True)
		# The f for the PXM is at least 50 hz
		self.PwmServo.setPWMFreq(50)
		# Channels of the camera servos are 8 and 9
		# The pulse is set to 1.5 ms corresponding to 90deg (middle)
		self.PwmServo.setServoPulse(8, 1500)
		self.PwmServo.setServoPulse(9, 1500)
		self.speed = 0.09 # 0.09deg/us

	def setServoPwm(self, channel, angle, error=10):
		angle = int(angle)
		if channel == 0:
			self.PwmServo.setServoPulse(8, 2500 - int((angle + error)/self.speed))
		elif channel == 1:
			self.PwmServo.setServoPulse(8, 500 + int((angle + error)/self.speed))
