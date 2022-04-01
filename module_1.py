import cv2
w, h = 640, 480
Cptr = cv2.VideoCapture(0)
Cptr.set(3, w)
Cptr.set(4, h)
while True:
    success, obj = c.read()
    cv2.imshow("Image", obj)
    cv2.waitKey(1)