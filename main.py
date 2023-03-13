import sys
import random
import pygame


pygame.init()
res = (1280, 720)
screen = pygame.display.set_mode(res)
screen.fill((255, 255, 255))
clock = pygame.time.Clock()

# ticking
mainClock = pygame.time.Clock()

# zmienne

tekstury_path = 'tekstury//'
click=False

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
p_score = 1
wyb = True
pause = False




# interfejs
up_bar = pygame.Surface((1280, 30))
up_bar.fill("black")

# wczytanie tekstury
image1_surface = pygame.image.load(tekstury_path+"hex_trawa.png")
image2_surface = pygame.image.load(tekstury_path+"wioska.png")
image3_surface = pygame.image.load(tekstury_path+"las.png")
image4_surface = pygame.image.load(tekstury_path+"woda.png")
image5_surface = pygame.image.load(tekstury_path+"castle.png")
imageDEC_surface = pygame.image.load(tekstury_path+"ekran.png")
button1_surface = pygame.image.load(tekstury_path+"button1.png")
button2_surface = pygame.image.load(tekstury_path+"button2.png")
button3_surface = pygame.image.load(tekstury_path+"button3.png")
# tło meny pauzy
pause_surface = pygame.Surface((res[0]-100,res[1]-100), pygame.SRCALPHA)   # per-pixel alpha
#przycisku menu

#b = pygame.Rect(left, top, width, height)
button_play = pygame.Rect(res[0]/2-200/2,200,200,97)
button_option = pygame.Rect(res[0]/2-200/2, 310, 200, 78)
button_exit = pygame.Rect(res[0]/2-200/2, 420, 200, 78)
#button_option = pygame.Rect(centerW-ButtonW/2, ButtonPosition*(2+1), ButtonW, 50)
button_exit = pygame.Rect(res[0]/2-200/2, 530, 200, 100)

button_play_surface = pygame.image.load('GUI//play_button.png')
button_option_surface = pygame.image.load('GUI//option_button.png')
button_exit_surface = pygame.image.load('GUI//exit_button.png')


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

    up_bar.fill((0, 0, 0))
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
    obw = 0

    player_hex.fill((0, 0, 0, 0))

    for o in range(0, 6):
        wymiar_p.append((obramowanie_wymiary_x[o] + 535 + camx + obw, obramowanie_wymiary_y[o] + 294 + camy))

    pygame.draw.polygon(player_hex, (30, 224, 33, 110), wymiar_p)
    pygame.draw.polygon(player_hex, (255, 255, 255, 50), wymiar_p, 4)

    for o in range(0, 6):
        wymiar_p.pop()

    screen.blit(player_hex, (0, 0))


def decision():
    global m_score
    global a_score
    global wyb

    if wyb:

        dec_rect = imageDEC_surface.get_rect(center=(640, 360))
        button1_rect = button1_surface.get_rect(midleft=(670, 360))
        button2_rect = button2_surface.get_rect(midright=(610, 360))
        screen.blit(imageDEC_surface, dec_rect)
        screen.blit(button1_surface, button1_rect)
        screen.blit(button2_surface, button2_rect)
        colision = pygame.mouse.get_pos()
        mouse_pressed = pygame.mouse.get_pressed()
        if button1_rect.collidepoint(colision) and mouse_pressed[0]:

            m_score += 10
            wyb = False
        if button2_rect.collidepoint(colision) and mouse_pressed[0]:

            a_score += 10
            wyb = False


def turn():
    global wyb
    turn_rect = button3_surface.get_rect(center=(100, 600))
    screen.blit(button3_surface, turn_rect)
    colision = pygame.mouse.get_pos()
    mouse_pressed = pygame.mouse.get_pressed()
    if turn_rect.collidepoint(colision) and mouse_pressed[0]:

        wyb = True

font = pygame.font.SysFont(None, 30)

def draw_text(text, font, color, surface, x, y):
    textobj = font.render(text, 1, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)

def menu_pause():
    
    global pause
    global click
    pause_surface = pygame.Surface((res[0]-100,res[1]-100), pygame.SRCALPHA)   # per-pixel alpha
    pause_surface.fill((0,0,0,220))                         # notice the alpha value in the color
    
    screen.blit(pause_surface, (50,50))
    

    screen.blit(button_play_surface, button_play)
    screen.blit(button_option_surface, button_option)
    screen.blit(button_exit_surface, button_exit)

    while pause:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit(0)
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE and pause==False:
                    pause=True
                else:
                    pause=False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True
        mx, my = pygame.mouse.get_pos()
        if button_play.collidepoint((mx, my)):
            if click:
                click=False
                print('Play')
                #game()
        if button_option.collidepoint((mx, my)):
            if click:
                click=False
                print('Options')
                #options()
        if button_exit.collidepoint((mx, my)):
            if click:
                pygame.quit()
                sys.exit()

        pygame.display.update()
        mainClock.tick(60)
def game():
    click=False

def options():
    click=False

while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit(0)
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE and pause==False:
                pause=True
                menu_pause()
    draw()
    playe_hex()
    screen.blit(up_bar, (0, 0))
    score()
    decision()
    keyboard()
    mouse()
    turn()
    

    pygame.display.update()
    mainClock.tick(60)