
import cv2
import serial
import time
import io
import numpy as np

#para saber el puerto usar en linux 'ls /dev/tty*' /dev/ttyUSB0
arduino = serial.Serial(port='/dev/ttyUSB0',baudrate=115200, timeout=0.1)

def write_read(x):
	arduino.write(bytes(x, 'utf-8'))
	#arduino.flush()
	time.sleep(0.05)
	data = arduino.readline()
	return data

def main():
	#cargar imagen
	while(True):
		img=cv2.imread("rojo.jpg")
		num=input("ingrese un número:")
		value = write_read(num)
		print (value)

		cv2.imshow('resultado',img)
		#cv2.waitKey(0)
		#cv2.destroyAllWindows()
		k=cv2.waitKey(0) #& 0xFF
		if k==27:
			print ('bye');
			break


if __name__ == '__main__':
	main()
