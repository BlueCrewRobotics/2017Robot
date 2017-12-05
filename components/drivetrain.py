#imports the wpi library for later use
import wpilib

#is used in  autonomous/straight.py, and robot.py
class Drivetrain:
    #these variables essentially set up different for the overall program inputs and outputs
    robot_drive = wpilib.RobotDrive
    drive_joystick = wpilib.Joystick
    right_motor = wpilib.Talon
    left_motor = wpilib.Talon

    #used in robot.py
    def arcadeDrive(self):
        #this pretty much sets up the joystick
        self.robot_drive.arcadeDrive(self.drive_joystick, True)
    
    #used in autonomous/straight.py
    def driveStraight(self):
        #sets the speeds at which the motors drive
        self.right_motor.set(0.5)
        self.left_motor.set(0.5)

    def execute(self):
        #unfinished
        pass