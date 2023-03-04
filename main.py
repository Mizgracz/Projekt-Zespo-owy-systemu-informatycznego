import sys
import random
import pygame
pygame.init()
res = (1280, 720)
screen = pygame.display.set_mode(res)
screen.fill((255,255,255))

#zmienne
wymiary = (100,200)
szerokosc_hex = 0
wysokosc_hex = 0
przesuniecie_x = 0
przesuniecie_y = 0
obramowanie_wymiary_x = [58,0,0,58,119,119]
obramowanie_wymiary_y = [0,30,97,127,97,30]
wymiar_obramowania = []




#wczytanie tekstury
image1_surface = pygame.image.load("hex.png")
image2_surface = pygame.image.load("hex2.png")
image3_surface = pygame.image.load("forest.png")
image4_surface = pygame.image.load("hex4.png")
def obramowanie():
    for o in range(0, 6):
        wymiar_obramowania.append((obramowanie_wymiary_x[o] + szerokosc_hex + przesuniecie_x, obramowanie_wymiary_y[o] + wysokosc_hex + przesuniecie_y))

    pygame.draw.polygon(screen, (20, 20, 20), wymiar_obramowania, 2)

    for i in range(0, 6):
        wymiar_obramowania.pop()




#umieszczanie hexów
for j in range(0,7):
    wysokosc_hex = 128 * j
    szerokosc_hex = 0


    for i in range (0,10):
        x = random.randint(0,100)
        if x > 80:
            screen.blit(image4_surface, (szerokosc_hex + przesuniecie_x, wysokosc_hex + przesuniecie_y) )


        elif x > 50 and x < 80 :


            screen.blit(image1_surface, (szerokosc_hex + przesuniecie_x, wysokosc_hex + przesuniecie_y) )



        elif x > 40 and x < 61:
            screen.blit(image3_surface, (szerokosc_hex + przesuniecie_x, wysokosc_hex + przesuniecie_y))
        else :
            screen.blit(image2_surface, (szerokosc_hex + przesuniecie_x, wysokosc_hex + przesuniecie_y))
        obramowanie()

        szerokosc_hex += 119

    if j%2 != 0 :
        przesuniecie_x = 0
    else:
        przesuniecie_x += -60

    przesuniecie_y += -30








while True:
    for x in pygame.event.get():
        if x.type == pygame.QUIT:
            sys.exit(0)





    pygame.display.update()
