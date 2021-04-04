import pygame
from random import randint

BLACK = (0, 0, 0)
width = 640
height = 480


class Player(pygame.sprite.Sprite):
    def __init__(self):
        # pygame.sprite.Sprite.__init__(self)
        super().__init__()
        self.image = pygame.Surface([25, 25])
        self.image.fill(BLACK)
        self.rect = self.image.get_rect()
        self.lifes = 2
        self.score = 0
        self.high_score = 0
        self.speed = 10
        self.position_x = randint(100, 500)
        self.position_y = randint(100, 350)

    # Aqui o jogador tem movimento constante e eu só preciso indicar a direção
    # Também preciso mudar a configuração de direção manual ou não no "if playing:"
    def move(self):
        key = pygame.key.get_pressed()
        if key[pygame.K_LEFT]:
            self.position_x = -self.speed
            self.position_y = 0
        if key[pygame.K_RIGHT]:
            self.position_x = self.speed
            self.position_y = 0
        if key[pygame.K_UP]:
            self.position_y = -self.speed
            self.position_x = 0
        if key[pygame.K_DOWN]:
            self.position_y = self.speed
            self.position_x = 0

    def update_score(self):
        self.score += 1

        if self.score % 7 == 0:
            self.speed = 15
        elif self.score % 8 == 0 or self.score % 6 == 0:
            self.speed = 6
        else:
            self.speed = 10

    # Aqui eu movo o jogador da maneira q eu quero,
    # se não mover, ele fica parado
    def move_yourself(self):
        key = pygame.key.get_pressed()
        if key[pygame.K_LEFT]:
            self.position_x -= self.speed
            if self.position_x <= -35:
                self.position_x = 635

        if key[pygame.K_RIGHT]:
            self.position_x += self.speed
            if self.position_x >= 640:
                self.position_x = 5

        if key[pygame.K_UP]:
            self.position_y -= self.speed
            if self.position_y <= 0:
                self.position_y = 470

        if key[pygame.K_DOWN]:
            self.position_y += self.speed
            if self.position_y >= 480:
                self.position_y = 5