from mindstorms import MSHub, Motor, MotorPair, ColorSensor, DistanceSensor, App
from mindstorms.control import wait_for_seconds, wait_until, Timer
from mindstorms.operator import greater_than, greater_than_or_equal_to, less_than, less_than_or_equal_to, equal_to, not_equal_to
import math, sys

def main():
    # goal is to be able to write code like this:
    robot = Kraken()
    robot.reset_angle()
    attachment_motor = Motor('D')

    #top_left(robot)
    #shipping_two(robot,attachment_motor)
    #collection_robot(robot)
    #sonar(robot, attachment_motor)

# Luke
# Still needs work.
# To do: collect everything and come home.
def collection_robot(robot):
    robot.drive_forward(38)

# Rutledge.
# Still needs work.
def sonar(robot, attachment_motor):
    robot.drive_backward(26)
    robot.turn_left(40)
    robot.drive_backward(40)
    robot.turn_right(40)
    attachment_motor.run_for_degrees(360,-50)

# works sometimes
# Cora
def shipping_two(robot,attachment_motor):
    robot.drive_backward(6)
    robot.turn_left(40)
    robot.drive_backward(4, speed =20) 
    attachment_motor.start(60)
    wait_for_seconds(1.5)
    robot.drive_forward(18, speed=10)

# works 50% of the time.
# Raden and Phoebe
def top_left(robot):
    robot.drive_forward(35)
    robot.turn_right(30)
    robot.drive_forward(32)
    robot.turn_left(120)
    robot.drive_forward(14)
    robot.drive_backward(4)
    robot.turn_right(45)
    robot.drive_forward(22)
    robot.drive_backward(6)
    robot.turn_right(45)
    robot.drive_forward(22)
    robot.drive_backward(50)
    robot.turn_right(45)
    robot.drive_backward(50)

SPEED = 90

class Kraken:
    def __init__(self):
        self.wheel_diameter = 5.5 # cm
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
    def drive_forward(self, distance, speed = SPEED):
        # convert distance (centimeters) to degrees
        distance_in_degrees = distance * (360.0 / (self.wheel_diameter * math.pi))
        start_position = self.right_motor.get_degrees_counted()
        goal_position = start_position + distance_in_degrees
        small_goal = goal_position - 7 * (360.0 / (self.wheel_diameter * math.pi))
        while self.right_motor.get_degrees_counted() < small_goal:
            self .motor_pair.start(self.correction(),speed)
        while self.right_motor.get_degrees_counted() < goal_position:
            self.motor_pair.start(self.correction(),10)
        self.motor_pair.stop()

    def correction(self):
        correction = self.angle_goal - self.motion_sensor.get_yaw_angle()
        correction *= 10
        if correction < -50:
            correction = -50
        if correction > 50:
            correction = 50
        return correction


    def drive_backward(self, distance, speed = SPEED):
        # convert distance (centimeters) to degrees
        distance_in_degrees = distance * (360.0 / (self.wheel_diameter * math.pi))
        start_position = self.right_motor.get_degrees_counted()
        goal_position = start_position - distance_in_degrees
        small_goal = goal_position - 7 * (360.0 / (self.wheel_diameter * math.pi))
        while self.right_motor.get_degrees_counted() > small_goal:
            self .motor_pair.start(-self.correction(),-speed)
        while self.right_motor.get_degrees_counted() > goal_position:
            self.motor_pair.start(-self.correction(),-10)
        self.motor_pair.stop()


    def turn_left(self, degrees, speed = 50):
        if speed>50:
            speed = 50
        self.angle_goal = self.angle_goal - degrees
        small_goal = self.angle_goal + 20
        self.motor_pair.start_tank(-speed, speed)
        while self.motion_sensor.get_yaw_angle()>small_goal:
            # wait
            True
        self.motor_pair.start_tank(-10, 10)
        while self.motion_sensor.get_yaw_angle()>self.angle_goal:
            True
        self.motor_pair.stop()

    def turn_right(self, degrees, speed = 50):
        if speed>50:
            speed = 50
        self.angle_goal = self.angle_goal + degrees
        small_goal = self.angle_goal - 20
        self.motor_pair.start_tank(speed, -speed)
        while self.motion_sensor.get_yaw_angle()<small_goal:
            # wait
            True
        self.motor_pair.start_tank(10, -10)
        while self.motion_sensor.get_yaw_angle()<self.angle_goal:
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