from picamera.array import PiRGBArray
from picamera import PiCamera
#import sys, os
import time
import cv2
import numpy as np

camera = PiCamera()
camera.resolution = (160, 128)
camera.framerate = 16
rawCapture = PiRGBArray(camera, size=camera.resolution)

time.sleep(0.1)


lk_params = dict(winSize=(15,15), maxLevel=2, criteria=(cv2.TERM_CRITERIA_EPS | cv2.TERM_CRITERIA_COUNT, 10, 0.03))
ft_params = dict(maxCorners=100, qualityLevel=0.3, minDistance=7, blockSize=7)

counter=0
for frame in camera.capture_continuous(rawCapture, format="bgr", use_video_port=True):
    image_flip = frame.array
    image_curr = cv2.flip(image_flip,1)
    gray_curr = cv2.cvtColor(image_curr, cv2.COLOR_BGR2GRAY)

    if counter > 0 :
        ft_curr, status, err = cv2.calcOpticalFlowPyrLK(gray_prev, gray_curr, ft_prev, None, **lk_params)
        good_prev = ft_prev[status==1]
        good_curr = ft_curr[status==1]
        #for i, (pt2,pt1) in enumerate(zip(good_curr,good_prev)):
        for i, pt2 in enumerate(good_curr):
            x1,y1=pt2.ravel()
            cv2.circle(image_temp,(x1,y1),5,[255,0,0],-1)
        image_buf=cv2.add(image_curr, image_temp)
        cv2.imshow("Frame", image_buf)

    else:
        counter=1
        ft_curr = cv2.goodFeaturesToTrack(gray_curr, mask = None, **ft_params)
        image_temp= np.zeros_like(image_curr)

    
    gray_prev= gray_curr
    ft_prev= ft_curr
    #cv2.imshow("Frame", image_curr)
    key = cv2.waitKey(1) & 0xFF

    rawCapture.truncate(0)

    if key == ord("q"):
        break
