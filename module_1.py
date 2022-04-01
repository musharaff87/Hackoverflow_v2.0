import cv2
w, h = 640, 480
c = cv2.VideoCapture(0)
c.set(3, w)
c.set(4, h)
while True:
    success, obj = c.read()
    cv2.imshow("Image", obj)
    cv2.waitKey(1)