import pygame
import random

pygame.init()

genislik = 1000
yukseklik = 600

FPS = 30
saat = pygame.time.Clock()

karakter_ilk_cani = 5
karakter_hizi = 10
altin_ilk_hizi = 10
altin_ivmesi = .5
tampon_mesafesi = 100

skor = 0
karakter_cani = karakter_ilk_cani
altin_hizi = altin_ilk_hizi

yesil = (0, 255, 0)
koyu_yesil = (10, 50, 10)
beyaz = (255, 255, 255)
siyah = (0, 0, 0)

fonts = pygame.font.Font("AttackGraffiti.ttf",32)

skor_metni = fonts.render("SKOR:" + str(skor),True,yesil,beyaz)
skor_metni_koordinati = skor_metni.get_rect()
skor_metni_koordinati.topleft = (10,10)

oyun_basligi = fonts.render("EJDERAHIYI_BESLE",True,yesil,beyaz)
oyun_basligi_koordinati = oyun_basligi.get_rect()
oyun_basligi_koordinati.centerx = genislik//2
oyun_basligi_koordinati.y = 10

kalan_cani = fonts.render("CAN:" + str(karakter_cani),True,yesil,koyu_yesil )
kalan_cani_koordinati = kalan_cani.get_rect()
kalan_cani_koordinati.topright = (genislik-10,10)

