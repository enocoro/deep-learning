import cv2
import numpy as np
 
lk_params = dict(winSize=(15,15), maxLevel=2, criteria=(cv2.TERM_CRITERIA_EPS | cv2.TERM_CRITERIA_COUNT, 10, 0.03))
ft_params = dict(maxCorners=100, qualityLevel=0.3, minDistance=7, blockSize=7)

img0 = cv2.imread("eno6.jpg")
gray0 = cv2.cvtColor(img0, cv2.COLOR_BGR2GRAY)
ft0 = cv2.goodFeaturesToTrack(gray0, mask = None, **ft_params)

img1 = cv2.imread("eno7.jpg")
gray1 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
ft1, status, err = cv2.calcOpticalFlowPyrLK(gray0, gray1, ft0, None, **lk_params)

img_buf0= np.zeros_like(img1)
img_buf1= np.zeros_like(img1)
for i, (pt0,pt1) in enumerate(zip(ft0,ft1)):
    x0,y0=pt0.ravel()
    cv2.circle(img_buf0,(x0,y0),5,[0,255,0],-1)
    x1,y1=pt1.ravel()
    cv2.circle(img_buf1,(x1,y1),5,[0,0,255],-1)

img_out0 = cv2.add(img_buf0,img0)
img_out1 = cv2.add(img_buf1,img1)

cv2.imshow('image0', img_out0)
cv2.imshow('image1', img_out1)
cv2.waitKey(0)
cv2.destroyAllWindows()
