import cv2
import numpy as np
from time import sleep

### https://www.youtube.com/watch?v=oR71RSulTkQ

# rojo
red_low1=np.array([0,100,20],np.uint8)
red_low2=np.array([175,100,20],np.uint8)
red_hi1=np.array([8,255,255],np.uint8)
red_hi2=np.array([179,255,255],np.uint8)
# Verde
green_low=np.array([30,100,20],np.uint8)
green_hi=np.array([80,255,255],np.uint8)


cap = cv2.VideoCapture('Seleccionadora1.mp4')

def find_object(im, mask, color):
    cnts, hierarchy = cv2.findContours(mask, cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
    #cont, hierarchy = cv2.findContours(morpho(mask),cv2.RETR_LIST,cv2.CHAIN_APPROX_NONE) 
    #if 
    c = max(cnts, key=cv2.contourArea,default=1)

    x,y,w,h = cv2.boundingRect(c)
    cv2.rectangle(im,(x,y), (x+w,y+h), color,2)
    return (round(x+w/2),round(y+h/2))

while (cap.isOpened()):
    ret, im = cap.read()

    if ret == False:
        break


    hsv= cv2.cvtColor(im,cv2.COLOR_BGR2HSV)
    mask_hsv1=cv2.inRange(hsv,red_low1,red_hi1)
    mask_hsv2=cv2.inRange(hsv,red_low2,red_hi2)
    mask_hsv_r=cv2.add(mask_hsv1,mask_hsv2)

    mask_hsv_g=cv2.inRange(hsv,green_low,green_hi)
    print('ya saqué las mascaras')


    pb=find_object(im,mask_hsv_r,(0,0,255))


    cv2.imshow('Image',im)
    #cv2.imshow('Mask Red',mask_hsv_r)
    #cv2.imshow('Mask Green',mask_hsv_g)
    if cv2.waitKey(1) & 0xFF==27:
        break
    #sleep(0.03)


