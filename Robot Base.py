from hub import light_matrix, port
import motor_pair
import runloop
import math 
import motor 

SPEED = 90

async def main():
    # write your code here
    await light_matrix.write("Hi!")

class Kraken:
    def __init__(self):
        self.wheel_diameter = 5.5 # cm
        self.left_motor = port.A
        self.right_motor = port.B 
        self.motor_pair = motor_pair.PAIR_1
        motor_pair.pair(self.motor_pair, self.left_motor, self.right_motor)
        
    async def drive_forward(self, distance, speed = SPEED):
        distance_in_degrees = distance * (360.0 / (self.wheel_diameter * math.pi))
        start_position = motor.relative_position(self.right_motor)
        goal_position = start_position + distance_in_degrees
        small_goal = goal_position - 7 * (360.0 / (self.wheel_diameter * math.pi))
        while motor.relative_position(self.right_motor) < small_goal:
            self .motor_pair.start(self.correction(),speed)
        while motor.relative_position(self.right_motor) < goal_position:
            self.motor_pair.start(self.correction(),10)
        self.motor_pair.stop()

runloop.run(main())
