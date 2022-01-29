import wpilib
from wpilib.drive import DifferentialDrive
from rev import

class MyRobot(wpilib.TimedRobot):
    def robotInit(self):
        self.m_motor = wpilib.Spark(2)
        self.m_stick = wpilib.XboxController(0)
        self.m_encoder = self.m_motor.getEncoder()


    def teleopInit(self):
        """Executed at the start of teleop mode"""
        self.myRobot.setSafetyEnabled(True)

    def teleopPeriodic(self):
        """Runs the motors with tank steering"""
        self.myRobot.tankDrive(self.leftStick.getY() * -1, self.rightStick.getY() * -1)


if __name__ == "__main__":
    wpilib.run(MyRobot)
