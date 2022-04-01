import cv2
w, h = 640, 480
c = cv2.VideoCapture(0)
c.set(3, w)
c.set(4, h)
while True:

    success, img = c.read()
    img = findHands(img)
    lmList = findPosition(img)

    if len(lmList) != 0:
        x1, y1 = lmList[8][1:]
        x2, y2 = lmList[12][1:]
        print(x1, y1, x2, y2)

    cv2.imshow("Frame", obj)
    cv2.waitKey(1)