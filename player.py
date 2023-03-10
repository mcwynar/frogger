import pygame


class Player(pygame.sprite.Sprite):
    def __init__(self, position, groups):
        super().__init__(groups)

        self.import_assets()
        self.frame_index = 0
        self.image = self.animation[self.frame_index]
        self.rect = self.image.get_rect(center=position)

        # float based movement
        self.pos = pygame.math.Vector2(self.rect.center)
        self.direction = pygame.math.Vector2()
        self.speed = 200

    def import_assets(self):
        path = './graphics/player/right/'
        self.animation = [pygame.image.load(f'{path}{frame}.png').convert_alpha() for frame in range(4)]
        print(self.animation)

    def move(self, dt):
        # normalize a vector -> the length of a vector is going to be 1
        if self.direction.magnitude() != 0:
            self.direction = self.direction.normalize()

        self.pos += self.direction * self.speed * dt
        self.rect.center = (round(self.pos.x), round(self.pos.y))

    def input(self):
        keys = pygame.key.get_pressed()

        # vertical input
        if keys[pygame.K_w] or keys[pygame.K_UP]:
            self.direction.y = -1
        elif keys[pygame.K_s] or keys[pygame.K_DOWN]:
            self.direction.y = 1
        else:
            self.direction.y = 0

        # horizontal input
        if keys[pygame.K_a] or keys[pygame.K_LEFT]:
            self.direction.x = -1
        elif keys[pygame.K_d] or keys[pygame.K_RIGHT]:
            self.direction.x = 1
        else:
            self.direction.x = 0

    def animate(self, dt):
        self.frame_index += 10 * dt
        if self.frame_index >= len(self.animation):
            self.frame_index = 0
        self.image = self.animation[int(self.frame_index)]

    def update(self, dt):
        self.input()
        self.move(dt)
        self.animate(dt)