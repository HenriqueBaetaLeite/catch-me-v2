import pygame
from pygame.locals import *
from random import randint

BLACK = (0, 0, 0)


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
        self.direction_x = randint(100, 500)
        self.direction_y = randint(100, 350)

    # Aqui o jogador tem movimento constante e eu só preciso indicar a direção
    def move(self):
        key = pygame.key.get_pressed()
        if key[pygame.K_LEFT]:
            self.direction_x = -self.speed
            self.direction_y = 0
        if key[pygame.K_RIGHT]:
            self.direction_x = self.speed
            self.direction_y = 0
        if key[pygame.K_UP]:
            self.direction_y = -self.speed
            self.direction_x = 0
        if key[pygame.K_DOWN]:
            self.direction_y = self.speed
            self.direction_x = 0

    # Aqui eu movo o jogador da maneira q eu quero, se não mover, ele fica parado
    def moveYourself(self):
        key = pygame.key.get_pressed()
        if key[pygame.K_LEFT]:
            self.direction_x -= self.speed
            if self.direction_x <= -35:
                self.direction_x = 635

        if key[pygame.K_RIGHT]:
            self.direction_x += self.speed
            if self.direction_x >= 640:
                self.direction_x = 5

        if key[pygame.K_UP]:
            self.direction_y -= self.speed
            if self.direction_y <= 0:
                self.direction_y = 470

        if key[pygame.K_DOWN]:
            self.direction_y += self.speed
            if self.direction_y >= 480:
                self.direction_y = 5