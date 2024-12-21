from hub import light_matrix, motion_sensor, port
import motor_pair
import runloop
import math 
import motor 

SPEED = 900

async def main():
   robot = Kraken()
   robot.reset_angle()
   front_motor = port.F
   back_motor = port.D 


   await robot.drive_forward(30)


class Kraken:
    def __init__(self):
        self.wheel_diameter = 5.5 # cm
        self.left_motor = port.A
        self.right_motor = port.B 
        self.motor_pair = motor_pair.PAIR_1
        motor_pair.pair(self.motor_pair, self.left_motor, self.right_motor)

    def show_state(self):
        print("current angle: {} / angle goal: {}".format(self.get_yaw(), self.angle_goal))

        
    # drive_forward tells the robot to drive in a
    # straight line "distance" centimeters forwards.
    async def drive_forward(self, distance, speed = SPEED):
        distance_in_degrees = distance * (360.0 / (self.wheel_diameter * math.pi))
        start_position = motor.relative_position(self.right_motor)
        goal_position = start_position + distance_in_degrees
        small_goal = goal_position - 7 * (360.0 / (self.wheel_diameter * math.pi))
        while motor.relative_position(self.right_motor) < small_goal:
            motor_pair.move(self.motor_pair, self.correction(),velocity = speed)
        while motor.relative_position(self.right_motor) < goal_position:
            motor_pair.move(self.motor_pair, self.correction(),velocity = 100)
        motor_pair.stop(self.motor_pair)
        
    async def drive_backward(self, distance, speed = SPEED):
        # convert distance (centimeters) to degrees
        distance_in_degrees = distance * (360.0 / (self.wheel_diameter * math.pi))
        start_position = motor.relative_position(self.right_motor)
        goal_position = start_position - distance_in_degrees
        # plus sign before the seven used to be a minus sign
        small_goal = goal_position + 7 * (360.0 / (self.wheel_diameter * math.pi))
        while motor.relative_position(self.right_motor) > small_goal:
            motor_pair.move(self.motor_pair, -self.correction(),velocity = -speed)
        while motor.relative_position(self.right_motor) > goal_position:
            motor_pair.move(self.motor_pair, -self.correction(),velocity = -100)
        motor_pair.stop(self.motor_pair)

    async def turn_left(self, degrees, speed = 500):
        if speed>500:
            speed = 500
        self.angle_goal = self.angle_goal - degrees
        small_goal = self.angle_goal + 20
        motor_pair.move_tank(self.motor_pair, -speed, speed)
        while self.get_yaw()>small_goal:
            # wait
            True
        motor_pair.move_tank(self.motor_pair, -100, 100)
        while self.get_yaw()>self.angle_goal:
            True
        motor_pair.stop(self.motor_pair)

    async def turn_right(self, degrees, speed = 500):
        if speed>500:
            speed = 500
        self.angle_goal = self.angle_goal + degrees
        small_goal = self.angle_goal - 20
        motor_pair.move_tank(self.motor_pair, speed, -speed)
        while self.get_yaw()<small_goal:
            # wait
            True
        motor_pair.move_tank(self.motor_pair, 100, -100)
        while self.get_yaw()<self.angle_goal:
            True
        motor_pair.stop(self.motor_pair)

    def correction(self):
        correction = self.angle_goal - self.get_yaw()
        correction *= 10
        if correction < -50:
            correction = -50
        if correction > 50:
            correction = 50
        return int(correction)

    # reset_angle tells the robot that it is currently facing
    # the right direction. Call this at the beginning of each
    # program and after the robot squares itself up on an
    # object.
    def reset_angle(self):
        self.angle_goal = 0
        motion_sensor.reset_yaw(0) 

    def get_yaw(self):
        yaw, _, _ = motion_sensor.tilt_angles()
        return yaw/10

runloop.run(main())
