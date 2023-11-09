import modi
import time

bundle = modi.MODI()
network = bundle.networks[0]
ir = bundle.irs[0]
ul = bundle.ultrasonics[0]

while True:
    print("ir: %f", ir.proximity)
    print("ul: %f", ul.distance)
    time.sleep(1)
