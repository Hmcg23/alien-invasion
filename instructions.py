import pygame

from base_path import *

image_path = get_file_path('images', 'alien_invasion_instructions.bmp')

class Instructions:
    def __init__(self, ai_game):

        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()
        self.settings = ai_game.settings

        self.image = pygame.image.load(image_path)
        self.rect = self.image.get_rect()

        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

    def blitme(self):
        """Draw the bullet on the screen."""
        # Blit the instructions onto the screen at its current position
        self.screen.blit(self.image, self.rect)