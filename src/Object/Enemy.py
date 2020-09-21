import pygame
import random


class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("img/win.png")
        self.surf = pygame.Surface((50, 50))
        self.rect = self.surf.get_rect(center=(random.randint(40, 360), 0))

    def move(self, speed):
        self.rect.move_ip(0, speed)
        if self.rect.bottom > 600:
            self.rect.top = 0
            self.rect.center = (random.randint(30, 370), 0)

    def draw(self, surface):
        surface.blit(self.image, self.rect)


E = Enemy()
