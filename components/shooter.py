import wpilib

class Shooter:
    shoot_motor = wpilib.Talon

    def shoot(self):
        self.shoot_motor.set(-0.35)

    def stop(self):
        self.shoot_motor.set(0)

    def execute(self):
        pass
