from mindstorms import MSHub, Motor, MotorPair, ColorSensor, DistanceSensor, App
from mindstorms.control import wait_for_seconds, wait_until, Timer
from mindstorms.operator import greater_than, greater_than_or_equal_to, less_than, less_than_or_equal_to, equal_to, not_equal_to
import math, sys
self.hub = MSHub()

def main():
    # goal is to be able to write code like this:
    robot = Kraken()
    robot.reset_angle()
 
    # test program: trace letter H
    robot.drive_forward(20)
    robot.drive_backward(10)
    robot.turn_right(90)
    robot.drive_forward(10)
    robot.turn_left(90)
    robot.drive_forward(10)
    robot.drive_backward(20)


class Kraken:
    def __init__(self):
        self.wheel_diameter = 8.76 # cm
        self.left_motor = Motor('A')
        self.right_motor = Motor('B')
        self.motor_pair = MotorPair('A', 'B')
        self.hub = MSHub()
        self.motion_sensor = hub.motion_sensor

    # drive_forward tells the robot to drive in a
    # straight line "distance" centimeters forwards.
    def drive_forward(self, distance):
        # convert distance (centimeters) to degrees
        distance_in_degrees = distance * (360.0 / (self.wheel_diameter * math.pi)

        start_position = self.right_motor.get_degrees_counted()
        goal_position = start_position + distance_in_degrees        
        while self.right_motor.get_degrees_counted() < goal_position:
            correction = self.angle_goal - self.motion_sensor.get_yaw.angle()
            self .motor_pair.start(correction*30)
        self.motor_pair.stop()
        
    def turn_left(self, degrees):

    # reset_angle tells the robot that it is currently facing
    # the right direction. Call this at the beginning of each
    # program and after the robot squares itself up on an
    # object.
    def reset_angle(self):
        self.angle_goal = 0
        hub.motion_sensor.reset_yaw_angle()
     
main()
sys.exit()