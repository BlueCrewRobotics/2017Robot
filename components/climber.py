import wpilib

class Climber:
    climb_motor = wpilib.Talon

    def climb(self):
        self.climb_motor.set(1)

    def stop_climb(self):
        self.climb_motor.set(0)

    def execute(self):
        pass
