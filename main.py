import cv2
import numpy as np
import HandModule as tool
import pyautogui
import time
import autopy

w, h = 640, 480
frame_reduction = 100
smooth = 9



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
    #mouse movement
    if fingers[1] == 1 and fingers[2] == 1 and fingers[3] == 0:

        x3 = np.interp(x1, (frame_reduction, w - frame_reduction), (0, wid))
        y3 = np.interp(y1, (frame_reduction, h - frame_reduction), (0, hei))

        modX = camX + (x3 - camX) / smooth
        modY = camY + (y3 - camY) / smooth

        autopy.mouse.move(wid - modX, modY)
        #cv2.circle(obj, (x1, y1), 15, (255, 0, 255), cv2.FILLED)
        camX, camY = modX, modY

    #mouse left click
    if fingers[1] == 1 and fingers[2] == 1:
        length, obj, lineInfo = detector.findDistance(4, 5, obj)

        if length < 45:
            cv2.circle(obj, (lineInfo[4], lineInfo[5]), 5, (0, 255, 0), cv2.FILLED)
            autopy.mouse.click()
            #pyautogui.click()

    #mouse right click

    if fingers[1] == 1 and fingers[2] == 1:
        length, obj, lineInfo = detector.findDistance(12, 9, obj)
        if length < 62:
            autopy.mouse.toggle(autopy.mouse.Button.RIGHT, False)

    #scroll wheel
    if fingers[1] == 1 and fingers[2] == 1:
        length, obj, lineInfo = detector.findDistance(8, 12, obj)
        #print(length)
        if length < 25:
            pyautogui.scroll(100)
        if length > 105:
            pyautogui.scroll(-100)



    #drag and drop
    if fingers[2] == 1 and fingers[3] == 0:
        length, obj, lineInfo = detector.findDistance(8, 5, obj)
        print(length)
        #if length < 30:
        #    pyautogui.mouseDown()
        #if length > :
        #    pyautogui.mouseUp()



    #pinch zoom in and out
    if fingers[2] == 0 and fingers[3] == 0 and fingers[4] == 1:
        length, obj, lineInfo = detector.findDistance(4, 8, obj)
        print(length)
        if length < 17:
            pyautogui.keyDown('ctrl')
            pyautogui.scroll(100)
            pyautogui.keyUp('ctrl')
        if length > 170:
            pyautogui.keyDown('ctrl')
            pyautogui.scroll(-100)
            pyautogui.keyUp('ctrl')

    




    cv2.imshow("Frame", obj)
    cv2.waitKey(1)

    if cv2.getWindowProperty('Frame', cv2.WND_PROP_VISIBLE) < 1:
        break