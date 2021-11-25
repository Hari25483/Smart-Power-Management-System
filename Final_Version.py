######################################################################################################################
#
#     Author : Hariharan Raveenthiran
#     Prototype function for changing speed of motor(AC) by inputting no. of persons detected from photos
#
######################################################################################################################


#Importing required libraries
import RPi.GPIO as GPIO  
import time
from time import sleep

#ComputerVison libraries
import numpy as np
import cv2


in1 = 24
in2 = 23
en = 25

MAX_NO_OF_PEOPLE=30
#If DIRECTION_SELECTOR=1 motor will move forward. Else it moves backwards.
DIRECTION_SELECTOR=1

GPIO.setmode(GPIO.BCM)
GPIO.setup(in1,GPIO.OUT)
GPIO.setup(in2,GPIO.OUT)
GPIO.setup(en,GPIO.OUT)
GPIO.output(in1,GPIO.LOW)
GPIO.output(in2,GPIO.LOW)
p=GPIO.PWM(en,1000)

#Start servo motor with 25 as default duty cycle
p.start(25)

#Setting up the LED
LED =4                      
GPIO.setwarnings(False)
GPIO.setup( LED, GPIO.OUT)  
# 50Hz PWM Frequency  
pwm_led = GPIO.PWM( LED, 200)  

# Start the LED with full brightness. If you want to start with low brightness, simply change the argument. 
pwm_led.start(100)


###############This part detects the no of faces using haarcascade_frontalface_default.xml that is provided by opencv in github.###########

face_cascade = cv2.CascadeClassifier("/home/pi/Downloads/haarcascade_frontalface_default.xml")
image = cv2.imread('/home/pi/Downloads/WhatsApp Image 2021-04-24 at 2.51.03 AM (2).jpeg')
grayImage = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

#facedetection and light manupilation
faces = face_cascade.detectMultiScale(grayImage)
  

print(type(faces))

####Print the no of faces detected.  
if len(faces) == 0:
    print("No faces found")
  
else:
    print (faces)
    print (faces.shape)
    print("Number of faces detected: " + str(faces.shape[0]))
    no_of_faces=faces.shape[0]

    
##Change the speed of motor (AC) , and brightness of bulb according to no of persons detected.
try:
    while True:
            #Get the duty cycle depending the no of people inside the room.
            duty_s = (no_of_faces/MAX_NO_OF_PEOPLE)*100  
            # Convert into Integer Value
            x= (100 - duty_s)
            duty = int(x)  
            pwm_led.ChangeDutyCycle(duty)
            p.ChangeDutyCycle(duty)
        
except KeyboardInterrupt:
    
    print("Exiting Program")
    GPIO.cleanup()  



for (x,y,w,h) in faces:
    cv2.rectangle(image,(x,y),(x+w,y+h),(0,255,0),1)

cv2.rectangle(image, ((0,image.shape[0] -25)),(270, image.shape[0]), (255,255,255), -1)
cv2.putText(image, "Number of faces detected: " + str(faces.shape[0]), (0,image.shape[0] -10), cv2.FONT_HERSHEY_TRIPLEX, 0.5,  (0,0,0), 1)

cv2.imshow('Image with faces',image)
cv2.waitKey(0)
cv2.destroyAllWindows()


