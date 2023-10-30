"""resim = cv2.imread("alpler.jpg")
print(resim)
cv2.imshow("daglar",resim)
cv2.waitKey(0)
print(resim)
cv2.imshow("daglar",resim)
cv2.waitKey(0)

import cv2

resim = cv2.imread("alpler.jpg")
size = cv2.resize(resim,(1200,600))
cv2.imshow("daglar", size)
cv2.waitKey(0)"""

"""
import cv2
resim = cv2.imread("alplar.jpg")
cv2.line(resim,(60,60),(250,250),(100,200,200),5)
cv2.circle(resim,(500,500),100,(200,100,201),-1)
cv2.rectangle(resim,(0,250),(150,400),(104,55,76),-1)
cv2.imshow("orj",resim)
cv2.waitKey(0)"""

"""
import cv2
cap = cv2.VideoCapture("video.mp4")

while True:
    control, video = cap.read()

    cv2.imshow("video.mp4", video)
    if cv2.waitkey(100) == 27:
        break"""
"""
import cv2

cap = cv2.VideoCapture(0)
while True:
    control, webcam = cap.read()
    cv2.imshow("webcam",webcam)
    gri = cv2.cvtColor(webcam, cv2.COLOR_BGR2GRAY)
    cv2.imshow("gri",gri)
    if cv2.waitKey(100) == 27:
        break"""

import cv2
import mediapipe

el_model = mediapipe.solutions.hands
el_cizim = mediapipe.solutions.drawing_utils

dosya = cv2.VideoCapture(0)

with el_model.Hands(min_tracking_confidence = 0.5, min_detection_confidence = 0.5) as el:
    while True:
        control, webcam = dosya.read()
        rgb =cv2.cvtColor(webcam, cv2.COLOR_BGR2RGB)
        sonuc = el.process(rgb)
        if sonuc.multi_hand_landmarks:
            for hand_landmark in sonuc.multi_hand_landmarks:
                el_cizim.draw_landmarks(webcam,hand_landmark,el_model.HAND_CONNECTIONS)


        cv2.imshow("elmodelim",webcam)
        if cv2.waitKey(150) == 27:
            break

















