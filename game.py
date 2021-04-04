import pygame
from pygame.locals import *
import sys

from time import sleep
from random import randint, choice

from player import Player
from bomb import Bomb
from prize import Prize

from sounds import background_music, sounds_prize, sounds_bomb, sounds_gameover

pygame.init()

width = 640
height = 480

window = pygame.display.set_mode((width, height))

pygame.display.set_caption("Catch Me!")

frame_per_second = pygame.time.Clock()
FPS = 30

# MUSIC AND SOUNDS

pygame.mixer.music.load(choice(background_music))
pygame.mixer.music.play(-1)  # -1 faz um loop com a música
pygame.mixer.music.set_volume(0.1)


# Colors

RED = (194, 24, 7)
BLACK = (0, 0, 0)
RUST = (147, 58, 22)
WHITE = (255, 255, 255)

# Criação dos objetos Player e Prize

player = Player()

# player.rect.x = width // 2
# player.rect.y = height // 2

prize = Prize()
prize.rect.x = randint(50, width - 50)
prize.rect.y = randint(50, height - 50)


# Sprite Groups

sprites_groups = pygame.sprite.Group()
sprites_groups.add(player, prize)
ghost_prize_group = pygame.sprite.Group()
ghost_prize_group.add()

bomb_group = pygame.sprite.Group()


# redraw function


def redraw():
    if playing:
        window.fill(WHITE)
        font = pygame.font.SysFont("ebrima", 20)
        score = font.render("Score: " + str(player.score), False, BLACK)
        scoreRect = score.get_rect()
        scoreRect.center = (width // 2, 50)
        window.blit(score, scoreRect)
        lifes = font.render("Life: " + str(player.lifes), False, BLACK)
        window.blit(lifes, (5, 5))
        player.moveYourself()
        sprites_groups.update()
        sprites_groups.draw(window)
        ghost_prize_group.update()
        ghost_prize_group.draw(window)
        bomb_group.update()
        bomb_group.draw(window)
    else:
        window.fill(BLACK)
        font = pygame.font.SysFont("gabriola", 40)
        title = font.render("Catch Me IF You Can!", False, WHITE)
        titleRect = title.get_rect()
        titleRect.center = (width // 2, 100)
        window.blit(title, titleRect)

        high_score = font.render(
            "High Score " + str(player.high_score), False, RUST
        )
        high_scoreRect = high_score.get_rect()
        high_scoreRect.center = (width // 2, height // 2)
        window.blit(high_score, high_scoreRect)

        start_space = font.render(
            "Press Space to start",
            False,
            (randint(0, 255), randint(0, 255), randint(0, 255)),
        )
        start_spaceRect = start_space.get_rect()
        start_spaceRect.center = (width // 2, 400)
        window.blit(start_space, start_spaceRect)

    # pygame.display.flip()
    pygame.display.update()


def player_get_prize():
    collision_noise_prize = pygame.mixer.Sound(choice(sounds_prize))
    collision_noise_prize.set_volume(0.2)
    collision_noise_prize.play()

    player.update_score()

    # player.score += 1

    # if player.score % 7 == 0:
    #     player.speed = 15
    # elif player.score % 8 == 1:
    #     player.speed = 5
    # else:
    #     player.speed = 10

    new_prize = Prize()
    new_prize.rect.x = randint(50, width - 50)
    new_prize.rect.y = randint(50, height - 50)

    prize.move()
    
    bomb = Bomb()

    if player.score % 2 == 0:
        ghost_prize_group.add(new_prize)
    if player.score % 6 == 0:
        ghost_prize_group.empty()
    if player.score % 2 == 0:
        bomb.update()
        bomb.rect.x = randint(0, 600)
        bomb.rect.y = randint(0, 400)
        bomb_group.add(bomb)
    if len(bomb_group) % 7 == 0 and len(ghost_prize_group) % 7 == 0:
        bomb_group.empty()


# Main loop

running = True
playing = False

while running:
    # pygame.time.delay(60)
    frame_per_second.tick(FPS)

    key = pygame.key.get_pressed()

    for event in pygame.event.get():
        if event.type == QUIT or key[pygame.K_q] or key[pygame.K_ESCAPE]:
            # running = False
            pygame.quit()
            sys.exit()

    if key[pygame.K_s]:
        pygame.mixer.music.fadeout(1500)

    if key[pygame.K_p]:
        pygame.mixer.music.pause()

    if key[pygame.K_m]:
        pygame.mixer.music.load(choice(background_music))
        pygame.mixer.music.play()

    if playing:
        # Para o modo contínuo devo acrescentar +=
        # Para o modo manual apenas atribuo o valor
        player.rect.x = player.direction_x
        player.rect.y = player.direction_y

        # Collision
        for bomb in bomb_group:
            bomb_sound = pygame.mixer.Sound(choice(sounds_bomb))
            bomb_sound.set_volume(0.4)
            if bomb.rect.colliderect(prize.rect):
                bomb.rect.x = randint(0, 600)
                bomb.rect.y = randint(0, 400)
            if bomb.rect.colliderect(player.rect):
                player.lifes -= 1
                player.score -= 2
                bomb_sound.play()
                bomb_group.remove(bomb)
                if player.score > player.high_score:
                    player.high_score = player.score
                if player.lifes <= 0:
                    pygame.mixer.music.fadeout(400)
                    sleep(0.5)
                    game_over_sound = pygame.mixer.Sound(
                        choice(sounds_gameover)
                    )
                    game_over_sound.play()
                    sleep(1.5)
                    playing = False

        if player.rect.colliderect(prize.rect):
            player_get_prize()

        # if player.rect.collidepoint(50, 50):
        #     player.rect.x = randint(0,600)
        #     player.rect.y = randint(0,600)
        #     print('bati')
        #     print('...')

    else:
        if key[pygame.K_SPACE]:
            playing = True
            pygame.mixer.music.play()
            bomb_group.empty()
            ghost_prize_group.empty()
            player.score = 0
            player.lifes = 2
            player.rect.x = width // 2
            player.rect.y = width // 2

    redraw()

pygame.quit()
sys.exit()
