import modi
# import sys
# sys.path.append('../pymodi/modi')
# import pymodi.modi
import time

bundle = modi.MODI()
network = bundle.networks[0]
#button = bundle.networks[0]
#motor = bundle.motors[0]
dial = bundle.dials[0]
display = bundle.displays[0]
#gyro = bundle.gyros[0]


while(True):
	if(dial.degree > 30):
		display.text = "Bigger"
	else:
		display.text = "Smaller"