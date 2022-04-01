import cv2
w, h = 640, 480
cap = cv2.VideoCapture(0)
cap.set(3, w)
cap.set(4, h)
while True:
    success, img = cap.read()
    cv2.imshow("Image", img)
    cv2.waitKey(1)