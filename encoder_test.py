import wpilib
from wpilib.drive import DifferentialDrive
from rev import CANSparkMax, CANSparkMaxLowLevel
from wpilib import SmartDashboard
from networktables import NetworkTables


class MyRobot(wpilib.TimedRobot):
    def robotInit(self):
        self.m_motor = CANSparkMax(2, CANSparkMaxLowLevel.MotorType.kBrushless)
        self.m_motor.restoreFactoryDefaults()
        self.m_stick = wpilib.XboxController(0)
        self.m_encoder = self.m_motor.getEncoder()
        self.sd = NetworkTables.getTable("LiveWindow")
        NetworkTables.initialize(server="127.0.0.1")

    def teleopPeriodic(self):
        self.m_motor.set(self.m_stick.getRawAxis(2))
        self.sd.putNumber("Encoder Position", self.m_encoder.getPosition())
        self.sd.putNumber("Encoder Velocity", self.m_encoder.getVelocity())


if __name__ == "__main__":
    wpilib.run(MyRobot)
