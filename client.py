import sys
import time
from networktables import NetworkTables
import photonvision
import logging


camera = photonvision.PhotonCamera('photonvision')
logging.basicConfig(level=logging.INFO)

if len(sys.argv) != 2:
    print("Error: specify an IP to connect to!")
    exit(0)

ip = sys.argv[1]

NetworkTables.initialize(server=ip)

sd = NetworkTables.getTable("photonvision/mmal_service_16.1")

i = 0
while True:
    time.sleep(0.2)
    i += 1
    print("BEEP", sd.getNumber('targetPitch', -1), "*"*(int(sd.getNumber('targetYaw', -1))+15))
