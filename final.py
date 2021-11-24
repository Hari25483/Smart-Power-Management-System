#led libs
import RPi.GPIO as GPIO  
import time
from time import sleep

#computervison libraries
import numpy as np
import cv2

in1 = 24
in2 = 23
en = 25
temp1=1

GPIO.setmode(GPIO.BCM)
GPIO.setup(in1,GPIO.OUT)
GPIO.setup(in2,GPIO.OUT)
GPIO.setup(en,GPIO.OUT)
GPIO.output(in1,GPIO.LOW)
GPIO.output(in2,GPIO.LOW)
p=GPIO.PWM(en,1000)

p.start(25)

# Led1 on my Board  
led =4                      
GPIO.setwarnings(False)
GPIO.setup( led, GPIO.OUT)  
# 50Hz PWM Frequency  
pwm_led = GPIO.PWM( led, 200)  
# Full Brightness, 100% Duty Cycle  
pwm_led.start(100)

face_cascade = cv2.CascadeClassifier("/home/pi/Downloads/haarcascade_frontalface_default.xml")
image = cv2.imread('/home/pi/Downloads/WhatsApp Image 2021-04-24 at 2.51.03 AM (2).jpeg')
grayImage = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

#facedetection and light manupilation
faces = face_cascade.detectMultiScale(grayImage)
  
print(type(faces))
  
if len(faces) == 0:
    print("No faces found")
  
else:
    print (faces)
    print (faces.shape)
    print("Number of faces detected: " + str(faces.shape[0]))
    no_of_faces=faces.shape[0]

    

try:
    
    while True:
        
            duty_s = (no_of_faces/30)*100  
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


