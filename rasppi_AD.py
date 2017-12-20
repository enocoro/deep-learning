import pigpio
import time

pi= pigpio.pi()

def readSpiADC ( numCH, pinCLK, pinMOSI, pinMISO, pinCS ):
    if numCH > 7 or numCH < 0:
        return -1
    pi.write(pinCS,pigpio.HIGH)
    pi.write(pinCLK,0)
    pi.write(pinCS,0)
    dataMOSI = numCH
    dataMOSI |= 0x18
    dataMOSI <<= 3
    for i in range(5):
        if dataMOSI & 0x80:
            pi.write(pinMOSI,1)
        else:
            pi.write(pinMOSI,0)
        dataMOSI <<= 1
        pi.write(pinCLK,1)
        pi.write(pinCLK,0)
    dataMISO = 0
    for i in range(13):
        pi.write(pinCLK,1)
        pi.write(pinCLK,0)
        dataMISO <<= 1
        if i>0 and pi.read(pinMISO)==pigpio.HIGH:
            dataMISO |= 0x1
    pi.write(pinCS,1)
    time.sleep(0.001)
    return dataMISO

PinCLK  = 11
PinMISO =  9
PinMOSI = 10
PinCS0  =  8
PinCS1  =  7

pi.set_mode(PinCLK,pigpio.OUTPUT)
pi.set_mode(PinMISO,pigpio.INPUT)
pi.set_mode(PinMOSI,pigpio.OUTPUT)
pi.set_mode(PinCS0,pigpio.OUTPUT)
pi.set_mode(PinCS1,pigpio.OUTPUT)

pinDIR= 16  
pinPWM= 20
pi.set_mode(pinDIR,pigpio.OUTPUT)
pi.set_mode(pinPWM,pigpio.OUTPUT)

try:
    while True:
        v00= readSpiADC(0,PinCLK,PinMOSI,PinMISO,PinCS0)
        v01= readSpiADC(1,PinCLK,PinMOSI,PinMISO,PinCS0)
        v02= readSpiADC(2,PinCLK,PinMOSI,PinMISO,PinCS0)
        v03= readSpiADC(3,PinCLK,PinMOSI,PinMISO,PinCS0)
        v04= readSpiADC(4,PinCLK,PinMOSI,PinMISO,PinCS0)
        v05= readSpiADC(5,PinCLK,PinMOSI,PinMISO,PinCS0)
        v06= readSpiADC(6,PinCLK,PinMOSI,PinMISO,PinCS0)
        v07= readSpiADC(7,PinCLK,PinMOSI,PinMISO,PinCS0)
        print("0: {0:4d} {1:4d} {2:4d} {3:4d} {4:4d} {5:4d} {6:4d} {7:4d}".format(v00,v01,v02,v03,v04,v05,v06,v07))
        time.sleep(0.2)
	
	power= (v00 -2048 )/16
	if power > 0:
		pi.write(pinDIR,1)
		pi.set_PWM_dutycycle(pinPWM,0)
	else:
		power = -power
		pi.write(pinDIR,0)
		pi.set_PWM_dutycycle(pinPWM,power)

	print(power)
except KeyboardInterrupt:
    pass

pi.write(pinDIR,0) 
pi.write(pinPWM,0) 
pi.stop()
