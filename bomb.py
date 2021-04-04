import pygame
from pygame.locals import *

sprites_bomb = [
    pygame.image.load("assets/bomb1.png"),
    pygame.image.load("assets/bomb2.png"),
    pygame.image.load("assets/bomb3.png"),
]


class Bomb(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        # self.image = pygame.Surface([20, 20])
        # self.image.fill(RUST)
        self.sprites = sprites_bomb
        self.current_sprite = 0
        self.image = self.sprites[self.current_sprite]
        self.rect = self.image.get_rect()
        self.is_animating = False

    # def animate(self):
    #     self.is_animating = True

    def update(self):
        self.current_sprite += 0.2
        if self.current_sprite > len(self.sprites):
            self.current_sprite = 0
        self.image = self.sprites[int(self.current_sprite)]