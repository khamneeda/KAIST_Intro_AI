import modi
import time

# define range constant 
# If value differ between sensors, use list
cls = 40
mid = 80
far = 120

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

while True:
    time.sleep(0.01) # minimum detection time

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