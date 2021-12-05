import cv2
import numpy as np
from matplotlib import pyplot as plt

def main():
	#cargar imagen
	img=cv2.imread("ivvi_684x684.jpg")
	b,g,r = cv2.split(img)
	# create a mask
	mask = np.zeros(img.shape[:2], np.uint8)
	mask[100:img.shape[0]-100, 100:img.shape[1]-100] = 255
	masked_img = cv2.bitwise_and(img,img,mask = mask)
	# Calculate histogram with mask and without mask
	# Check third argument for mask
	hist_b = cv2.calcHist([img],[0],None,[256],[0,256])
	hist_mask = cv2.calcHist([img],[0],mask,[256],[0,256])
	hist_g = cv2.calcHist([img],[1],None,[256], [0,256])
	hist_r = cv2.calcHist([img],[2],None,[256], [0,256])
	plt.subplot(221), plt.imshow(img, 'gray')
	plt.subplot(222), plt.imshow(mask,'gray')
	plt.subplot(223), plt.imshow(masked_img, 'gray')
	plt.subplot(224), plt.plot(hist_b), plt.plot(hist_g), plt.plot(hist_r), plt.plot(hist_mask)
	plt.xlim([0,256])
	plt.show()


	#cv2.imshow('resultado',img)
	#cv2.waitKey(0)
	#cv2.destroyAllWindows()


if __name__ == '__main__':
	main()
