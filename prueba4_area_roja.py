import cv2
import numpy as np
from matplotlib import pyplot as plt

def main():

	#img=cv2.imread("nada.jpg")
	#img=cv2.imread("verde.jpg")
	img=cv2.imread("rojo.jpg")


	kernel = np.ones((9,9),np.uint8)

	red_low1=np.array([0,100,20],np.uint8)
	red_low2=np.array([175,100,20],np.uint8)
	red_hi1=np.array([8,255,255],np.uint8)
	red_hi2=np.array([179,255,255],np.uint8)

	hsv=cv2.cvtColor(img,cv2.COLOR_BGR2HSV)

	mask_hsv1=cv2.inRange(hsv,red_low1,red_hi1)
	mask_hsv2=cv2.inRange(hsv,red_low2,red_hi2)
	mask_hsv=cv2.add(mask_hsv1,mask_hsv2)

	#erode=cv2.erode(mask_hsv,kernel,iterations=2)
	#dilate=cv2.dilate(img,kernel,iterations=1)
	close=cv2.morphologyEx(mask_hsv,cv2.MORPH_CLOSE,kernel)
	open=cv2.morphologyEx(close,cv2.MORPH_OPEN,kernel)
	#gradient = cv2.morphologyEx(img,cv2.MORPH_GRADIENT,kernel)
	#tophat = cv2.morphologyEx(img,cv2.MORPH_TOPHAT,kernel)
	#blackhat = cv2.morphologyEx(img,cv2.MORPH_BLACKHAT,kernel)

	cont, hierarchy = cv2.findContours(open,cv2.RETR_LIST,cv2.CHAIN_APPROX_NONE)
	for c in cont:
		area=cv2.contourArea(c)
		print (area)
	cv2.drawContours(img,cont,-1,(0,0,255),2)


	cv2.imshow('Mask HSV',mask_hsv)
	cv2.imshow('Open Mask HSV',open)
	cv2.imshow('close Mask HSV',close)
	cv2.imshow('Original',img)
	cv2.waitKey(0)
	cv2.destroyAllWindows()


if __name__ == '__main__':
	main()
