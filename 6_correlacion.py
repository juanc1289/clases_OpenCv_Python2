import numpy as np
import cv2


RESIZE_RATIO = 0.5

def main():

	region()

	return

def region():

	cap = cv2.VideoCapture("../2calle26.MOV")
	cap.set(cv2.CAP_PROP_POS_FRAMES,540)
	ret1,img=cap.read()

	#img= cv2.imread("../images/car7.JPG")
	(h, w) = img.shape[:2]

	gray=cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
	#b,g,r = cv2.split(img)

	#placa2 = cv2.imread("../placa1.png")
	placa2=img[271*2:297*2,717*2:770*2]
	#placa=img[348:404,244:344]
	placa=img[349*2:371*2,191*2:237*2]
	cv2.imshow('placa',placa)
	cv2.imshow('placa2',placa2)
	patch=cv2.cvtColor(placa, cv2.COLOR_BGR2GRAY)
	result = cv2.matchTemplate(gray,patch,cv2.TM_CCOEFF_NORMED)
	result = np.abs(result)**3
	val, result = cv2.threshold(result, 0.01, 0, cv2.THRESH_TOZERO)
	result8 = cv2.normalize(result,None,0,255,cv2.NORM_MINMAX,cv2.CV_8U)


	img = cv2.resize(img, (int(w * RESIZE_RATIO), int(h * RESIZE_RATIO)), interpolation=cv2.INTER_CUBIC)
	result8 = cv2.resize(result8, (int(w * RESIZE_RATIO), int(h * RESIZE_RATIO)), interpolation=cv2.INTER_CUBIC)

	cv2.imshow("result", result8)
	cv2.imshow('img',img)

	cv2.waitKey(0)
	cv2.destroyAllWindows()
	return

if __name__ == '__main__':
	main()
