import pygame


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("img/grouterW.png")
        self.surf = pygame.Surface((67, 62))
        self.rect = self.surf.get_rect(center = (200, 450))

    def update(self):
        keys = pygame.key.get_pressed()

        if self.rect.left >= 0:
            if keys[pygame.K_LEFT]:
                self.rect.move_ip(-7, 0)
        if self.rect.left <= 430:  # possible bug
            if keys[pygame.K_RIGHT]:
                self.rect.move_ip(7, 0)

    def draw(self, surface):
        surface.blit(self.image, self.rect)


P = Player()
