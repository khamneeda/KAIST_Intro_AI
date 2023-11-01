import modi
import time

bundle = modi.MODI()
network = bundle.networks[0]
button = bundle.networks[0]
motor = bundle.motors[0]
gyro = bundle.gyros[0]

print("Yaw:", gyro.yaw, "Max_interval:", 0)
print("Pitch:", gyro.pitch, "Max_interval:", 0)
print("Roll:", gyro.roll, "Max_interval:", 0, "\n")
time.sleep(2)
p_max =gyro.pitch
p_min =p_max
r_max =gyro.roll
r_min =r_max
y_max =gyro.yaw
y_min =y_max

init_time = time.time()
while (time.time() - init_time < 6):
    print("Time:", time.time()-init_time)
    print("Yaw:", gyro.yaw, "Max_interval:", y_max-y_min)
    print("Pitch:", gyro.pitch, "Max_interval:", p_max-p_min)
    print("Roll:", gyro.roll, "Max_interval:", r_max-r_min, "\n")
	
	#max,min update
    if (gyro.pitch > p_max):
        p_max = gyro.pitch
    elif (gyro.pitch < p_min):
        p_min = gyro.pitch
    if (gyro.roll > r_max):
        r_max = gyro.roll
    elif (gyro.roll < r_min):
        r_min = gyro.roll
    if (gyro.yaw > y_max):
        y_max = gyro.yaw
    elif (gyro.yaw < y_min):
        y_min = gyro.yaw
    time.sleep(1)

p1 = gyro.pitch
r1 = gyro.roll
y1 = gyro.yaw


print("left")
motor.speed = 50,50
time.sleep(0.688)
motor.speed = 0, 0
time.sleep(1)

print("right")
motor.speed = -50,-50
time.sleep(0.688)
motor.speed = 0, 0

p_max =gyro.pitch
p_min =p_max
r_max =gyro.roll
r_min =r_max
y_max =gyro.yaw
y_min =y_max

mid_time = time.time()
while (time.time() - mid_time < 6):
    
    print("Time:", time.time()-mid_time)
    print("Yaw:", gyro.yaw, "Max_interval:", y_max-y_min)
    print("Pitch:", gyro.pitch, "Max_interval:", p_max-p_min)
    print("Roll:", gyro.roll, "Max_interval:", r_max-r_min, "\n")
	
	#max,min update
    if (gyro.pitch > p_max):
        p_max = gyro.pitch
    elif (gyro.pitch < p_min):
        p_min = gyro.pitch
    if (gyro.roll > r_max):
        r_max = gyro.roll
    elif (gyro.roll < r_min):
        r_min = gyro.roll
    if (gyro.yaw > y_max):
        y_max = gyro.yaw
    elif (gyro.yaw < y_min):
        y_min = gyro.yaw
    time.sleep(1)

p2 = gyro.pitch
r2 = gyro.roll
y2 = gyro.yaw

print("p1:", p1, "/ p2:", p2)
print("r1:", r1, "/ r2:", r2)
print("y1:", y1, "/ y2:", y2)