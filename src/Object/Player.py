import pygame


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("img/grouterW.png")
        self.surf = pygame.Surface((100, 100))
        self.rect = self.surf.get_rect(center=(200, 450))

    def move(self, speed):
        keys = pygame.key.get_pressed()

        if self.rect.left >= 0:
            if keys[pygame.K_LEFT]:
                self.rect.move_ip(-10, 0)
        if self.rect.left <= 420:
            if keys[pygame.K_RIGHT]:
                self.rect.move_ip(10, 0)

    def draw(self, surface):
        surface.blit(self.image, self.rect)


P = Player()
