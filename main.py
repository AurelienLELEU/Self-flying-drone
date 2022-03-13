# libraries
import cv2
import os
import serial
global x2
import time
arduino = serial.Serial(port='COM4', baudrate=115200, timeout=.1)

# cascade classifier ( positive images = w/face, negative images w/o face )
cascPath = os.path.dirname(
    cv2.__file__) + "/data/haarcascade_frontalface_alt2.xml"
faceCascade = cv2.CascadeClassifier(cascPath)

# turns on webcam 
video_capture = cv2.VideoCapture(0)

# Capture frame-by-frame
def write_read(x):
        arduino.write(bytes(x, 'utf-8'))
        
while True:
    ret, frame = video_capture.read()
    # image to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    """ scale factor -> how much the image size is reduced at each image scale, 
        minneighbors -> quality of the detcted faces ( average = 3~6)
        minsize -> min possible object size, smaller is ignored ( average 30,30 )
        maxsize -> max possible object size, bigger is ignored
        flags -> default 
    """
    faces = faceCascade.detectMultiScale(gray,scaleFactor=1.05,minNeighbors=4,minSize=(50, 50),flags=cv2.CASCADE_SCALE_IMAGE)
    num ="=x=y"
    write_read(num)
    # draws rectangle around face
    for (x,y,w,h) in faces:
        cv2.rectangle(frame, (x, y), (x + w, y + h),(0,255,0), 2)
        x1 = x
        x2 = (x + w)/2
        y1 = y
        y2 = (y + h)/2
        if (x2<185 ):
            if (y2<140):
                num = "-x+y"
                write_read(num)
            elif(y2>160):
                num = "-x-y"
                write_read(num)
            else:
                num = "-x=y"
                write_read(num)
        elif (x2<215):
            if (y2<140):
                num = "=x+y"
                write_read(num)
            elif(y2>160):
                num = "=x-y"
                write_read(num)
            else:
                num = "=x=y"
                write_read(num)
        elif (x2>215):
            if (y2<140):
                num = "+x+y"
                write_read(num)
            elif(y2>160):
                num = "+x-y"
                write_read(num)
            else:
                num = "+x=y"
                write_read(num)
        
    # Display the resulting frame
    cv2.imshow('Video', frame)
    
    # quit webcam with -q
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break    


video_capture.release()
cv2.destroyAllWindows()
