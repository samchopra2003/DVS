# OPENCV CAPTURE VIDEO FROM CAMERA USING OPENCV

import cv2
import numpy as np

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
        # cv2.imshow("Samarth_Video", grayFrame)
        
        # going to be saving frame values and then comparing to previous frame
        frameCounter += 1
        frameList.append(grayFrame)
        
        if frameCounter >= 2: # comparing latest two frames and subtract (find difference in new frame)
            frameList[frameCounter-1] = frameList[frameCounter-1].astype(np.int16)
            frameList[frameCounter-2] = frameList[frameCounter-2].astype(np.int16)
            frameDifference = frameList[frameCounter-1] - frameList[frameCounter-2]          
            # print('Frame difference = ', frameDifference)

            # now lets only show difference of 20 threshold value on dvs
            # dvs = np.zeros(grayFrame.shape)
    
            dvs = frameDifference
            with np.nditer(dvs, op_flags=['readwrite']) as it:
                for x in it:
                    if x >= 20:
                        x[...] = 255 # 255 is white
                    elif x <= -20:
                        x[...] = 0 # 0 is black
                    else:
                        x[...] = 125 # pretty darn grey
            print('dvs=', dvs)
            cv2.imshow("DVS", dvs)
            


        key = cv2.waitKey(1) # wait 1 ms 
        if key==ord("q"): # q is quit
            break # when user presses q, while loop breaks
        


webcam.release()
cv2.destroyAllWindows()