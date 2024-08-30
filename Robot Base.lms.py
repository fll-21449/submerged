from mindstorms import MSHub, Motor, MotorPair, ColorSensor, DistanceSensor, App
from mindstorms.control import wait_for_seconds, wait_until, Timer
from mindstorms.operator import greater_than, greater_than_or_equal_to, less_than, less_than_or_equal_to, equal_to, not_equal_to
import math
self.hub = MSHub()

def main():
    # goal is to be able to write code like this:
    robot = Kraken()
    robot.drive_forward(20)
    robot.turn_left(75)
    robot.drive_backward(10.5)

class Kraken:
    def __init__(self):
        self.left_motor = Motor('A')
        self.right_motor = Motor('B')
        self.motor_pair = MotorPair('A', 'B')
        self.hub = MSHub()
        self.motion_sensor = hub.motion_sensor

    def drive_forward(self, distance):
        
        self.motion_sensor.reset_yaw_angle()
        while self.right_motor. get_degrees_counted() < distance:
            self .motor_pair.start(-self.motion_sensor.get_yaw.angle()*30)
        self .motor_pair.stop()
    def turn_left(self, degrees):
     
main()