from mindstorms import MSHub, Motor, MotorPair, ColorSensor, DistanceSensor, App
from mindstorms.control import wait_for_seconds, wait_until, Timer
from mindstorms.operator import greater_than, greater_than_or_equal_to, less_than, less_than_or_equal_to, equal_to, not_equal_to
import math, sys

PROGRAM_NUMBER = 4

def main():
    # goal is to be able to write code like this:
    robot = Kraken()
    robot.reset_angle()
    attachment_motor = Motor('D')
    attachment_motor2 = Motor('F')

    if PROGRAM_NUMBER == 1:
        pickaxe(robot, attachment_motor2)
    elif PROGRAM_NUMBER == 2:
        whale_feeder(robot, attachment_motor)
    elif PROGRAM_NUMBER == 3:
        traverse_map(robot, attachment_motor)
    elif PROGRAM_NUMBER == 4:
        top_left(robot, attachment_motor2)
    elif PROGRAM_NUMBER == 5:
        boat(robot)
    elif PROGRAM_NUMBER == 6:
        shark_squid_express(robot, attachment_motor)

def pickaxe(robot, attachment_motor2): 
    robot.drive_forward(43)
    attachment_motor2.run_for_degrees(70)
    wait_for_seconds(1)
    robot.turn_left(30)
    robot.drive_backward(10)
    robot.turn_left(30)
    robot.drive_forward(10)
    robot.drive_backward(5)
    robot.turn_left(10)
    robot.drive_backward(5)
    robot.turn_left(15)
    robot.drive_backward(25)
    robot.show_state()
    robot.turn_left(45)
    
# Rutledge.
# Still needs work.
def sonar(robot, attachment_motor):
    robot.drive_backward(26)
    robot.turn_left(40)
    robot.drive_backward(40)
    robot.turn_right(40)
    attachment_motor.run_for_degrees(360,-50)
    robot.turn_left(40)
    robot.drive_forward(56)

# works sometimes
# Cora, Rutledge
def shipping_two(robot,attachment_motor):
    robot.drive_backward(45)
    robot.turn_right(45)
    robot.drive_backward(2)
    robot.turn_left(20)
    robot.drive_backward(2)
    attachment_motor.start(-10)
    robot.turn_right(45, speed = 10)
    attachment_motor.stop()
    attachment_motor.start(10)
    robot.drive_forward(20, speed = 10)
    attachment_motor.stop()

def traverse_map(robot, attachment_motor):
    robot.drive_forward(25)
    robot.turn_left(33)
    robot.drive_forward(56)
    attachment_motor.run_for_degrees(900, 100)
    robot.drive_backward(3)
    robot.turn_left(57)
    robot.drive_forward(58.2)
    robot.turn_right(15)
    robot.drive_forward(30)
    robot.turn_left(47)
    robot.drive_forward(30)
    robot.turn_left(40)
    robot.drive_forward(55)
    # robot.turn_left(25)
    # robot.drive_forward(10)
    # robot.turn_left(20)
    # robot.drive_forward(55)
    # robot.turn_left(10)
    # robot.drive_forward(20)
    # robot.turn_left(15)
    # robot.drive_forward(15)
    # robot.turn_left(30)
    # robot.drive_forward(70)

# works 100% of the time.
# Raden and Phoebe
def top_left(robot, attachment_motor2):
    robot.drive_forward(23)
    robot.turn_right(25)
    robot.drive_forward(45)
    robot.turn_left(115)
    # get scuba diver :-)
    attachment_motor2.run_for_degrees(86,50)
    robot.drive_forward(8)
    attachment_motor2.run_for_degrees(-60,100)
    # flip coral buds up
    robot.drive_backward(20)
    #raise the mast
    robot.drive_forward(36)
    robot.turn_right(45)
    robot.drive_forward(15)
    #hit the sherk
    robot.drive_backward(6)
    robot.turn_right(45)
    robot.drive_forward(22)
    #cora reef
    robot.drive_backward(50)
    robot.turn_right(45)
    robot.drive_backward(50)

# works 80% of the time
# raden progamed and caolan builded
def raise_the_mast(robot):
    robot.drive_forward(30)
    robot.turn_right(45)
    robot.drive_forward(24)
    robot.turn_right(43)
    motor_pair = MotorPair('A', 'B')
    motor_pair.move(21, 'cm', 0, 40)
    robot.drive_backward(20,speed = 35)
    robot.turn_left(43)
    robot.drive_backward(24)
    robot.turn_left(45)
    robot.drive_backward(30)


def boat(robot):
    robot.drive_forward(12,speed = 20)
    wait_for_seconds(1)
    robot.drive_backward(20)

def whale_feeder(robot, attachment_motor):
    robot.drive_forward(40)
    robot.turn_left(45)
    robot.drive_forward(22)
    robot.turn_right(90)
    robot.drive_forward(36,speed=70)
    # this is where it hits the whale
    #attachment_motor.run_for_seconds(2, 70)
    #added shipping lanes to whale feeder
    robot.drive_backward(11)
    robot.turn_left(90)
    robot.drive_forward(7)
    # lined up with shipping lanes
    attachment_motor.run_for_degrees(180, 50)
    robot.drive_backward(1, speed = 15)
    attachment_motor.run_for_degrees(-100, 100)
    # robot.drive_backward(1, speed = 15)
    # attachment_motor.start(80)
    # robot.turn_left(5)
    # robot.turn_right(5)
    # robot.turn_left(5)
    # attachment_motor.stop()
    robot.drive_forward(6)
    robot.turn_right(45)
    robot.drive_backward(40)
    robot.turn_left(45)
    robot.drive_backward(19)


def tsunami(robot):
    robot.drive_forward(7, speed = 20)
    robot.drive_backward(10)

def shark_squid_express(robot, attachment_motor):
    robot.drive_forward(25)
    robot.turn_left(20)
    robot.drive_forward(67)
    robot.turn_left(40)
    robot.drive_forward(13)
    attachment_motor.run_for_degrees(-360, 100)


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
