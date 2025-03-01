import pygame
import sys
from settings import Settings
from ship import Ship
import game_functions as gf


def run_game():
    # initialization
    pygame.init()
    # screen = pygame.display.set_mode((1200, 800))
    ai_settings = Settings()
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height)
    )
    pygame.display.set_caption("Alien Invasion")

    # create a ship
    ship = Ship(screen)

    # set bakground color
    # bg_color = (230, 230, 230)

    # start game main
    while True:
        # monitor keyboard and mouse event
        gf.check_events()
        gf.update_screen(ai_settings, screen, ship)
        '''
        for event in pygame.event.get():
            # screen.fill(bg_color)
            screen.fill(ai_settings.bg_color)
            ship.blitme()
            if event.type == pygame.QUIT:
                sys.exit()
        '''

        # show the latest screen
        pygame.display.flip()


run_game()
