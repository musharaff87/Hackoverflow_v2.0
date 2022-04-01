import cv2
import numpy as np
import HandModule as tool
import pyttsx3
import pyautogui
import time
import autopy

engine=pyttsx3.init('sapi5')
rate = engine.getProperty('rate')
voices = engine.setProperty('rate',170)
voices=engine.getProperty('voices')
engine.setProperty('voice','voices[0].id')

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

def speak(text):
    engine.say(text)
    engine.runAndWait()




while True:
    success, obj = cap.read()
    obj = detector.findHands(obj)
    lmList = detector.findPosition(obj)
    if len(lmList) != 0:
        x1, y1 = lmList[8][1:]
        x2, y2 = lmList[12][1:]

    fingers = detector.fingersUp()


    if fingers[2] == 1 and fingers[3] == 1 and fingers[4] == 1:
        length, obj, lineInfo = detector.findDistance(8, 4, obj)
        #print(length)

        if length < 20:
            pyautogui.keyDown("win")
            pyautogui.keyDown("ctrl")
            pyautogui.press("o", presses=1)
            pyautogui.keyUp("win")
            pyautogui.keyUp("ctrl")
            #pyautogui.hotkey('win','ctrl','o',presses=1)
            #speak("Okay")
            #time.sleep(2)


    #if fingers[1] == 1 and fingers[2] == 1:
    #    length, obj, lineInfo = detector.findDistance(20, 0, obj)
        #print(length)
    #    length1, obj, lineInfo = detector.findDistance(14, 4, obj)
        #print(length1)

    #    if (length < 50 and length1 < 25):

    #        speak("peace out")
    #        time.sleep(2)



    cv2.imshow("Mouse", obj)
    cv2.waitKey(1)

    if cv2.getWindowProperty('Mouse', cv2.WND_PROP_VISIBLE) < 1:
        break















'''import cv2
import numpy as np
import HandModule as tool
import pyttsx3
import time
import autopy

engine=pyttsx3.init('sapi5')
rate = engine.getProperty('rate')
voices = engine.setProperty('rate',170)
voices=engine.getProperty('voices')
engine.setProperty('voice','voices[0].id')

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

def speak(text):
    engine.say(text)
    engine.runAndWait()




while True:
    success, obj = cap.read()
    obj = detector.findHands(obj)
    lmList = detector.findPosition(obj)
    if len(lmList) != 0:
        x1, y1 = lmList[8][1:]
        x2, y2 = lmList[12][1:]

    fingers = detector.fingersUp()


    if fingers[2] == 1 and fingers[3] == 1 and fingers[4] == 1:
        length, obj, lineInfo = detector.findDistance(8, 4, obj)
        #print(length)

        if length < 20:
            #speak("Okay")

            time.sleep(1)


    if fingers[1] == 1 and fingers[2] == 1:
        length, obj, lineInfo = detector.findDistance(20, 0, obj)
        #print(length)
        length1, obj, lineInfo = detector.findDistance(14, 4, obj)
        #print(length1)

        if (length < 50 and length1 < 25):

            speak("peace out")
            time.sleep(1)


    cv2.imshow("Mouse", obj)
    cv2.waitKey(1)

    if cv2.getWindowProperty('Mouse', cv2.WND_PROP_VISIBLE) < 1:
        break'''