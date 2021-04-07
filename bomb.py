import pygame

from random import randint, choice
# from sounds import sounds_bomb

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

    def bomb_animate(self):
        self.current_sprite += 0.2
        if self.current_sprite > len(self.sprites):
            self.current_sprite = 0
        self.image = self.sprites[int(self.current_sprite)]

    def bomb_position(self):
        self.rect.x = randint(0, 600)
        self.rect.y = randint(50, 400)

    # def bomb_collision(self, create_bomb, bomb, prize, ghost_prize, player, bomb_group):
    #     bomb_sound = pygame.mixer.Sound(choice(sounds_bomb))

    #     bomb_sound.set_volume(0.4)
    #     if bomb.rect.colliderect(prize.rect):
    #         bomb.rect.x = randint(0, 600)
    #         bomb.rect.y = randint(0, 400)
    #     if bomb.rect.colliderect(ghost_prize.rect):
    #         bomb.rect.x = randint(0, 600)
    #         bomb.rect.y = randint(0, 400)
    #     if bomb.rect.colliderect(player.rect):
    #         player.lifes -= 1
    #         player.score += 2
    #         bomb_sound.play()
    #         bomb_group.remove(bomb)
    #         create_bomb()
    #         if player.score > player.high_score:
    #             player.high_score = player.score