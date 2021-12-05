import cv2
import numpy as np
from matplotlib import pyplot as plt

def main():

	img=cv2.imread("nada.jpg")
	img_v=cv2.imread("verde.jpg")
	img_r=cv2.imread("rojo.jpg")

	res_rojo = cv2.subtract(img_r,img)
	res_verde = cv2.subtract(img_v,img)

	ret, mask_r= cv2.threshold(cv2.cvtColor(res_rojo,cv2.COLOR_BGR2GRAY), 80,255,cv2.THRESH_BINARY)
	ret, mask_v= cv2.threshold(cv2.cvtColor(res_verde,cv2.COLOR_BGR2GRAY), 80,255,cv2.THRESH_BINARY)

	#masked_img_r = cv2.bitwise_and(img_r,img_r,mask = mask_r)
	#masked_img_v = cv2.bitwise_and(img_v,img_v,mask = mask_v)

	R_b,R_g,R_r = cv2.split(img_r)
	V_b,V_g,V_r = cv2.split(img_v)
	histR_b = cv2.calcHist([R_b],[0],mask_r,[256],[0,256])
	histR_g = cv2.calcHist([R_g],[0],mask_r,[256], [0,256])

	histR_r = cv2.calcHist([R_r],[0],mask_r,[256], [0,256])

	histV_b = cv2.calcHist([V_b],[0],mask_v,[256],[0,256])
	histV_g = cv2.calcHist([V_g],[0],mask_v,[256], [0,256])

	histV_r = cv2.calcHist([V_r],[0],mask_v,[256], [0,256])


	plt.subplot(231), plt.plot(histR_b)
	plt.subplot(232), plt.plot(histR_g)
	plt.subplot(233), plt.plot(histR_r)

	plt.subplot(234), plt.plot(histV_b)
	plt.subplot(235), plt.plot(histV_g)
	plt.subplot(236), plt.plot(histV_r)
	plt.xlim([0,256])
	plt.show()

	plt.subplot(231), plt.imshow(R_b,'gray')
	plt.subplot(232), plt.imshow(R_g,'gray')
	plt.subplot(233), plt.imshow(R_r,'gray')

	plt.subplot(234), plt.imshow(V_b,'gray')
	plt.subplot(235), plt.imshow(V_g,'gray')
	plt.subplot(236), plt.imshow(V_r,'gray')
	plt.show()


	#cv2.imshow('mascara rojo',masked_img_r)
	#cv2.imshow('mascara verde',masked_img_v)
	cv2.imshow('mascara rojo',R_r)


	cv2.waitKey(0)
	cv2.destroyAllWindows()


if __name__ == '__main__':
	main()
