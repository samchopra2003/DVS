# OPENCV CAPTURE VIDEO FROM CAMERA USING OPENCV

import cv2
import numpy as np
import time

webcam = cv2.VideoCapture(0) # 0 denotes default laptop webcam
threshold = 20

def make720p(): # makes webcam 720p
    webcam.set(3, 1280)
    webcam.set(4, 720)

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

            # dvs = np.zeros(grayFrame.shape)
            # threshold value of 20 is pretty sensitive
            # dvs = frameDifference
            # print(frameDifference)
            

            # working code (white background instead of grey)
            dvs = np.ones(frameDifference.shape) * 128
            dvs[frameDifference >= threshold] = 255
            dvs[frameDifference <= -threshold] = 0
            print(dvs)


            # dvs[abs(dvs) <= threshold] = 128
            # with np.nditer(dvs, op_flags=['readwrite']) as it:
            #     for x in it:
            #         if x <= 125 and x >= threshold: # 10 is the threshold value (below 125 is positive vals)
            #             x[...] = 255 # 255 is white
            #         elif x >= 125 and x <= (255 - threshold): # threshold value again 10
            #             x[...] = 0 # 0 is black
            #         else:
            #             x[...] = 125 # pretty darn grey
            # print('dvs=', dvs)
            cv2.imshow("DVS", dvs)
            #end = time.time()
            #print('end= ',end - start)

        key = cv2.waitKey(1) # wait 1 ms 
        if key==ord("q"): # q is quit
            break # when user presses q, while loop breaks
        


webcam.release()
cv2.destroyAllWindows()