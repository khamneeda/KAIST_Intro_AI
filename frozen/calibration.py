import modi
# import sys
# sys.path.append('../pymodi/modi')
# import pymodi.modi
import time

bundle = modi.MODI()
network = bundle.networks[0]
button = bundle.networks[0]
motor = bundle.motors[0]
gyro = bundle.gyros[0]


# Fast
# print("Forward start")
# motor.speed = 70,-67
# time.sleep(1.32)

# turn right
motor.speed = -50,-50
time.sleep(0.688)
motor.speed = 0, 0

"""
# Good
motor.speed = 50,-44.5
time.sleep(2.47)
motor.speed = 0,0
time.sleep(0.1)
motor.speed = 25, 0
time.sleep(0.375)
motor.speed = 0,0
time.sleep(0.1)

motor.speed = 30, 30
time.sleep(0.12)


print("left")
motor.speed = 40,40
time.sleep(1.115)
motor.speed = 0,0
print("Forward start")
motor.speed = -40,-40
time.sleep(1.115)
motor.speed = 0,0


motor.speed = 0,0
            time.sleep(0.01)
            motor.speed = 50,-47    
            time.sleep(2.3)
"""

