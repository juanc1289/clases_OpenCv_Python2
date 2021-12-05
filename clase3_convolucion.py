import cv2
import numpy as np

def main():
	#cargar imagen
	img=cv2.imread("verde.jpg")
	#obtener pixel

	kernel1 = np.array([[-1/9,0,1/9],[-1/9,0,1/9],[-1/9,0,1/9]]) #este deriva
	kernel2 = np.full((5,5),1/25) #este halla los bordes
	print (kernel2);
	result = cv2.filter2D(img,-1,kernel1)
	cv2.imshow('original',img)
	cv2.imshow('resultado',result)
	cv2.waitKey(0)
	cv2.destroyAllWindows()


if __name__ == '__main__':
	main()
