import pygame.font
from base_path import *
import random

fonts_path = get_file_path('fonts', 'pixel.ttf')

class PowerupInfoText:
    def __init__(self, ai_game):
        """Initialize the scoreboard."""
        # Initialize attributes
        self.ai_game = ai_game
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()
        self.settings = ai_game.settings
        self.stats = ai_game.stats

        # Text color and font
        self.text_color = (255, 255, 255)
        self.font = pygame.font.Font(fonts_path, 48)

        # Prepare initial scoreboard elements
        self.prep_text()

    def prep_text(self, text=""):
        """Prepare the text image."""
        # Render the score image
        self.image = self.font.render(text, True, self.text_color)

        # Position the score image
        self.rect = self.image.get_rect()
        self.rect.centerx = self.screen_rect.centerx
        self.rect.centery = self.screen_rect.centery

    def show_text(self):
        """Display/Blit the text onto the screen."""
        self.screen.blit(self.image, self.rect)