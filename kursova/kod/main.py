#!/usr/bin/env python3

# Import the necessary libraries
import time
import math
from ev3dev2.motor import *
from ev3dev2.sound import Sound
from ev3dev2.button import Button
from ev3dev2.sensor import *
from ev3dev2.sensor.lego import *
from ev3dev2.sensor.virtual import *

# Create the sensors and motors objects
motorA = LargeMotor(OUTPUT_A)
motorB = LargeMotor(OUTPUT_B)
left_motor = motorA
right_motor = motorB
tank_drive = MoveTank(OUTPUT_A, OUTPUT_B)
steering_drive = MoveSteering(OUTPUT_A, OUTPUT_B)

spkr = Sound()
btn = Button()
radio = Radio()
obtr = ObjectTracker()

color_sensor_in1 = ColorSensor(INPUT_1)
color_sensor_in2 = ColorSensor(INPUT_2)
color_sensor_in3 = ColorSensor(INPUT_3)
ultrasonic_sensor_in4 = UltrasonicSensor(INPUT_4)
gyro_sensor_in5 = GyroSensor(INPUT_5)
gps_sensor_in6 = GPSSensor(INPUT_6)
ultrasonic_sensor_in7 = UltrasonicSensor(INPUT_7)
ultrasonic_sensor_in8 = UltrasonicSensor(INPUT_8)

motorC = LargeMotor(OUTPUT_C) # Arm
motorD = LargeMotor(OUTPUT_D) # Swivel
motorE = LargeMotor(OUTPUT_E) # Magnet

# Here is where your code starts

Start_Time = None
Align = None
Correction = None
Color = None

# Describe this function...
def Right():
    global Start_Time, Align, Correction, Color
    print('Turn right')
    while gyro_sensor_in5.angle < 85:
        tank_drive.on(10, (-10))
    tank_drive.off(brake=True)
    time.sleep(0.2)
    while not gyro_sensor_in5.angle == 90:
        if gyro_sensor_in5.angle < 90:
            tank_drive.on(1, (-1))
        elif gyro_sensor_in5.angle > 90:
            tank_drive.on((-1), 1)
    tank_drive.off(brake=True)
    gyro_sensor_in5.reset()

# Describe this function...
def Left():
    global Start_Time, Align, Correction, Color
    print('Turn left')
    while gyro_sensor_in5.angle > -85:
        tank_drive.on((-10), 10)
    tank_drive.off(brake=True)
    time.sleep(0.2)
    if gyro_sensor_in5.angle != 90:
        while not gyro_sensor_in5.angle == -90:
            if gyro_sensor_in5.angle > -90:
                tank_drive.on((-1), 1)
            elif gyro_sensor_in5.angle < -90:
                tank_drive.on(1, (-1))
    tank_drive.off(brake=True)
    gyro_sensor_in5.reset()

# Describe this function...
def Turn_180():
    global Start_Time, Align, Correction, Color
    print('Turn 180')
    while gyro_sensor_in5.angle < 180:
        tank_drive.on(10, (-10))
    tank_drive.off(brake=True)
    time.sleep(0.2)
    while not gyro_sensor_in5.angle == 180:
        if gyro_sensor_in5.angle < 180:
            tank_drive.on(1, (-1))
        elif gyro_sensor_in5.angle > 180:
            tank_drive.on((-1), 1)
    tank_drive.off(brake=True)
    gyro_sensor_in5.reset()

# Describe this function...
def Forward():
    global Start_Time, Align, Correction, Color
    Time_Function()
    while ultrasonic_sensor_in4.distance_centimeters > 14:
        if color_sensor_in3.color_name == 'Blue':
            motorE.on(20)
            time.sleep(1)
            motorC.on_to_position(10, 90)
        tank_drive.on(20, 20)
        if ultrasonic_sensor_in7.distance_centimeters > 40 and 3 + Start_Time < time.time():
            tank_drive.on_for_seconds(15, 15, 1)
            break
    tank_drive.off(brake=True)

# Describe this function...
def Time_Function():
    global Start_Time, Align, Correction, Color
    Start_Time = time.time()
    print('Time')


Time_Function()
while True:
    Color = color_sensor_in3.color_name
    print(Color)
    Forward()
    if ultrasonic_sensor_in7.distance_centimeters > 40:
        Right()
    elif ultrasonic_sensor_in8.distance_centimeters > 40:
        Left()
    elif ultrasonic_sensor_in7.distance_centimeters < 23 and ultrasonic_sensor_in8.distance_centimeters < 23 and ultrasonic_sensor_in4.distance_centimeters < 23:
        Turn_180()
    elif color_sensor_in1.color_name == 'Blue' and color_sensor_in2.color_name == 'Blue':
        motorC.on_to_position(10, (-90))
        time.sleep(1)
        motorE.off(brake=True)
    else:
        print('Error')
