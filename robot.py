#!/usr/bin/env python3

import wpilib
from wpilib.buttons import JoystickButton
from magicbot import MagicRobot

from components.drivetrain import Drivetrain
from components.shooter import Shooter
from components.climber import Climber

from common.xbox import XboxController

class BluCubed(MagicRobot):

    drivetrain = Drivetrain
    shooter = Shooter
    climber = Climber

    def createObjects(self):
        self.climb_motor = wpilib.Talon(3)
        self.shoot_motor = wpilib.Talon(4)

        self.right_motor = wpilib.Talon(1)
        self.left_motor = wpilib.Talon(0)

        self.robot_drive = wpilib.RobotDrive(self.right_motor, self.left_motor)

        self.drive_joystick = wpilib.Joystick(0)
        self.controller = XboxController(0)

    def teleopPeriodic(self):
        self.drivetrain.arcadeDrive()

        if self.controller.b():
            self.shooter.shoot()
        else:
            self.shooter.stop()

        if self.controller.y():
            self.climber.climb()
        else:
            self.climber.stop_climb()


if __name__ == '__main__':
    wpilib.run(BluCubed)
