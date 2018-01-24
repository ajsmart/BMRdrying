import numpy as np
import serial

ser=serial.Serial('COM3',115200)
if ser.isOpen():
    ser.close()
    print 'com3 is closed'
else:
    print 'con3 already closed'