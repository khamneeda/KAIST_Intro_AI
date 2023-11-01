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

"""
print("Forward start")
motor.speed = 70,-67
time.sleep(1.32)

# Good
# motor.speed = 50,-47
# time.sleep(2.3)

motor.speed = 0,0

"""
"""
print("left")
motor.speed = 40,40
time.sleep(1.115)
motor.speed = 0,0
print("Forward start")
motor.speed = -40,-40
time.sleep(1.115)
motor.speed = 0,0
"""

