
import cv2
import serial
import time
import io
import numpy as np

 #v4l2-ctl --list-devices

#para saber el puerto usar en linux 'ls /dev/tty*' /dev/ttyUSB0
arduino = serial.Serial(port='/dev/ttyUSB1',baudrate=115200, timeout=0.1)

def write_read(x):
	arduino.write(bytes(x, 'utf-8'))
	#arduino.flush()
	time.sleep(0.05)
	data = arduino.readline()
	return data

def morpho(src):
	kernel = np.ones((3,3),np.uint8)
	open=cv2.morphologyEx(src,cv2.MORPH_OPEN,kernel)
	close=cv2.morphologyEx(open,cv2.MORPH_CLOSE,kernel)
	return close

def contours(mask,dst,col):
	if col == 'r':
		color=(0,0,255)
		clase='1'
	if col == 'v':
		color=(0,255,0)
		clase='0'
	cont, hierarchy = cv2.findContours(morpho(mask),cv2.RETR_LIST,cv2.CHAIN_APPROX_NONE)
	for c in cont:
		area=cv2.contourArea(c)
		print ('area:',area,'color',col)
		if area > 1000:
			value = write_read(clase)
			print ('arduino dice:',value);
			break
		#print ('area:',area)
	cv2.drawContours(dst,cont,-1,color,2)


def main():
	cap = cv2.VideoCapture(1)
	time.sleep(3)
	while(True):
		
		#cargar imagen
		#img=cv2.imread("rojo.jpg")
		
		value = write_read('2')
		print ('arduino dice:',value);
		time.sleep(2)
		ret,img1=cap.read()
		time.sleep(0.1)
		ret,img2=cap.read()
		time.sleep(0.1)
		ret,img3=cap.read()
		time.sleep(0.1)
		ret,img4=cap.read()
		time.sleep(0.1)
		ret,img=cap.read()
		#time.sleep(1)
		#ret,img=cap.read()
		cv2.imshow('camera',img)
		print('ya lei la camara')
		#num=input("ingrese un número:")
		#value = write_read(num)
		#print (value)
		#time.sleep(3)
		red_low1=np.array([0,100,20],np.uint8)
		red_low2=np.array([175,100,20],np.uint8)
		red_hi1=np.array([8,255,255],np.uint8)
		red_hi2=np.array([179,255,255],np.uint8)
		green_low=np.array([30,100,20],np.uint8)
		green_hi=np.array([80,255,255],np.uint8)

		hsv=cv2.cvtColor(img,cv2.COLOR_BGR2HSV)

		mask_hsv1=cv2.inRange(hsv,red_low1,red_hi1)
		mask_hsv2=cv2.inRange(hsv,red_low2,red_hi2)
		mask_hsv_r=cv2.add(mask_hsv1,mask_hsv2)

		mask_hsv_g=cv2.inRange(hsv,green_low,green_hi)
		print('ya saqué las mascaras')
		
		contours(morpho(mask_hsv_r),img,'r')
		contours(morpho(mask_hsv_g),img,'v')
		print('ya pinte contornos')

		cv2.imshow('Mask HSV verde',mask_hsv_g)
		cv2.imshow('Mask HSV roja',mask_hsv_r)
		#cv2.imshow('Open Mask HSV',open)
		#cv2.imshow('close Mask HSV_rojo',close)
		#cv2.imshow('close Mask HSV_verde',close_v)
		cv2.imshow('Original',img)
		#cv2.waitKey(0)
		#cv2.destroyAllWindows()


		#value = write_read(input("ingrese un número:"))
		#print ('arduino dice:',value);


		k=cv2.waitKey(0) #& 0xFF
		if k==27:
			print ('bye');
			break

if __name__ == '__main__':
	main()
