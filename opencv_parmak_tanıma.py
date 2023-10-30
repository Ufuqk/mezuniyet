import cv2
import mediapipe as mp

el_model = mp.solutions.hands

dosya = cv2.VideoCapture(0)

with el_model.Hands(min_tracking_confidence=0.5,min_detection_confidence=0.5) as el:
    while True:
        kontrol,webcam = dosya.read()
        yukseklik,genislik,kanal = webcam.shape
        rgb = cv2.cvtColor(webcam,cv2.COLOR_BGR2RGB)
        sonuc = el.process(rgb)
        if sonuc.multi_hand_landmarks:
            for hand_mark in sonuc.multi_hand_landmarks:
                for koordinat in el_model.HandLandmark:

                    mark = hand_mark.landmark[4]
                    x = int(mark.x*genislik)
                    y = int(mark.y*yukseklik)
                    cv2.circle(webcam,(x,y),5,(125,153,20),-1)


                    mark2 = hand_mark.landmark[8]
                    x2 = int(mark2.x * genislik)
                    y2 = int(mark2.y * yukseklik)
                    cv2.circle(webcam, (x2, y2), 5, (125, 153, 20), -1)

                    mark3 = hand_mark.landmark[12]
                    x3 = int(mark3.x * genislik)
                    y3 = int(mark3.y * yukseklik)
                    cv2.circle(webcam, (x3, y3), 5, (205, 53, 5), 10)
                    
                    mark4 = hand_mark.landmark[16]
                    x4 = int(mark4.x * genislik)
                    y4 = int(mark4.y * yukseklik)
                    cv2.circle(webcam, (x4, y4), 3, (13, 192, 16), 1)

                    mark5 = hand_mark.landmark[20]
                    x5 = int(mark5.x * genislik)
                    y5 = int(mark5.y * yukseklik)
                    cv2.rectangle(webcam, (x5, y5), (x5 + 7 ,y5 + 7), (125, 153, 20), 3)

        cv2.imshow("eloyunu", webcam)
        if cv2.waitKey(15) == 27:
            break