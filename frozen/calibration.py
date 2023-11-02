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
# Good
motor.speed = -50,-50
time.sleep(0.67)
motor.speed = 0,0
time.sleep(0.5)

motor.speed = 50,-43
time.sleep(2.36)
motor.speed = 0,0
time.sleep(0.5)
motor.speed = 25, 0
time.sleep(0.3)
motor.speed = 0,0
time.sleep(0.1)  

print("left")
motor.speed = 50,50
time.sleep(0.65)
motor.speed = 0,0
time.sleep(1)


motor.speed = 50,-43
time.sleep(2.33)
motor.speed = 0,0
time.sleep(0.59)
motor.speed = 0,0
time.sleep(0.1)
motor.speed = 25, 0
time.sleep(0.42)
motor.speed = 0,0
time.sleep(0.1)  





"""
for i in range(7):
    motor.speed = 50,50
    time.sleep(0.7)
    motor.speed = 0, 0
    time.sleep(0.5)
    

    

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

