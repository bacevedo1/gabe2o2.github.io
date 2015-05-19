from gopigo import * #import all functions from the gopigo Library
import time #allows you to use the time.sleep() function
import math #allows you to use math functions like floor()

set speed (100) #you can use values from 0 to 255

enc_tgt(1,1,18) #set both motors to encode 18 steps of rotation
time.sleep(.1) #can make motor movement more reliable
fwd() #motion function in the gopigo library
time.sleep(3) #set this wait for as long as the movement will take

def move_forward(feet): #make a function that takes in a number of feet and moves the robot forward that far
    mm = feet * float(304.8)
    steps = mm/float(11.34)
    steps = int(steps)
    enc_tgt(1,1,steps) 
    time.sleep(.1)
    fwd()
    time.sleep(feet * 2)

def move_left():
    enc_tgt(1,0,14)
    time.sleep(.1)
    fwd()
    time.sleep(5)

def move_right():
    enc_tgt(0,1,14)
    time.sleep(.1)
    fwd()
    time.sleep(5)

move_forward(4)

