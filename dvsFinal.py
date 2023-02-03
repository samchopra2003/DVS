# OPENCV CAPTURE VIDEO FROM CAMERA USING OPENCV

import cv2
import numpy as np
import time

webcam = cv2.VideoCapture(0) # 0 denotes default laptop webcam
threshold = 20

# make720p()
frameCounter = 0
frameList = [] # saves all frames

stop = False
while True:
    ret, frame = webcam.read() # return 
    start = time.time() # get start time

    if ret:
        grayFrame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        # cv2.imshow("Samarth_Video", grayFrame)
        
        # going to be saving frame values and then comparing to previous frame
        frameCounter += 1
        frameList.append(grayFrame)
        
        if frameCounter >= 2: # comparing latest two frames and subtract (find difference in new frame)
            frameDifference = frameList[frameCounter-1].astype(np.int16) - frameList[frameCounter-2].astype(np.int16)
            # print('Frame difference = ', frameDifference)            

            # working code (white background instead of grey)
            dvs = np.ones(frameDifference.shape) * 0.5
            dvs[frameDifference >= threshold] = 255
            dvs[frameDifference <= -threshold] = 0
            # print(dvs)

            cv2.imshow("DVS", dvs)
            #end = time.time()
            #print('end= ',end - start)

        key = cv2.waitKey(1) # wait 1 ms 
        if key==ord("q"): # q is quit
            break # when user presses q, while loop breaks
        


webcam.release()
cv2.destroyAllWindows()