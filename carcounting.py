import cv2
import numpy as np
#cam=cv2.VideoCapture(3)
kernel=np.ones((5,5),np.uint8)
#cap = cv2.VideoCapture("/home/juan/Desktop/DJI_0024.MOV")
cap = cv2.VideoCapture("/home/juan/Desktop/carcount/OpenCV_3_Car_Counting_Visual_Basic-master/CarsDrivingUnderBridge.mp4")
#cap = cv2.VideoCapture(1)

ret1, frame1=cap.read()

while(True):
	ret2, frame2=cap.read()
	frame2_c=frame2.copy()
	frame1_g = cv2.cvtColor(frame1,cv2.COLOR_BGR2GRAY)
	frame2_g = cv2.cvtColor(frame2,cv2.COLOR_BGR2GRAY)

	frame1_g_b = cv2.GaussianBlur(frame1_g,(5,5),0)
	frame2_g_b = cv2.GaussianBlur(frame2_g,(5,5),0)

	frame_diff = cv2.absdiff(frame1_g_b,frame2_g_b)

	b,g,r = cv2.split(frame2)

	b1 = cv2.merge((b,g*0,r*0))
	g1 = cv2.merge((b*0,g,r*0))
	r1 = cv2.merge((b*0,g*0,r))
	bg = cv2.merge((b/100,g,r))
	#bg=(b+g)/2

	ret_th, frame_th = cv2.threshold(frame_diff, 20, 255, cv2.THRESH_BINARY)

	structuringElement3x3 = cv2.getStructuringElement(cv2.MORPH_RECT,(3,3))
	structuringElement5x5 = cv2.getStructuringElement(cv2.MORPH_RECT,(5,5))
	structuringElement7x7 = cv2.getStructuringElement(cv2.MORPH_RECT,(7,7))
	structuringElement9x9 = cv2.getStructuringElement(cv2.MORPH_RECT,(9,9))

	kernel = np.ones((5,5),np.uint8)

	for i in range(0,1):
		frame_th = cv2.dilate(frame_th,structuringElement9x9,iterations = 1)
		frame_th = cv2.dilate(frame_th,structuringElement9x9,iterations = 1)
		frame_th = cv2.erode(frame_th,structuringElement9x9,iterations = 1)
	next


	frame_th_c=frame_th
	frame_th_c,contours,hierarchy = cv2.findContours(frame_th_c,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
	cv2.drawContours(frame2_c,contours, -1, (0,0,255),1 )

	hull = [cv2.convexHull(cnt, returnPoints = True) for cnt in contours ]
	cv2.drawContours(frame2_c,hull, -1, (0,255,0),1 )



	#for cnt in contours
	#	hull = cv2.convexHull(cnt)
	#pass
	rangomax=np.array([50,255,50])
	rangomin=np.array([0,51,0])
	mascara=cv2.inRange(frame2,rangomin,rangomax)
	opening=cv2.morphologyEx(mascara,cv2.MORPH_OPEN, kernel)
	x,y,w,h=cv2.boundingRect(opening)
	cv2.rectangle(frame2,(x,y),(x+w,y+h),(0,255,0),3)
	cv2.circle(frame2,(x+w/2,y+h/2),5,(0,0,255),-1)

	#cv2.imshow('camara_R', r1)
	#cv2.imshow('camara_G', g1)
	#cv2.imshow('camara_B', b1)
	cv2.imshow('camara_G_B', frame2_c)
	frame1=frame2

	k=cv2.waitKey(1) & 0xFF
	if k==27:
		print len(contours);
		break
