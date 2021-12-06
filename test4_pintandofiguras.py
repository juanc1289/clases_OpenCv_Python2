import numpy as np
import cv2


img = np.zeros((512,512,3),np.uint8)

img = cv2.line(img,(0,0),(511,511),(255,255,255),1)
img = cv2.circle(img,(447,63),65,(0,0,255),-1)  
img = cv2.ellipse(img,(256,250),(200,50),0,0,360,(0,255,0),1)

pts = np.array([[10,5],[200,30],[70,100],[50,50]], np.int32)
pts = pts.reshape((-1,1,2))
img = cv2.polylines(img,[pts],True,(255,255,255))

font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(img,'Ha',(100,500), font, 1.5,(0,255,0),2,cv2.LINE_AA)

#cv2.namedWindow('image', cv2.WINDOW_NORMAL)
cv2.imwshow('image.jpg',img)
cv2.imwrite('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()



