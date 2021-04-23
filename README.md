# RobotCar

The aim is to construct a 4W robotic car with a Raspberry pi 4 B as a microcontroller, construct a Server-Client architecture and remotly control the car from my laptop first, and a Web application (and mobile application) later. 

## Server part
On the server part, i.e. on the raspberry pi, we installed Ubuntu Mate 20.04 with ROS Noetic.

### DONE
- The PCA9685 python module in order to comunicate with the servo motors and the 2 DoF camera servos.
- Motor module that implements a Motor class for comunicating with the motor.
- Servo module that implements a Servo class for comunicating with the camera servos.
- Listener node that receives commands of type String on the /command topic

## Client part
The client part will be represented by my personal laptop, that will connect to the server in order to communicate with the car.

### DONE
- Teleop node publisher in order to publish on the /command topic istructions of type String to move the car.
