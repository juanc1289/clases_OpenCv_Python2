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

	img= cv2.imread("../images/1.png")

	b,g,r = cv2.split(img)
	invGamma = 1.0

	lut = np.array([(255-i )  for i in np.arange(0, 256)]).astype("uint8")		#negativo
	# lut = np.array([(pow(i*255,0.5) )  for i in np.arange(0, 256)]).astype("uint8")		#raiz cuadrada
	#lut = np.array([(pow(i,3)/(255*255) )  for i in np.arange(0, 256)]).astype("uint8")		#cubica
	print(lut)

	kernel = np.ones((5,5),np.float32)/25
	# for x in range(1, 256, 1):
	# 	lut[0,x]=x
	print(lut)
	img_inv = cv2.LUT(img, lut)
	b_inv = cv2.LUT(b, lut)
	#g_inv = cv2.LUT(g, lut)
	#r_inv = cv2.LUT(r, lut)
	cv2.imshow('b',b)
	cv2.imshow('b_inv',b_inv)
	cv2.imshow('img',img)
	cv2.imshow('img_inv',img_inv)

	cv2.waitKey(0)
	cv2.destroyAllWindows()


	return







if __name__ == '__main__':
	main()
