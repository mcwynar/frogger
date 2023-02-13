import pygame

class Player(pygame.sprite.Sprite):
    def __init__(self, position, groups):
        super().__init__(groups)
        self.image = pygame.Surface((50,50))
        self.image.fill('red')
        self.rect = self.image.get_rect(center=position)

    def input(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w] or keys[pygame.K_UP]:
            print('up')
        if keys[pygame.K_s] or keys[pygame.K_DOWN]:
            print('down')
        if keys[pygame.K_a] or keys[pygame.K_LEFT]:
            print('left')
        if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
            print('right')

    def update(self):
        self.input()