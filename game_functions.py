import sys
import pygame


def check_events():
    # monitor keyboard and mouse event
    for event in pygame.event.get():
        if event.type == pygame.quit:
            sys.exit()


def update_screen(ai_settings, screen, ship):
    # update screen image, and cut to the new screen
    # every time loop through, update the screen
    screen.fill(ai_settings.bg_color)
    ship.blitme()

    # show the lastest screen
    pygame.display.flip()
