import sys
import random
import pygame

pygame.init()
res = (1280, 720)
screen = pygame.display.set_mode(res)
screen.fill((255, 255, 255))
clock = pygame.time.Clock()

# ticking


# zmienne

wymiary = (100, 200)
szerokosc_hex = 0
wysokosc_hex = 0
przesuniecie_x = 0
przesuniecie_y = 0
obramowanie_wymiary_x = [58, 0, 0, 58, 119, 119]
obramowanie_wymiary_y = [0, 30, 97, 127, 97, 30]
wymiar_obramowania = []
m_score = 0
a_score = 0
p_score = 0


# interfejs
up_bar = pygame.Surface((1280, 30))
up_bar.fill("black")

# wczytanie tekstury
image1_surface = pygame.image.load("hex_trawa.png")
image2_surface = pygame.image.load("wioska.png")
image3_surface = pygame.image.load("las.png")
image4_surface = pygame.image.load("woda.png")
image5_surface = pygame.image.load("castle.png")
player_hex = pygame.Surface((1000, 1000), pygame.SRCALPHA)

wymiar_p = []
camx = 0
camy = 0

hex_surf = {}
hex_x = {}
hex_y = {}
hex_typ = {}
hex_num_x = 20
hex_num_y = 20
hex_num = (hex_num_x * hex_num_y)
licz = 0


for j in range(0, hex_num_y):

    wysokosc_hex = 128 * j
    szerokosc_hex = 0

    for i in range(hex_num_x):
        hex_x["hex", licz] = szerokosc_hex + przesuniecie_x
        hex_y["hex", licz] = wysokosc_hex + przesuniecie_y
        if szerokosc_hex == 595 and wysokosc_hex == 384:
            hex_surf["hex", licz] = 101
        else:
            hex_surf["hex", licz] = random.randint(0, 100)
        szerokosc_hex += 119
        licz += 1

    if j % 2 != 0:
        przesuniecie_x = 0
    else:
        przesuniecie_x += -60

    przesuniecie_y += -30


def draw():
    screen.fill((255, 255, 255))
    for d in range(0, hex_num):

        if hex_surf["hex", d] == 101:
            screen.blit(image5_surface, (hex_x["hex", d], hex_y["hex", d]))

        elif hex_surf["hex", d] < 20:
            screen.blit(image4_surface, (hex_x["hex", d], hex_y["hex", d]))

        elif 19 < hex_surf["hex", d] < 50:
            screen.blit(image3_surface, (hex_x["hex", d], hex_y["hex", d]))

        elif 101 > hex_surf["hex", d] > 95:
            screen.blit(image2_surface, (hex_x["hex", d], hex_y["hex", d]))

        else:
            screen.blit(image1_surface, (hex_x["hex", d], hex_y["hex", d]))


def mouse():
    global camy
    global camx
    mouse_x, mouse_y = pygame.mouse.get_pos()
    if mouse_y > 50:
        camy -= 5
        for MY1 in range(0, hex_num):
            hex_y["hex", MY1] -= 5

    if mouse_y < 720 - 50:
        camy += 5
        for MY2 in range(0, hex_num):
            hex_y["hex", MY2] += 5
    if mouse_x < 1280 - 50:
        camx += 5
        for MX1 in range(0, hex_num):
            hex_x["hex", MX1] += 5
    if mouse_x > 50:
        camx -= 5
        for MX2 in range(0, hex_num):
            hex_x["hex", MX2] -= 5


def keyboard():
    press = pygame.key.get_pressed()
    global camy
    global camx
    if press[pygame.K_RIGHT]:
        camx -= 5
        for KR in range(0, hex_num):
            hex_x["hex", KR] -= 5
    if press[pygame.K_LEFT]:
        camx += 5
        for KL in range(0, hex_num):
            hex_x["hex", KL] += 5
    if press[pygame.K_DOWN]:
        camy -= 5
        for KD in range(0, hex_num):
            hex_y["hex", KD] -= 5

    if press[pygame.K_UP]:

        camy += 5
        for KU in range(0, hex_num):
            hex_y["hex", KU] += 5


def score():

    # money
    money = pygame.font.Font(None, 25)

    money_score = money.render("Ilość Złota: " + str(m_score), False, "white")
    money_score.blit(screen, (1, 30))
    up_bar.blit(money_score, (0, 6))
    # wojsko
    army = pygame.font.Font(None, 25)

    army_score = army.render("Ilość Wojska: " + str(a_score), False, "white")
    army_score.blit(screen, (100, 300))
    up_bar.blit(army_score, (150, 6))

    # pola

    tiles_score = army.render("Ilość Posiadanych Pól: " + str(p_score), False, "white")
    tiles_score.blit(screen, (100, 300))
    up_bar.blit(tiles_score, (330, 6))


def playe_hex():
    obw = -119

    player_hex.fill((0, 0, 0, 0))
    for ob in range(0, 3):

        for o in range(0, 6):
            wymiar_p.append((obramowanie_wymiary_x[o] + 535 + camx + obw, obramowanie_wymiary_y[o] + 294 + camy))

        pygame.draw.polygon(player_hex, (30, 224, 33, 110), wymiar_p)
        pygame.draw.polygon(player_hex, (255, 255, 255, 50), wymiar_p, 4)

        for o in range(0, 6):
            wymiar_p.pop()

        obw += 119
    screen.blit(player_hex, (0, 0))


while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit(0)

    draw()
    playe_hex()
    screen.blit(up_bar, (0, 0))
    score()

    keyboard()
    mouse()

    pygame.display.update()
