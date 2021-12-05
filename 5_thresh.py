import numpy as np
import cv2

cap = cv2.VideoCapture("../calle26.MOV")
cap.set(cv2.CAP_PROP_POS_MSEC,9000)

fps = cap.get(cv2.CAP_PROP_FPS)
print("fps")
print(fps)

# module level variables ##########################################################################
GAUSSIAN_SMOOTH_FILTER_SIZE = (1, 1)
ADAPTIVE_THRESH_BLOCK_SIZE = 19
ADAPTIVE_THRESH_WEIGHT = 9
RESIZE_RATIO = 0.5
def main():

	#Cargar Imagen
	#cap.set(cv2.CAP_PROP_FPS,1)
	#length = int(vidcap.get(cv2.CAP_PROP_FRAME_COUNT))

	img= cv2.imread("../images/car3.png")

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
	#unirImagenes120

	return


def region():
	vel=int(1)

	while(True):

		#cap.set(cv2.CAP_PROP_POS_MSEC,vel*10)
		#cap.set(cv2.CAP_PROP_POS_FRAMES,540+vel*2)
		ret1, frame1=cap.read()
		(h, w) = frame1.shape[:2]
		vel=vel+1




		img = cv2.cvtColor(frame1,cv2.COLOR_BGR2GRAY)

		#img= cv2.imread("../images/car3.png")

		b,g,r = cv2.split(frame1)

		kernel=np.ones((3,3), np.float32)/9
		kernel[0,0]=kernel[0,1]*-1
		kernel[1,0]=kernel[1,1]*-1
		kernel[2,0]=kernel[2,1]*-1
		kernel[0,1]=0
		kernel[1,1]=0
		kernel[2,1]=0

		print(kernel)

		dst = cv2.filter2D(img,-1,kernel)

		imgThresh = cv2.adaptiveThreshold(b, 255.0, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, ADAPTIVE_THRESH_BLOCK_SIZE, ADAPTIVE_THRESH_WEIGHT)


		img = cv2.resize(img, (int(w * RESIZE_RATIO), int(h * RESIZE_RATIO)), interpolation=cv2.INTER_CUBIC)
		dst = cv2.resize(dst, (int(w * RESIZE_RATIO), int(h * RESIZE_RATIO)), interpolation=cv2.INTER_CUBIC)
		imgThresh = cv2.resize(imgThresh, (int(w * RESIZE_RATIO), int(h * RESIZE_RATIO)), interpolation=cv2.INTER_CUBIC)
		cv2.imshow('img',img)
		cv2.imshow('dst',dst)
		cv2.imshow('imgThresh',imgThresh)

		#cv2.waitKey(0)
		#cv2.destroyAllWindows()
		k=cv2.waitKey(1) & 0xFF
		if k==27:
			print (len("hi"));
			break
	return

if __name__ == '__main__':
	main()
