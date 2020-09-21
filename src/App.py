import pygame, sys
from pygame.locals import *
import random

from src.Object.Player import P
from src.Object.Enemy import E

pygame.init()

FPS = 60
FramePerSecond = pygame.time.Clock()

WHITE = (255, 255, 255)

DISPLAYSURF = pygame.display.set_mode((500, 500))
DISPLAYSURF.fill(WHITE)
pygame.display.set_caption("OMEGALUL")


while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    P.update()
    E.move()

    DISPLAYSURF.fill(WHITE)
    P.draw(DISPLAYSURF)
    E.draw(DISPLAYSURF)

    pygame.display.update()
    FramePerSecond.tick(FPS)
