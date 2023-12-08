import modi
import time

# modi sensor init
bundle = modi.MODI()
network = bundle.networks[0]
ul0 = bundle.ultrasonics[0]

while True:
    print(ul0.distance)
    time.sleep(0.5)
