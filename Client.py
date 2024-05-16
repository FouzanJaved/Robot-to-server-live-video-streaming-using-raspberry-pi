# Client side code -------------

# Here is the code to recieve the video. As the video is send in the format of MPEG so 
# it should be recieved in the same pattern

import cv2
import urllib 
import numpy as np

stream = urllib.urlopen('http://192.168.1.20:8081/frame.mjpg')
bytes = ''
while True:
    bytes += stream.read(1024)
    a = bytes.find('\xff\xd8')
    b = bytes.find('\xff\xd9')
    if a != -1 and b != -1:
        jpg = bytes[a:b+2]
        bytes = bytes[b+2:]
        i = cv2.imdecode(np.fromstring(jpg, dtype=np.uint8),  cv2.IMREAD_COLOR)
        cv2.imshow('i', i)
        if cv2.waitKey(1) == 27:
            exit(0)   
