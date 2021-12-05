import cv2
import numpy as np

def main():
	#cargar imagen
	img=cv2.imread("ivvi_684x684_gray.jpg")
	#obtener pixel
	px=img[55,88]
	print (px);

	filas,columnas,canales = img.shape
	print (img.shape);
	for i in range(int(columnas/4),int(3*columnas/4)):
		for j in range(int(filas/4),int(3*filas/4)):
			img[j,i] = [255,0,0]
	cv2.imshow('resultado',img)
	cv2.waitKey(0)
	cv2.destroyAllWindows()


if __name__ == '__main__':
	main()
