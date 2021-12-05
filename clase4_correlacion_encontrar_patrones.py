import cv2
import numpy as np

def main():
	#cargar imagen
	img=cv2.imread("corr_norm.tif")
	templ = cv2.imread("modelo.tif")
	res = cv2.matchTemplate(img,templ,cv2.TM_SQDIFF)
	min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
	print (min_val, max_val, min_loc, max_loc)
	x1, y1 = min_loc
	x2,y2 = min_loc[0] + templ.shape[1], min_loc[1] + templ.shape[0]

	cv2.rectangle(img, (x1,y1), (x2,y2),(0,255,0),3)
	cv2.imshow('original',img)
	cv2.imshow('resultado',res)
	cv2.imshow('patron',templ)
	cv2.waitKey(0)
	cv2.destroyAllWindows()


if __name__ == '__main__':
	main()
