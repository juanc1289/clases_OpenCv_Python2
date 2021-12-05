import cv2
import numpy as np

def main():
	#cargar imagen
	img1=cv2.imread("nada.jpg")
	img2=cv2.imread("rojo.jpg")
	#obtener pixe
	res=cv2.subtract(img2,img1)
	#res2=cv2.absdiff(img2,img1)
	#res2= cv2.adaptiveThreshold(cv2.cvtColor(img2,cv2.COLOR_BGR2GRAY), 255.0, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, 19, 9)
	gris=cv2.cvtColor(res,cv2.COLOR_BGR2GRAY)
	ret, mask= cv2.threshold(gris, 80,255,cv2.THRESH_BINARY)
	cv2.imshow('img1',img1)
	cv2.imshow('img2',img2)
	cv2.imshow('gris',gris)
	cv2.imshow('resultado',res)
	cv2.imshow('mascara',mask)

	cv2.waitKey(0)
	cv2.destroyAllWindows()


if __name__ == '__main__':
	main()
