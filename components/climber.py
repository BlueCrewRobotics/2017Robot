import wpilib
#Commands to make the robot climb.
class Climber:
    climb_motor = wpilib.Talon
    
    #Set robot to climb when motor is on.
    def climb(self):
        self.climb_motor.set(1)
    
    #Stops the robot from climbing when motor is off.
    def stop_climb(self):
        self.climb_motor.set(0)
    
    #Execute is needed, but won't work with a given value.
    def execute(self):
        pass
