from mindstorms import MSHub, Motor, MotorPair, ColorSensor, DistanceSensor, App
from mindstorms.control import wait_for_seconds, wait_until, Timer
from mindstorms.operator import greater_than, greater_than_or_equal_to, less_than, less_than_or_equal_to, equal_to, not_equal_to
import math, sys

def main():
    # goal is to be able to write code like this:
    robot = Kraken()
    robot.reset_angle()

    # robot.turn_left(90)
    # wait_for_seconds(1)
    # robot.show_state()
    # return

    # test program: trace letter H
    robot.show_state()
    robot.drive_forward(80)
    robot.show_state()
    robot.drive_backward(40)
    robot.turn_right(90)
    robot.drive_forward(40)
    robot.turn_left(90)
    robot.drive_forward(40)
    robot.drive_backward(80)
    wait_for_seconds(1)
    robot.show_state()

SPEED = 80

class Kraken:
    def __init__(self):
        self.wheel_diameter = 8.7 # cm
        left_motor_port = 'A'
        right_motor_port = 'B'
        self.left_motor = Motor(left_motor_port)
        self.right_motor = Motor(right_motor_port)
        self.motor_pair = MotorPair(left_motor_port, right_motor_port)
        self.hub = MSHub()
        self.motion_sensor = self.hub.motion_sensor

    def show_state(self):
        print("current angle: {} / angle goal: {}".format(self.motion_sensor.get_yaw_angle(), self.angle_goal))

    # drive_forward tells the robot to drive in a
    # straight line "distance" centimeters forwards.
    def drive_forward(self, distance):
        # convert distance (centimeters) to degrees
        distance_in_degrees = distance * (360.0 / (self.wheel_diameter * math.pi))
        start_position = self.right_motor.get_degrees_counted()
        goal_position = start_position + distance_in_degrees        
        while self.right_motor.get_degrees_counted() < goal_position:
            correction = self.angle_goal - self.motion_sensor.get_yaw_angle()
            self .motor_pair.start(correction*10,SPEED)
        self.motor_pair.stop()

    def drive_backward(self, distance):
        # convert distance (centimeters) to degrees
        distance_in_degrees = distance * (360.0 / (self.wheel_diameter * math.pi))
        start_position = self.right_motor.get_degrees_counted()
        goal_position = start_position - distance_in_degrees
        while self.right_motor.get_degrees_counted() > goal_position:
            correction = self.angle_goal - self.motion_sensor.get_yaw_angle()
            self .motor_pair.start(-correction*10,-SPEED)
        self.motor_pair.stop()

    
    def turn_left(self, degrees):
        self.angle_goal = self.angle_goal - degrees
        turn_goal = self.angle_goal + 20
        self.motor_pair.start_tank(-50, 50)
        while self.motion_sensor.get_yaw_angle()>turn_goal:
            # wait
            True
        self.motor_pair.stop()

    def turn_right(self, degrees):
        self.angle_goal = self.angle_goal + degrees
        turn_goal = self.angle_goal - 20
        self.motor_pair.start_tank(50, -50)
        while self.motion_sensor.get_yaw_angle()<turn_goal:
            # wait
            True
        self.motor_pair.stop()


    # reset_angle tells the robot that it is currently facing
    # the right direction. Call this at the beginning of each
    # program and after the robot squares itself up on an
    # object.
    def reset_angle(self):
        self.angle_goal = 0
        self.hub.motion_sensor.reset_yaw_angle()
     
main()
sys.exit()