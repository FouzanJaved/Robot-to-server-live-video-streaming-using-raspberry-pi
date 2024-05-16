# Server side code -----------------------

# Python recieving video background subtraction and contour find from motion in python 
and bcm cm of raspberry pi attached to it 



import cv2 
import urllib 
import numpy as np

stream = urllib.urlopen('http://192.168.43.45:8081/frame.mjpg')
bytes = ''

kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(3,3))
fgbg = cv2.bgsegm.createBackgroundSubtractorGMG()

while True:
    bytes += stream.read(1024)
    a = bytes.find('\xff\xd8')
    b = bytes.find('\xff\xd9')
    if a != -1 and b != -1:
        jpg = bytes[a:b+2]
        bytes = bytes[b+2:]
        i = cv2.imdecode(np.fromstring(jpg, dtype=np.uint8),  cv2.IMREAD_COLOR)
        cv2.imshow('i1', i)

        fgmask = fgbg.apply(i)
        fgmask = cv2.morphologyEx(fgmask, cv2.MORPH_OPEN, kernel)
        cv2.imshow('frame',fgmask)

        #finding white area
        gray = cv2.cvtColor(i,cv2.COLOR_BGR2GRAY)
        ret,gray = cv2.threshold(gray,127,255,0)
        gray2 = gray.copy()
        mask = np.zeros(gray.shape,np.uint8)
        contours, hier = cv2.findContours(gray,cv2.RETR_LIST,cv2.CHAIN_APPROX_SIMPLE)
        for cnt in contours:
            if 20000<cv2.contourArea(cnt)<50000:
                cv2.drawContours(i,[cnt],0,(0,255,0),2)
                cv2.drawContours(mask,[cnt],0,255,-1)
                print("got it")
        #new added

