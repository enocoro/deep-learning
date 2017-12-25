# -*- coding: UTF-8 -*-
#http://qiita.com/Algebra_nobu/items/a488fdf8c41277432ff3
#https://ai-coordinator.jp/opencv-object-detection
from picamera.array import PiRGBArray
from picamera import PiCamera
import cv2
import os
import time
 
# カメラの起動
camera = PiCamera()

camera.resolution = (320, 240)
camera.framerate = 32
rawCapture = PiRGBArray(camera, size=(320, 240))

cascPath = sys.argv[1]
faceCascade = cv2.CascadeClassifier(/home/pi/opencv-3.1.0/data/haarcascades/haarcascade_fullbody.xml)

while(True):
 
    # 動画ストリームからフレームを取得
    ret, frame = cap.read() 
    
    #物体認識（人）の実行
    facerect = f_cascade.detectMultiScale(frame, scaleFactor=1.2, minNeighbors=2, minSize=(1, 1))
    
    #検出した人を囲む矩形の作成
    for rect in facerect:
        cv2.rectangle(frame, tuple(rect[0:2]),tuple(rect[0:2] + rect[2:4]), (255, 255, 255), thickness=2)
        
        text = 'p'
        font = cv2.FONT_HERSHEY_PLAIN
        cv2.putText(frame,text,(rect[0],rect[1]-10),font, 2, (255, 255, 255), 2, cv2.LINE_AA)
        
    # 表示
    cv2.imshow("Show FLAME Image", frame) 
 
    # qを押したら終了。
    k = cv2.waitKey(1)
    if k == ord('q'):
        break
 
cap.release()
cv2.destroyAllWindows()