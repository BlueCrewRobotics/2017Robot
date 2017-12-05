#!/usr/bin/env python3

import wpilib
from wpilib.buttons import JoystickButton
from magicbot import MagicRobot

from components.drivetrain import Drivetrain
from components.shooter import Shooter
from components.climber import Climber

from common.xbox import XboxController

class BluCubed(MagicRobot):
    #Initializing classes
    drivetrain = Drivetrain
    shooter = Shooter
    climber = Climber

    def createObjects(self):

        #Defines climb and shoot motors
        self.climb_motor = wpilib.Talon(3)
        self.shoot_motor = wpilib.Talon(4)

        #Defines driving motors
        self.right_motor = wpilib.Talon(1)
        self.left_motor = wpilib.Talon(0)

        #Defining what motors are being used
        self.robot_drive = wpilib.RobotDrive(self.right_motor, self.left_motor)

        #Defines joystick and controller
        self.drive_joystick = wpilib.Joystick(0)
        self.controller = XboxController(0)

    def teleopPeriodic(self):
        self.drivetrain.arcadeDrive()

        #Stops and starts the shooter if b is pressed or released
        if self.controller.b():
            self.shooter.shoot()
        else:
            self.shooter.stop()

        #Stop and starts climb motor if y is pressed or released
        if self.controller.y():
            self.climber.climb()
        else:
            self.climber.stop_climb()

#Main Function
if __name__ == '__main__':
    wpilib.run(BluCubed)
