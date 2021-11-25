######################################################################################################################
#
#     Author : Hariharan Raveenthiran
#     Prototype function for changing speed of motor(AC) by inputting no. of persons
#
######################################################################################################################


import RPi.GPIO as GPIO          
from time import sleep


in1 = 24
in2 = 23
en = 25


#If DIRECTION_SELECTOR=1 motor will move forward. Else it moves backwards.
DIRECTION_SELECTOR=1


#Setting up the two servo motors
GPIO.setmode(GPIO.BCM)
GPIO.setup(in1,GPIO.OUT)
GPIO.setup(in2,GPIO.OUT)
GPIO.setup(en,GPIO.OUT)
GPIO.output(in1,GPIO.LOW)
GPIO.output(in2,GPIO.LOW)


#Set the PWM frequency
p=GPIO.PWM(en,1000)

p.start(25)
print("\n")
print("Instructions or commans are displayed below.")
print("r-Run s-Stop f-Forward b-Backward l-Low m-Medium h-High e-Exit")
    

while(True):

    x=int(input("Enter no of persons"))
    
    if (x=='r'):
        print("Run")
        if(DIRECTION_SELECTOR==1):
         GPIO.output(in1,GPIO.HIGH)
         GPIO.output(in2,GPIO.LOW)
         print("forward")
         x='z'
        else:
         GPIO.output(in1,GPIO.LOW)
         GPIO.output(in2,GPIO.HIGH)
         print("backward")
         x='z'


    elif x=='s':
        print("stop")
        GPIO.output(in1,GPIO.LOW)
        GPIO.output(in2,GPIO.LOW)
        x='z'
        
        
    else:
        print("Enter a valid command:")


    p.ChangeDutyCycle(25)