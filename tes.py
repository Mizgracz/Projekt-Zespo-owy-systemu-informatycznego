import sys
import pygame

pygame.init()
res = (1280, 720)
screen = pygame.display.set_mode(res)
screen.fill((255, 255, 255))

color_surface = pygame.Surface((100, 200))
color_surface.fill((255, 0, 0))

image1_surface = pygame.image.load("hex.png")
szerokosc_hex = 0
wysokosc_hex = 0
przesuniecie_x = 0
przesuniecie_y = 0
for j in range(0, 2):
    wysokosc_hex = 128 * j
    szerokosc_hex = 0
    przesuniecie_x += 60
    przesuniecie_y += -35
    for i in range(0, 11):
        # Utwórz nowy Surface z obramowaniem
        bordered_surface = pygame.Surface((image1_surface.get_width() + 4, image1_surface.get_height() + 4))
        bordered_surface.fill((0, 0, 0))
        # Narysuj oryginalny sześciokąt na nowym Surface
        bordered_surface.blit(image1_surface, (2, 2))
        # Nałóż nowy Surface na ekran w miejscu sześciokąta
        screen.blit(bordered_surface, (szerokosc_hex + przesuniecie_x, wysokosc_hex + przesuniecie_y))
        szerokosc_hex += 119

while True:
    for x in pygame.event.get():
        if x.type == pygame.QUIT:
            sys.exit(0)

    pygame.display.update()
