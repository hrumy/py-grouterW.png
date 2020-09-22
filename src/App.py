import pygame
import sys
import time
from pygame.locals import *

from src.Object.Player import P
from src.Object.Enemy import E

pygame.init()

FPS = 60
FramePerSecond = pygame.time.Clock()

WHITE = (255, 255, 255)
RED = (255, 0, 0)
font_small = pygame.font.SysFont("Verdana", 20)


SPEED = 5
SCORE = 0

DISPLAYSURF = pygame.display.set_mode((500, 500))
DISPLAYSURF.fill(WHITE)
pygame.display.set_caption("grouterW.png")

background = pygame.image.load("img/background.png")

INC_SPEED = pygame.USEREVENT + 1
pygame.time.set_timer(INC_SPEED, 1000)

all_sprites = pygame.sprite.Group()
all_sprites.add(P)
all_sprites.add(E)

enemies = pygame.sprite.Group()
enemies.add(E)

# Game loop
while True:

    for event in pygame.event.get():
        if event.type == INC_SPEED:
            SPEED += 0.5
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    DISPLAYSURF.blit(background, (0, 0))
    score = font_small.render(str(SCORE), True, RED)
    DISPLAYSURF.blit(score, (10, 10))

    # moves and draws all sprites
    for entity in all_sprites:
        DISPLAYSURF.blit(entity.image, entity.rect)
        if entity.move(SPEED):
            SCORE += 1

    if pygame.sprite.spritecollideany(P, enemies):
        DISPLAYSURF.fill(RED)
        pygame.display.update()

        for entity in all_sprites:
            entity.kill()
        time.sleep(2)
        pygame.quit()
        sys.exit()

    pygame.display.update()
    FramePerSecond.tick(FPS)
