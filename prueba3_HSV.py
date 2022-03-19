import cv2
import numpy as np
from matplotlib import pyplot as plt

def main():

	img=cv2.imread("nada.jpg")
	img_v=cv2.imread("verde.jpg")
	img_r=cv2.imread("rojo.jpg")

	res_rojo = cv2.subtract(img_r,img)
	res_verde = cv2.subtract(img_v,img)


	red_low1=np.array([0,100,20],np.uint8)
	red_low2=np.array([175,100,20],np.uint8)
	red_hi1=np.array([8,255,255],np.uint8)
	red_hi2=np.array([179,255,255],np.uint8)

	r_hsv=cv2.cvtColor(img_r,cv2.COLOR_BGR2HSV)
	v_hsv=cv2.cvtColor(img_v,cv2.COLOR_BGR2HSV)

	mask_r_hsv1=cv2.inRange(r_hsv,red_low1,red_hi1)
	mask_r_hsv2=cv2.inRange(r_hsv,red_low2,red_hi2)
	mask_r_hsv=cv2.add(mask_r_hsv1,mask_r_hsv2)

	mask_v_hsv1=cv2.inRange(v_hsv,red_low1,red_hi1)
	mask_v_hsv2=cv2.inRange(v_hsv,red_low2,red_hi2)
	mask_v_hsv=cv2.add(mask_v_hsv1,mask_v_hsv2)


	contours_r, hierarchy = cv2.findContours(mask_r_hsv,cv2.RETR_LIST,cv2.CHAIN_APPROX_NONE)
	contours_v, hierarchy = cv2.findContours(mask_v_hsv,cv2.RETR_LIST,cv2.CHAIN_APPROX_NONE)
	cv2.drawContours(img_r,contours_r,-1,(0,0,255),2)
	cv2.drawContours(img_v,contours_v,-1,(0,0,255),2)


	cv2.imshow('HSV rojo',mask_r_hsv)
	cv2.imshow('HSV verde',mask_v_hsv)
	cv2.imshow('Original rojo',img_r)
	cv2.imshow('Original verde',img_v)


	cv2.waitKey(0)
	cv2.destroyAllWindows()


if __name__ == '__main__':
	main()
