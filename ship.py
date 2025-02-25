import pygame


class Ship():
    def __init__(self, screen):
        # inial ship and starting point
        self.screen = screen

        # load ship image
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # put every ship in the center of the screen
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

    def blitme(self):
        """put ship at the pre-determined location"""
        self.screen.blit(self.image, self.rect)
