# Example of a Python UDP server

import UdpComms as U
import time
import modi

# define range constant 
# If value differ between sensors, use list
cls = 40
mid = 80
far = 120

"""
# modi sensor init
bundle = modi.MODI()
network = bundle.networks[0]
ul0 = bundle.ultrasonics[0]
ul1 = bundle.ultrasonics[1]
ul2 = bundle.ultrasonics[2]
ul3 = bundle.ultrasonics[3]
ul4 = bundle.ultrasonics[4]
ul5 = bundle.ultrasonics[5]
ul6 = bundle.ultrasonics[6]
ul7 = bundle.ultrasonics[7]
ul8 = bundle.ultrasonics[8]

# for test
ultrasonics = [30,30,30,50,50,50,200,200,200]
ul0 = ultrasonics[0]
ul1 = ultrasonics[1]
ul2 = ultrasonics[2]
ul3 = ultrasonics[3]
ul4 = ultrasonics[4]
ul5 = ultrasonics[5]
ul6 = ultrasonics[6]
ul7 = ultrasonics[7]
ul8 = ultrasonics[8]
"""


# Create UDP socket to use for sending (and receiving)
sock = U.UdpComms(udpIP="127.0.0.1", portTX=8000, portRX=8001, enableRX=True, suppressWarnings=True)

while True:
    time.sleep(0.5) # minimum detection time
    key = input("Enter step number among 0,2,4,6,8: ")


    """
    # get sensor value
    row = [ul6, ul7, ul8]
    col = [ul0 if ul0<ul1 else ul1, ul2 if ul2<ul3 else ul3, ul4 if ul4<ul5 else ul5]

    # set 1 / 2 / 3 if stepped for each row and column
    for i in range(3):
        row[i] = [1 if row[i]<cls else (2 if row[i]<mid else (3 if row[i]<far else 0))]
        col[i] = [1 if col[i]<cls else (2 if col[i]<mid else (3 if col[i]<far else 0))]

    # value init - Unpressed : 0 / Pressed : 1
    step = [0,0,0,0,0,0,0,0,0] # Each position denote number

    # detection result update
    for i in range(3):
        if row[i] != 0:
            for j in range(3):
                if col[j] == i+1:
                    if (3*i+j) %2 == 0: 
                        step[3*i+j] = 1
    """
    

    step = [0,0,0,0,0,0,0,0,0]
    if key in ['0','2','4','6','8']:
        step[int(key)] = 1


    txt = ""
    for i in range(5):
        txt = txt + str(step[2*i])

    print("Current step info:",txt)
    
    sock.SendData(txt) # Send this string to other application

    data = sock.ReadReceivedData() # read data

    if data != None: # if NEW data has been received since last ReadReceivedData function call
        print(data) # print new received data
