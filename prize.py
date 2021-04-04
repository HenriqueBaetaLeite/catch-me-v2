import pygame
from pygame.locals import *
from random import randint

RED = (194, 24, 7)

width = 640
height = 480


class Prize(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface([10, 10])
        self.image.fill(RED)
        self.rect = self.image.get_rect()

    def move(self):
        self.rect.x = randint(50, width - 50)
        self.rect.y = randint(50, height - 50)
