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

	img= cv2.imread("../images/j2.png")
	img_g= cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
	kernel = np.ones((3,3), np.uint8)

	img_erosion = cv2.erode(img, kernel, iterations=1)
	img_dilation = cv2.dilate(img, kernel, iterations=1)
	img_d_e = cv2.dilate(img_erosion, kernel, iterations=1)
	img_e_d = cv2.erode(img_dilation, kernel, iterations=1)

	cv2.imshow('Input', img)
	cv2.imshow('Erosion', img_erosion)
	cv2.imshow('Dilation', img_dilation)
	cv2.imshow('Ed', img_d_e)
	cv2.imshow('De', img_e_d)
	#Regiones de Imagenes




	#Mostrar La imagen, esperar tecla para cerrar y destruir ventanas
	#cv2.imshow('gris',img_g)
	cv2.waitKey(0)
	cv2.destroyAllWindows()


	return


def unirImagenes():

	# Cargamos dos Imagenes las magenes deben mdir lo mismo en alto y ancho
	img1 = cv2.imread('/home/juan/Desktop/vision/Vision/imagenes/carro.jpg')
	img2 = cv2.imread('/home/juan/Desktop/vision/Vision/imagenes/logo.png')
	#print img1.shape
	# Optenemos el tamanio de la imagen del logo y obtenemos una region e la imagen carro del mismo tamanio
	filas,cols,canales = img2.shape
	area = img1[200:filas+200, 200:cols+200 ]


	b,g,r = cv2.split(img2)

	#r_gray = cv2.cvtColor(r,cv2.COLOR_BGR2GRAY)
	ret_g, mask_g = cv2.threshold(r, 200, 255, cv2.THRESH_BINARY)
	g_inv = cv2.bitwise_not(mask_g)

	ret_b, mask_b = cv2.threshold(g, 200, 255, cv2.THRESH_BINARY)
	b_inv = cv2.bitwise_not(mask_b)
	gb = cv2.bitwise_or(g_inv,g_inv,mask = b_inv)
	gb_inv = cv2.bitwise_not(gb)


	# Obtenemos la figura del logo sin colores
	img2gray = cv2.cvtColor(img2,cv2.COLOR_BGR2GRAY)
	ret, mask = cv2.threshold(img2gray, 10, 255, cv2.THRESH_BINARY)
	mask_inv = cv2.bitwise_not(mask)

	# Invertimos los colores
	img1_bg = cv2.bitwise_and(area,area,mask = gb)

	# obtenemos los colores de la imagen original
	img2_fg = cv2.bitwise_and(img2,img2,mask = gb_inv)

	# Anadimos los cambios a la imagen general
	dst = cv2.add(img1_bg,img2_fg)
	img1[200:filas+200, 200:cols+200  ] = dst

	cv2.imshow('res1',img1)
	cv2.waitKey(0)
	cv2.destroyAllWindows() ######################################################################
	b,g,r = cv2.split(img1)
	ret_g, mask_g = cv2.threshold(g, 100, 255, cv2.THRESH_BINARY)
	g_inv = cv2.bitwise_not(mask_g)

	ret_b, mask_b = cv2.threshold(r, 100, 255, cv2.THRESH_BINARY)
	b_inv = cv2.bitwise_not(mask_b)
	gb = cv2.bitwise_or(g_inv,g_inv,mask = b_inv)
	gb_inv = cv2.bitwise_not(gb)
	img_fg = cv2.bitwise_and(img1,img1,mask = gb_inv)

	cv2.imshow('res',dst)
	cv2.waitKey(0)
	cv2.destroyAllWindows()

	px = r[55,88]

	#img[100,100] = [255,255,255]

	print (px);


	print (r.shape)

	print (r.size)

	print (r.dtype)
	return






if __name__ == '__main__':
	main()
