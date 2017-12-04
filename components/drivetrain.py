import wpilib

class Drivetrain:
    robot_drive = wpilib.RobotDrive
    drive_joystick = wpilib.Joystick
    right_motor = wpilib.Talon
    left_motor = wpilib.Talon

    def arcadeDrive(self):
        self.robot_drive.arcadeDrive(self.drive_joystick, True)

    def driveStraight(self):
        self.right_motor.set(0.5)
        self.left_motor.set(0.5)

    def execute(self):
        pass