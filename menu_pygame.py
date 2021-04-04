import os
import pygame
import pygame_menu

pygame.init()
os.environ['SDL_VIDEO_CENTERED'] = '1'
surface = pygame.display.set_mode((700, 500))


def set_difficulty(selected, value):
    """
    Set the difficulty of the game.
    """
    print('Set difficulty to {} ({})'.format(selected[0], value))


def start_the_game():
    """
    Function that starts a game. This is raised by the menu button,
    here menu can be disabled, etc.
    """
    print('Do the job here !\nPrepare for game starting...')


menu = pygame_menu.Menu(height=400,
                        width=500,
                        theme=pygame_menu.themes.THEME_BLUE,
                        title='Catch me if you can')

menu.add_text_input('Name: ', default='Player1')
menu.add_selector(
    'Difficulty: ', [('Hard', 1), ('Medium', 2),('Easy', 3)], onchange=set_difficulty)
menu.add_button('Play', start_the_game)
menu.add_button('Quit', pygame_menu.events.EXIT)
menu.add_color_input('Player Color', 'rgb', default=(255, 255, 9))
menu.add_color_input('Empty color in RGB: ',
                     color_type='rgb', input_separator='-')

menu.mainloop(surface)
