import pygame
from pygame.locals import *
import random

# размер
size = width, height = (1200, 1000)
line_w = int(width / 1.6)
# линии
right_line = width / 2 + line_w / 4
left_line = width / 2 - line_w / 4
#скорость
speed = 5

pygame.init()
running = True

screen = pygame.display.set_mode(size)
pygame.display.set_caption("Messi simulator")
screen.fill((60, 220, 0))
pygame.display.update()

# фото
messi = pygame.image.load("messi.jpg")
messi_loc = messi.get_rect()
messi_loc.center = right_line, height * 0.8
ron = pygame.image.load("ron.jpg")
ron_loc = ron.get_rect()
ron_loc.center = left_line, height * 0.2

pitch = pygame.image.load("pitch.png")
pitch_loc = pitch.get_rect()
pitch_loc.center = width//2, height//2
counter = 0
k=1

while running:
    counter += 1

    # сложность
    if counter == 5000:
        speed += 0.15
        counter = 0

#движение
    ron_loc[1] += speed
    if ron_loc[1] > height:
        # randomly select line
        if random.randint(0, 1) == 0:
            ron_loc.center = right_line, -200
        else:
            ron_loc.center = left_line, -200

#проигрыш
    if messi_loc[0] == ron_loc[0] and ron_loc[1] > messi_loc[1] - 250:
        print("MESSI IS GOAT!")
        break

#бинд
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
        if event.type == KEYDOWN:
            # налево
            if event.key in [K_a, K_LEFT]:
                if(k==0):
                    continue
                else:
                    messi_loc = messi_loc.move([-int(line_w / 2), 0])
                    k=0
            #направо
            if event.key in [K_d, K_RIGHT]:
                if(k==1):
                    continue
                else:
                    messi_loc = messi_loc.move([int(line_w / 2), 0])
                    k=1

#вставка фото
    screen.blit(pitch, pitch_loc)
    screen.blit(messi, messi_loc)
    screen.blit(ron, ron_loc)
    pygame.display.update()
pygame.quit()