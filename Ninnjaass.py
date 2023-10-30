import pygame
import random
import cv2
import mediapipe
import numpy
pygame.init()

dosya = cv2.VideoCapture(0)
dosya.set(cv2.CAP_PROP_FRAME_WIDTH, 720)
dosya.set(cv2.CAP_PROP_FRAME_HEIGHT, 400)

FPS = 30
saat = pygame.time.Clock()

genislik = 1280
yukseklik = 720

skor = 0
can = 5
deger = 5
deger_2 = 10

dx = random.choice([-1, 1])
dy = random.choice([-1, 1])

dx2 = random.choice([-1, 1])
dy2 = random.choice([-1, 1])

goruntu_yuzeyi = pygame.display.set_mode((genislik, yukseklik))

karakter = pygame.image.load("final_karakter.png")
karakter_koordinati = karakter.get_rect()

x = 500
y = 300

arka_plan = pygame.image.load("final_arka_plan.jpg")
arka_plan_koordinati = arka_plan.get_rect()
arka_plan_koordinati.topleft = (0, 0)

pizza = pygame.image.load("final_pizza.png")
pizza_koordinati = pizza.get_rect()
pizza_koordinati.center = (random.randint(50, genislik - 50), random.randint(50, yukseklik - 50))

dusman = pygame.image.load("final_dusman.png")
dusman_koordinati = dusman.get_rect()
dusman_koordinati.center = (random.randint(50, genislik - 50), random.randint(50, yukseklik - 50))

ses_efekti_1 = pygame.mixer.Sound("final_kazanma.wav")
ses_efekti_2 = pygame.mixer.Sound("final_yanma.mp3")
ses_efekti_3 = pygame.mixer.Sound("final_game_over.wav")

pygame.mixer.music.load("final_arka_ses.wav")
pygame.mixer.music.play(-1, 0.0)

el_model = mediapipe.solutions.hands
with el_model.Hands(min_tracking_confidence=0.5, min_detection_confidence=0.5) as el:
    while True:
        kontrol, webcam = dosya.read()
        yukseklik, genislik, kanal = webcam.shape
        rgb = cv2.cvtColor(webcam, cv2.COLOR_BGR2RGB)
        sonuc = el.process(rgb)
        if sonuc.multi_hand_landmarks:
            for hand_mark in sonuc.multi_hand_landmarks:
                for koordinat in el_model.HandLandmark:
                    mark = hand_mark.landmark[8]
                    x = int(mark.x * genislik)
                    y = int(mark.y * yukseklik)

        karakter_koordinati.center = (x, y)
        rgb = numpy.rot90(rgb)
        web_cam_goruntu_yuzeyi = pygame.surfarray.make_surface(rgb).convert()
        web_cam_goruntu_yuzeyi = pygame.transform.flip(web_cam_goruntu_yuzeyi, True, False)

        pizza_koordinati.x = pizza_koordinati.x + (deger * dx)
        pizza_koordinati.y = pizza_koordinati.y + (deger * dy)

        if pizza_koordinati.left < 0 or pizza_koordinati.right > genislik:
            dx = -1 * dx
        if pizza_koordinati.top < 0 or pizza_koordinati.bottom > yukseklik:
            dy = -1 * dy

        dusman_koordinati.x = dusman_koordinati.x + (deger * dx2)
        dusman_koordinati.y = dusman_koordinati.y + (deger * dy2)

        if dusman_koordinati.left < 0 or dusman_koordinati.right > genislik:
            dx2 = -1 * dx2
        if dusman_koordinati.top < 0 or dusman_koordinati.bottom > yukseklik:
            dy2 = -1 * dy2

        if pizza_koordinati.colliderect(karakter_koordinati):
            skor += 1
            ses_efekti_1.play()
            deger += 1
            pizza_koordinati.x = random.randint(50, genislik - 50)
            pizza_koordinati.y = random.randint(50, yukseklik - 50)

        if dusman_koordinati.colliderect(karakter_koordinati):
            can -= 1
            ses_efekti_2.play()
            dusman_koordinati.x = random.randint(50, genislik - 50)
            dusman_koordinati.y = random.randint(50, yukseklik - 50)

        if can == 0:
            goruntu_yuzeyi.blit(arka_plan, arka_plan_koordinati)
            ses_efekti_3.play()
            pygame.mixer.music.stop()
            pygame.display.update()
            durdu = True
            while durdu:
                for etkinlik in pygame.event.get():
                    if etkinlik.type == pygame.KEYDOWN:
                        if etkinlik.key == pygame.K_SPACE:
                            durdu = False
                            skor = 0
                            can = 5
                            pygame.mixer.music.play(-1, 0.0)

                    if etkinlik.type == pygame.QUIT:
                        durdu = False
                        durum = False

        goruntu_yuzeyi.blit(web_cam_goruntu_yuzeyi, (0, 0))
        goruntu_yuzeyi.blit(pizza, pizza_koordinati)
        goruntu_yuzeyi.blit(dusman, dusman_koordinati)
        goruntu_yuzeyi.blit(karakter, karakter_koordinati)

        pygame.display.update()
        saat.tick(FPS)
pygame.quit()