import time
from networktables import NetworkTables
import photonvision
import logging

logging.basicConfig(level=logging.INFO)

NetworkTables.initialize()
sd = NetworkTables.getTable("SmartDashboard")
camera = photonvision.PhotonCamera()

i = 0
while True:
    print("dsTime:", sd.getNumber("dsTime", -1))

    sd.putNumber("robotTime", i)
    time.sleep(1)
    i += 1
    print("BEEP", camera.getLatestResult())