oyun_bitti = fonts.render("OYUNBITTI",True,yesil,koyu_yesil)
oyun_bitti_koordinati = oyun_bitti.get_rect()
oyun_bitti_koordinati.center = (genislik//2,yukseklik//2)

yeniden_giris = fonts.render("ENTER TUSUNA BASINIZ",True,yesil,koyu_yesil)
yeniden_giris_koordinati = yeniden_giris.get_rect()
yeniden_giris_koordinati.center = (genislik//2,yukseklik//2 - 40)

altin_sesi = pygame.mixer.Sound("eb_altn_ses.wav")
yanma_sesi = pygame.mixer.Sound("eb_yanma_ses.wav")
yanma_sesi.set_volume(.1)
pygame.mixer.music.load("eb_arka_ses.wav")


goruntu_yuzeyi = pygame.display.set_mode((genislik,yukseklik))

karakter = pygame.image.load("eb_karakter.png")
karakter_koordinati = karakter.get_rect()
karakter_koordinati.topleft = (100,100)

altin = pygame.image.load("eb_altn.png")
altin_koordinati = altin.get_rect()
altin_koordinati.topleft = (genislik//2,yukseklik//2)

pygame.mixer.music.play(-1,0.0)

durum = True
while durum:
    for etkinlik in pygame.event.get():
        if etkinlik.type == pygame.QUIT:
            durum = False

    tus = pygame.key.get_pressed()
    if tus[pygame.K_UP] and karakter_koordinati.top > 64:
        karakter_koordinati.y = karakter_koordinati.y - karakter_hizi
    elif tus[pygame.K_DOWN] and karakter_koordinati.bottom < yukseklik:
        karakter_koordinati.y = karakter_koordinati.y + karakter_hizi

    if altin_koordinati.x < 0:
        karakter_cani = karakter_cani - 1
        yanma_sesi.play()
        altin_koordinati.x = genislik + tampon_mesafesi
    else:
        altin_koordinati.x = altin_koordinati.x - (altin_hizi + altin_ivmesi)

    if karakter_koordinati.colliderect(altin_koordinati):
        skor = skor + 1
        altin_sesi.play()
        altin_koordinati.x = genislik + tampon_mesafesi
        altin_koordinati.y = random.randint(64, yukseklik - 40)
        altin_hizi += altin_ivmesi
    skor_metni = fonts.render("SKOR:" + str(skor), True, yesil, beyaz)
    kalan_cani = fonts.render("CAN:" + str(karakter_cani), True, yesil, koyu_yesil)

    if karakter_cani == 0:
        goruntu_yuzeyi.blit(oyun_bitti,oyun_bitti_koordinati)
        goruntu_yuzeyi.blit(yeniden_giris,yeniden_giris_koordinati)
        pygame.display.update()

        pygame.mixer.music.stop()
        durdu = True
        while durdu:
            for etkinlik in pygame.event.get():
                if etkinlik.type == pygame.KEYDOWN:
                    skor = 0
                    karakter_cani = karakter_ilk_cani
                    altin_hizi = altin_ilk_hizi
                    karakter_koordinati.y = yukseklik // 2
                    pygame.mixer.music.play(-1,0.0)
                    durdu = False
                if etkinlik.type == pygame.QUIT:
                    durum = False
                    durdu = False


    goruntu_yuzeyi.fill((82, 139, 139))

    goruntu_yuzeyi.blit(skor_metni,skor_metni_koordinati)
    goruntu_yuzeyi.blit(oyun_basligi,oyun_basligi_koordinati)
    goruntu_yuzeyi.blit(kalan_cani,kalan_cani_koordinati)

    pygame.draw.line(goruntu_yuzeyi,beyaz,(0,64),(genislik,64),2)

    goruntu_yuzeyi.blit(karakter,karakter_koordinati)
    goruntu_yuzeyi.blit(altin,altin_koordinati)

    pygame.display.update()
    saat.tick(FPS)

pygame.quit()









































"""import pygame
import random

pygame.init()

#Functions
width = 1000
height = 750

karakter_ilk_can = 5
karakter_ilk_hiz = 10
gold_ilk_hiz = 10
gold_ivme = 0.5
tampon_mesafe = 100

FPS = 30
saat = pygame.time.Clock()


screen = pygame.display.set_mode((width, height))

karakter_hiz = karakter_ilk_hiz

skor = 0
karakter_can = karakter_ilk_can
gold_hiz = gold_ilk_hiz

yesil = (0, 255, 0)
koyu_yesil = (10, 50, 10)
beyaz = (255, 255, 255)
siyah = (0, 0, 0)

fonts = pygame.font.Font("AttackGraffiti.ttf", 36)

skor_metni = fonts.render("SKOR:" + str(skor), True, yesil, beyaz)
skor_metni_cor = skor_metni.get_rect()
skor_metni_cor.topleft = (10, 10)

oyun_baslık = fonts.render("EJDERHAYI BESLE", True, yesil, beyaz)
oyun_baslık_cor = oyun_baslık.get_rect()
oyun_baslık_cor.centerx = (width/2)
oyun_baslık_cor.y = 10

kalan_can = fonts.render("CAN:" + str(karakter_can), True, yesil, beyaz)
kalan_can_cor = kalan_can.get_rect()
kalan_can_cor.topright = (width -10, 10)

#sesler
gold_ses = pygame.mixer.Sound("eb_altn_ses.wav")
yanma_sesi = pygame.mixer.Sound("eb_yanma_ses.wav")
pygame.mixer.music.load("eb_arka_ses.wav")

karakter = pygame.image.load("eb_karakter.png")
karakter_cor = karakter.get_rect()
karakter_cor.topleft = (100, 100)

gold = pygame.image.load("eb_altn.png")
gold_cor = gold.get_rect()
gold_cor.center = (width/2, height/2 + 250)

pygame.mixer.music.play(-1, 0.0)












durum = True

while durum:
    for etkinlik in pygame.event.get():
        if etkinlik.type == pygame.QUIT:
            durum = False

    tus = pygame.key.get_pressed()
    if tus[pygame.K_UP] and karakter_cor.top > 64:
        karakter_cor.y -= karakter_hiz
    elif tus[pygame.K_DOWN] and karakter_cor.bottom < height\
            :
        karakter_cor.y += karakter_hiz




    screen.fill(siyah)
    screen.blit(skor_metni, skor_metni_cor)
    screen.blit(oyun_baslık, oyun_baslık_cor)
    screen.blit(kalan_can, kalan_can_cor)
    screen.blit(karakter, karakter_cor)
    screen.blit(gold, gold_cor)




    pygame.display.update()
    saat.tick(FPS)
pygame.quit()"""