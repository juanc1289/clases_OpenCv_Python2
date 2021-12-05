import numpy as np
import cv2

cap = cv2.VideoCapture("../2calle26.MOV")


fps = cap.get(cv2.CAP_PROP_FPS)
print("fps")
print(fps)

# module level variables ##########################################################################
GAUSSIAN_SMOOTH_FILTER_SIZE = (1, 1)
ADAPTIVE_THRESH_BLOCK_SIZE = 19
ADAPTIVE_THRESH_WEIGHT = 9
RESIZE_RATIO = 0.5
def main():

	region()


	return


def region():
    vel=int(1)
    #cap.set(cv2.CAP_PROP_POS_MSEC,9000)
    #cap.set(cv2.CAP_PROP_POS_MSEC,vel*10)
    #cap.set(cv2.CAP_PROP_POS_FRAMES,540+vel*2)
    cap.set(cv2.CAP_PROP_POS_FRAMES,379)
    ret1, frame=cap.read()
    (r, c) = frame.shape[:2]
    placa=frame[500+23:500+56,356:430]
    cv2.imshow('placa',placa)
    cap.set(cv2.CAP_PROP_POS_FRAMES,0)
    while(True):
        #cap.set(cv2.CAP_PROP_POS_MSEC,9000)
        #cap.set(cv2.CAP_PROP_POS_MSEC,vel*10)
        #cap.set(cv2.CAP_PROP_POS_FRAMES,540+vel*2)
        # cap.set(cv2.CAP_PROP_POS_FRAMES,379)
        ret1, frame=cap.read()
        (r, c) = frame.shape[:2]
        print(frame.shape)
        print("frame",cap.get(cv2.CAP_PROP_POS_FRAMES))
        img=frame[500:600,0:c]

        vel=vel+1

        gray=cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        patch=cv2.cvtColor(placa, cv2.COLOR_BGR2GRAY)
        result = cv2.matchTemplate(gray,patch,cv2.TM_CCOEFF_NORMED)
        result = np.abs(result)**3
        val, result = cv2.threshold(result, 0.01, 0, cv2.THRESH_TOZERO)
        result8 = cv2.normalize(result,None,0,255,cv2.NORM_MINMAX,cv2.CV_8U)

        ret_b, mask_b = cv2.threshold(result8, 240, 255, cv2.THRESH_BINARY)

        # img = cv2.resize(img, (int(c * RESIZE_RATIO), int(r * RESIZE_RATIO)), interpolation=cv2.INTER_CUBIC)
        # result8 = cv2.resize(result8, (int(c * RESIZE_RATIO), int(r * RESIZE_RATIO)), interpolation=cv2.INTER_CUBIC)
        cv2.imshow('img',img)
        cv2.imshow('mask_b',mask_b)


        cv2.imshow("result", result8)


        # cv2.waitKey(0)
        # cv2.destroyAllWindows()
        # break
        k=cv2.waitKey(1) & 0xFF
        if k==27:
            print (len("hi"))
            break
    return

if __name__ == '__main__':
	main()
