#imrpoting wpilib
import wpilib

#a class for the shooter
class Shooter:
    shoot_motor = wpilib.Talon

    #defining the shooter to shoot
    def shoot(self):    
        self.shoot_motor.set(-0.35)

    #defining the shooter to stop  
    def stop(self):  
        self.shoot_motor.set(0)

    #has to have it in order to run
    def execute(self):
        pass
