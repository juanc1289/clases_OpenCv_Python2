import cv2
import numpy as np

def main():
	#cargar imagen
	img=cv2.imread("LetrasI_BW.jpg")
	kernel = np.ones((3,3),np.uint8)
	kernel2 = np.full((5,5),1/25)

	erode=cv2.erode(img,kernel,iterations=1)
	dilate=cv2.dilate(img,kernel,iterations=1)
	close=cv2.morphologyEx(img,cv2.MORPH_CLOSE,kernel)
	open=cv2.morphologyEx(img,cv2.MORPH_OPEN,kernel)
	gradient = cv2.morphologyEx(img,cv2.MORPH_GRADIENT,kernel)
	tophat = cv2.morphologyEx(img,cv2.MORPH_TOPHAT,kernel)
	blackhat = cv2.morphologyEx(img,cv2.MORPH_BLACKHAT,kernel)


	cv2.imshow('original',img)
	cv2.imshow('erode',erode)
	cv2.imshow('dilate',dilate)
	cv2.imshow('open',open)
	cv2.imshow('close',close)
	cv2.imshow('gradient',gradient)
	cv2.imshow('tophat',tophat)
	cv2.imshow('black hat',blackhat)

	cv2.waitKey(0)
	cv2.destroyAllWindows()


if __name__ == '__main__':
	main()
