import cv2

# To use the webcam in the rasperry pi to start capturing video
cap = cv2.VideoCapture(0)

# Load the cascade
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface.xml')

while True:
    # Read the frame
    _, img = cap.read()
    # Convert to grayscale
    
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    
    #Faces will be stored in faces variable
    faces = face_cascade.detectMultiScale(gray, 1.1, 4)
    # Draw the rectangle around each face

    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)
    

    #Show a frame with faces detected
    cv2.imshow('Face counter', img)
    print(len(faces))
    k = cv2.waitKey(30) & 0xff
    if k==27:
        break

#Stop capturing and release the video capture
cap.release()