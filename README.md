# RobotCar

The aim is to construct a 4W robotic car with a Raspberry pi 4 B as a microcontroller, construct a Server-Client architecture and remotly control the car from my laptop first, and a Web application (and mobile application) later. 

## Server part
On the server part, i.e. on the raspberry pi, we installed Ubuntu Mate 20.04 with ROS Noetic.

- [X] drivers_pkg that contains:
   - [x] The PCA9685 python module in order to comunicate with the servo motors and the 2 DoF camera servos.
   - [x] Motor module that implements a Motor class for comunicating with the motor.
   - [x] Servo module that implements a Servo class for comunicating with the camera servos.
   - [ ] Ultrasonic module in order to get the data from the sonar sensor
   
- [X] robotic_car_pkg that contains:
   - [x] Motor Listener node that receives commands of type String on the /command topic in order to move the car
   - [x] Camera servos node that receives commands of type Int32 on the /servoCamera topic in order to move the camera

## Client part
The client part will be represented by my personal laptop, that will connect to the server in order to communicate with the car.

- [X] robotic_car_pkg that contains
   - [x] teleop_motor_keyboard.py publisher in order to publish on the /command topic istructions of type String to move the car.

- [X] face_recognition_pkg that contains the face tracker node for face detection.
   - [ ] Link the face detection algorithm to camera servos control.

- [ ] Autonomous navigation pkg
  - [ ] Mapping
  - [ ] Estimation

## Application part

- [ ] Web page application 
- [ ] Mobile application
