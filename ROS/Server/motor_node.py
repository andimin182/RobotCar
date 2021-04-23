#!/usr/bin/env python
import time
from drivers_pkg.drivers_subpkg.PCA9685 import PCA9685
from drivers_pkg.motor import Motor
import rospy
from std_msgs.msg import String
       
PWM = Motor()             
def forward(): 
     PWM.setMotorModel(-2000,-2000,-2000,-2000)       #Forward
     
def back(): 
     PWM.setMotorModel(2000,2000,2000,2000)   #Back
     
def left(): 
     PWM.setMotorModel(500,500,-2000,-2000)       #Left 
     
def right(): 
     PWM.setMotorModel(-2000,-2000,500,500)       #Right    
   
def stop(): 
     PWM.setMotorModel(0,0,0,0)                   #Stop
    
def destroy():
     PWM.setMotorModel(0,0,0,0)     
    
def CommandCallback(msg):
    command = msg.data
    if command == 'forward':
        print('Moving forward')
        forward()
        
    elif command == 'backward':
        print('Moving backwards')
        back()
    elif command == 'left':
        print('Turning left')
        left()         
    elif command == 'right':
        print('Turning right')
        right()   
    elif command == 'stop':
        print('Stop moving')
        stop()    
    else:
        print('Unknown command, stop moving')
        stop()  
           
if __name__=='__main__':
    try:
        rospy.init_node('driver')
        rospy.loginfo('Driver node initialized')
        subscriber = rospy.Subscriber('command', String, CommandCallback)
        
        rospy.spin()
    except KeyboardInterrupt:  # When 'Ctrl+C' is pressed, the child program destroy() will be  executed.
        destroy()
