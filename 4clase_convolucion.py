import numpy as np
import cv2



def main():

	#Cargar Imagen
	img= cv2.imread("../images/car4.png")

	#Obtener el pixel de
	px = img[555,888]

	#img[100,100] = [255,255,255]

	print (px);


	print (img.shape)

	print (img.size)

	print (img.dtype)

	#capas()
	#blending()
	region()
	#unirImagenes()
	#unirImagenes()

	return







def region():

	img= cv2.imread("../images/car3.png")

	b,g,r = cv2.split(img)

	kernel=np.ones((3,3), np.float32)/9
	kernel[0,0]=kernel[0,1]*-1
	kernel[1,0]=kernel[1,1]*-1
	kernel[2,0]=kernel[2,1]*-1
	kernel[0,1]=0
	kernel[1,1]=0
	kernel[2,1]=0

	print(kernel)
	dst = cv2.filter2D(img,-1,kernel)



	cv2.imshow('img',img)
	cv2.imshow('dst',dst)

	cv2.waitKey(0)
	cv2.destroyAllWindows()
	return

if __name__ == '__main__':
	main()
