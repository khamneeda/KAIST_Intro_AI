import UdpComms as U
import modi
import time

# define range constant 
# Different beween sensor
rcls = [1,36,1]
rmid = [56,57,57]
rfar = [83,83,86]
ccls = [1,0,1]
cmid = [65,65,57]
cfar = [85,85,79]
t = 0

# Create UDP socket to use for sending
sock = U.UdpComms(udpIP="127.0.0.1", portTX=8000, portRX=8001, enableRX=True, suppressWarnings=True)

while True:
    time.sleep(0.05) # minimum detection time
    t += 1
    # get sensor value
    row = [[0,82,200,200,200],[200,200,56,200,200],[200,200,200,0,85]]
    col = [[0,200,200,84,200],[200,200,200,200,200],[200,0,200,200,78]] # middle one is not used

    print("Row:", row)
    print("Coulmn", col)

    # set 1 / 2 / 3 if stepped for each row and column
    for i in range(3):
        row[i] = 1 if row[i][t%5]<rcls[i] else (2 if row[i][t%5]<rmid[i] else (3 if row[i][t%5]<rfar[i] else 0))
        col[i] = 1 if col[i][t%5]<ccls[i] else (2 if col[i][t%5]<cmid[i] else (3 if col[i][t%5]<cfar[i] else 0))

    print("Row:", row)
    print("Column:", col)

    # value init - Unpressed : 0 / Pressed : 1
    step = [0,0,0,0,0,0,0,0,0] # Each position denote number

    # detection result update
    for i in range(3):
        if row[i] != 0:
            for j in range(3):
                if col[j] == i+1:
                    if (3*i+j) %2 == 0: 
                        step[3*i+j] = 1
                if i == 1 and row[i] == 2:
                    step[4] = 1

    
    print("#######")
    print("#"+ str(step[0]) +"###"+ str(step[2]) +"#")
    print("#######")
    print("###"+ str(step[4]) +"###")
    print("#######")
    print("#"+ str(step[6])  +"###"+ str(step[8]) +"#")
    print("#######")

    txt = ""
    for i in range(5):
        txt = txt + str(step[2*i])

    print("Current step info:",txt)
    
    sock.SendData(txt) # Send this string to other application

    