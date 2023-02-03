# OPENCV CAPTURE VIDEO FROM CAMERA USING OPENCV

import cv2
import numpy

webcam = cv2.VideoCapture(0) # 0 denotes default laptop webcam

def make720p(): # makes webcam 720p
    webcam.set(3, 1280)
    webcam.set(4, 720)

# make720p()
frameCounter = 0
frameList = [] # saves all frames

stop = False
while True:
    ret, frame = webcam.read() # return 

    if ret:
        grayFrame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        cv2.imshow("Samarth_Video", grayFrame)
        key = cv2.waitKey(1) # wait 1 ms 
        if key==ord("q"): # q is quit
            break # when user presses q, while loop breaks
        elif key==ord("t"):
            snapshot = frame.copy() # takes copy of frame when t is pressed
            snapshot = cv2.cvtColor(snapshot, cv2.COLOR_BGR2GRAY)
            cv2.imshow("Snapshot", snapshot)
            frameCounter += 1 
            frameList.append(snapshot)
            print(snapshot.shape)
            print(f"Frame {frameCounter}", "\n", snapshot)
            print('iso_pix=', frame[0][0][0])
            print('iso_pix1=', frame[0][1][0])
            print('iso_pix2=', frame[0][1][1])

        '''
        if len(frameList) >= 2: # comparing latest two frames and subtract (find difference in new frame)
            frameDifference = frameList[frameCounter-2] - frameList[frameCounter-1]
            print('Frame difference = ', frameDifference)
        '''


webcam.release()
cv2.destroyAllWindows()



