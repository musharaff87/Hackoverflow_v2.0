import cv2
import numpy as np
import HandModule as tool
import pyautogui
import time
import autopy

w, h = 640, 480
frame_reduction = 100
smooth = 7


pTime = 0
camX, camY = 0, 0
modX, modY = 0, 0


cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
cap.set(3, w)
cap.set(4, h)
detector = tool.handDetector(detectionCon=0.5, maxHands=1)
wid, hei = autopy.screen.size()

while True:
    success, obj = cap.read()
    obj = detector.findHands(obj)
    lmList = detector.findPosition(obj)
    if len(lmList) != 0:
        x1, y1 = lmList[8][1:]
        x2, y2 = lmList[12][1:]

    fingers = detector.fingersUp()

    if fingers[1] == 1 and fingers[2] == 1 and fingers[3] == 0:

        x3 = np.interp(x1, (frame_reduction, w - frame_reduction), (0, wid))
        y3 = np.interp(y1, (frame_reduction, h - frame_reduction), (0, hei))

        modX = camX + (x3 - camX) / smooth
        modY = camY + (y3 - camY) / smooth

        autopy.mouse.move(wid - modX, modY)
        #cv2.circle(obj, (x1, y1), 15, (255, 0, 255), cv2.FILLED)
        camX, camY = modX, modY


    if fingers[1] == 1 and fingers[2] == 1:
        length, obj, lineInfo = detector.findDistance(4, 5, obj)

        if length < 45:
            cv2.circle(obj, (lineInfo[4], lineInfo[5]), 5, (0, 255, 0), cv2.FILLED)
            #autopy.mouse.click()
            pyautogui.click()

    if fingers[1] == 1 and fingers[2] == 1:
        length, obj, lineInfo = detector.findDistance(12, 9, obj)
        if length < 62:
            cv2.circle(obj, (lineInfo[4], lineInfo[5]), 5, (0, 255, 0), cv2.FILLED)
            #autopy.mouse.toggle(autopy.mouse.Button.RIGHT, False)
            pyautogui.keyDown("win")
            pyautogui.keyDown("ctrl")
            pyautogui.press("o", presses=1)
            pyautogui.keyUp("win")
            pyautogui.keyUp("ctrl")

    cv2.imshow("Mouse", obj)
    cv2.waitKey(1)

    if cv2.getWindowProperty('Mouse', cv2.WND_PROP_VISIBLE) < 1:
        break