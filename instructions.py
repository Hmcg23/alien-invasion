import pygame
from pygame.sprite import Sprite
from base_path import *

image_path = get_file_path('images', 'alien_invasion_instructions.bmp')

class Instructions(Sprite):
    def __init__(self, ai_game):
        super().__init__()

        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()

        self.image = pygame.image.load(image_path)
        self.rect = self.image.get_rect()

        self.rect.centerx = self.screen_rect.centerx
        self.rect.centery = self.screen_rect.centery

        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

    def blitme(self):
        """Draw the image on the screen."""
        # Blit the instructions onto the screen at its current position
        self.screen.blit(self.image, self.rect)