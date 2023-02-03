# OPENCV CAPTURE VIDEO FROM CAMERA USING OPENCV

import cv2
import numpy

webcam = cv2.VideoCapture(0) # 0 denotes default laptop webcam

def make720p(): # makes webcam 720p
    webcam.set(3, 1280)
    webcam.set(4, 720)

# make720p()

stop = False
while True:
    ret, frame = webcam.read() # return 

    if ret:
        grayFrame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        cv2.imshow("Samarth_Video", grayFrame)
        key = cv2.waitKey(1) # wait 1 ms 
        if key==ord("q"): # q is quit
            break # when user presses q, while loop breaks
       


webcam.release()
cv2.destroyAllWindows()



