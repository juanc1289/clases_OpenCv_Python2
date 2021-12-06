import numpy as np
import cv2

cap = cv2.VideoCapture(1)




while(True):

	ret1, frame1=cap.read()
	# Cargamos dos Imagenes las magenes deben mdir lo mismo en alto y ancho
	img1 = frame1
	#img1 = cv2.imread('/home/juan/Desktop/vision/Vision/imagenes/carro.jpg')
	img2 = cv2.imread('/home/juan/Desktop/vision/Vision/imagenes/logo.png')
	#print img1.shape
	# Optenemos el tamanio de la imagen del logo y obtenemos una region e la imagen
 # carro del mismo tamanio
	filas,cols,canales = img2.shape
	#area = img1[100:filas+300, 100:cols+300 ]
	area = img1[filas, cols ]
	img2 = img1[100:filas+300, 100:cols+300 ]


	#b,g,r = cv2.split(img2)
	b,g,r = cv2.split(img1)

	#r_gray = cv2.cvtColor(r,cv2.COLOR_BGR2GRAY)


	cv2.imshow('img1',img1)
	ret_g, mask_g = cv2.threshold(b, 90, 255, cv2.THRESH_BINARY)
	g_inv = cv2.bitwise_not(mask_g)

	ret_b, mask_b = cv2.threshold(g, 90, 255, cv2.THRESH_BINARY)
	b_inv = cv2.bitwise_not(mask_b)

	ret_r, mask_r = cv2.threshold(r, 90, 255, cv2.THRESH_BINARY)
	r_inv = cv2.bitwise_not(mask_r)

	cv2.imshow('mask_g',mask_g)
	cv2.imshow('mask_b',mask_b)
	cv2.imshow('mask_r',mask_r)

	cv2.imshow('g_inv',g_inv)
	cv2.imshow('b_inv',b_inv)
	cv2.imshow('r_inv',r_inv)

	gb = cv2.bitwise_or(g_inv,g_inv,mask = b_inv)
	gb_t = cv2.bitwise_and(gb,gb,mask = mask_r)
	gb_inv = cv2.bitwise_not(gb_t)	#todo lo rojo se queda en cero


#	ret,gb = cv2.threshold(r, 30, 255, cv2.THRESH_BINARY)
#	gb_inv = cv2.bitwise_not(gb)

	# Obtenemos la figura del logo sin colores
	img2gray = cv2.cvtColor(img2,cv2.COLOR_BGR2GRAY)
	ret, mask = cv2.threshold(img2gray, 10, 255, cv2.THRESH_BINARY)
	mask_inv = cv2.bitwise_not(mask)

	rs = cv2.bitwise_and(r,r,mask = gb_inv)
	rs_2= cv2.merge((b,g,rs))
	# Invertimos los colores
	##img1_bg = cv2.bitwise_and(area,area,mask = gb_inv)

	# obtenemos los colores de la imagen original
	##img2_fg = cv2.bitwise_and(img2,img2,mask = gb_t)

	# Anadimos los cambios a la imagen general
	##dst = cv2.add(img1_bg,img2_fg)
	#img1[100:filas+300, 100:cols+300  ] = rs_2


	#cv2.imshow('gb',gb)
	#cv2.imshow('gb_inv',gb_inv)
	#cv2.imshow('mask_r',mask_r)
	#cv2.imshow('rs_2',rs_2)
	#cv2.imshow('gb_t',gb_t)
	#cv2.imshow('img1',img1)
######################################################################


	#cv2.imshow('res',img1_bg	)


	px = r[55,88]

	#img[100,100] = [255,255,255]


	k=cv2.waitKey(1) & 0xFF
	if k==27:
		print (len(contours));
		break
