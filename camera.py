from picamera import PiCamera
from time import sleep

camera = PiCamera()
camera.resolution=(320,240)


camera.start_preview()
camera.capture('eno1.jpg')
sleep(0.05)
camera.capture('eno2.jpg')
sleep(0.05)
camera.capture('eno3.jpg')
sleep(0.05)
camera.capture('eno4.jpg')
sleep(0.05)
camera.capture('eno5.jpg')
sleep(0.05)
camera.capture('eno6.jpg')
sleep(0.05)
camera.capture('eno7.jpg')
sleep(0.05)
camera.capture('eno8.jpg')
sleep(0.05)
camera.capture('eno9.jpg')
sleep(0.05)
camera.capture('eno10.jpg')
sleep(0.05)
camera.stop_preview()
