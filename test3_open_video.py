import sys
import cv2
from matplotlib import pyplot as plt


img = cv2.imread('/home/juan/Desktop/OpenCV/samples/data/butterfly.jpg',0)
#cv2.imshow('Curso de Opencv', img)

#plt.imshow(img)
#plt.xticks([]), plt.yticks([])
#plt.show()

#cap = cv2.VideoCapture("/home/juan/Desktop/OpenCV/samples/data/vtest.avi")

cap = cv2.VideoCapture("/home/juan/Desktop/DJI_0024.MOV")

while(cap.isOpened()):
	ret,frame = cap.read()
	
	gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
	cv2.imshow('frame',gray)
	if cv2.waitKey(1) & 0xFF == ord('q'):
		break
cap.release()
cv2.destroyAllWindows()


def cerrarVentan():
	cv2.destroyAllWindows()
	sys.exit()

k= cv2.waitKey(0)
if k == 27:
	cerrarVentan()
elif k == ord ('s'):
	cv2.imwrite('home/juan/Desktop/mi.png',img)
	cerrarVentan()





