import commands
import logging

import wpilib
from commandbased import CommandBasedRobot
from wpilib.command import Scheduler


class Marvin(CommandBasedRobot):

    def robotInit(self):

        pass

    def disabledInit(self):
        pass

    def disabledPeriodic(self):
        pass

    def autonomousInit(self):
        pass

    def autonomousPeriodic(self):
        pass

    def teleopInit(self):
        pass

    def teleopPeriodic(self):
        pass


if __name__ == '__main__':
    wpilib.run(Marvin)
