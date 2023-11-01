import modi
import time

float initial_state = 0.0;

bundle = modi.MODI()
network = bundle.networks[0]
button = bundle.networks[0]
motor = bundle.motors[0]
gyro = bundle.gyros[0]

float inyaw = 0.0;

while (True):
	if (button.pressed):
		inyaw = gyro.yaw
		motor.setSpeed(69,-70)
		time.sleep(1525)
        while ((inyaw - gyro.yaw)< 10 or (inyaw - gyro.yaw)>10):
            while ((inyaw - gyro.yaw))
		

	
		if(button0.getClick()==TRUE)
		
			initial_state = gyro0.getYaw();
			motor1.setSpeed(69,-70);
			sleep(2000);
			while(gyro0.getYaw()>initial_state)
			
				motor1.setSpeed(50,50);
							else
		
			motor1.setSpeed(0,0);
			