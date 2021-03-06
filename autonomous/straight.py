from magicbot import AutonomousStateMachine, tunable, timed_state
             
from components.drivetrain import Drivetrain
                    
class Straight(AutonomousStateMachine):

    MODE_NAME = 'Drive Straight'
    DEFAULT = True
    
    drivetrain = Drivetrain
    
    drive_speed = tunable(0.5)

    @timed_state(duration=2, first=True)
    def dont_do_something(self):
        '''This happens first'''
        pass

    @timed_state(duration=2)
    def do_something(self):
        '''This happens second'''
        self.drivetrain.driveStraight()