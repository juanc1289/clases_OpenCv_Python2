import cv2
import numpy as np

def main():
	#cargar imagen
	img=cv2.imread("Clase1.jpg")
	#img=cv2.imread("rojo.jpg")
	img_g=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
	ret, mask= cv2.threshold(img_g, 128,255,cv2.THRESH_BINARY)
	contours, hierarchy=cv2.findContours(mask,cv2.RETR_LIST,cv2.CHAIN_APPROX_NONE)

	cv2.drawContours(img,contours,-1,(0,0,255),1)

	#kernel = np.ones((3,3),np.uint8)
	#kernel2 = np.full((5,5),1/25)

	#erode=cv2.erode(img,kernel,iterations=1)
	#dilate=cv2.dilate(img,kernel,iterations=1)
	#close=cv2.morphologyEx(img,cv2.MORPH_CLOSE,kernel)
	#open=cv2.morphologyEx(img,cv2.MORPH_OPEN,kernel)
	#gradient = cv2.morphologyEx(img,cv2.MORPH_GRADIENT,kernel)
	#tophat = cv2.morphologyEx(img,cv2.MORPH_TOPHAT,kernel)
	#blackhat = cv2.morphologyEx(img,cv2.MORPH_BLACKHAT,kernel)


	cv2.imshow('original',img)
	#cv2.imshow('mask',mask)
	cv2.waitKey(0)
	cv2.destroyAllWindows()


if __name__ == '__main__':
	main()
