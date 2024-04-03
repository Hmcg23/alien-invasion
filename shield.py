import math
import random
import pygame
from pygame.sprite import Sprite
from base_path import *

shield_path = get_file_path('images', 'pixel-shield.bmp')

class Shield(Sprite):
    def __init__(self, ai_game):
        """Initialize the alien and set its starting position."""
        super().__init__()
        # Store the screen object and game settings
        self.screen = ai_game.screen
        self.settings = ai_game.settings

        # Load the alien image and scale it
        self.image = pygame.image.load(shield_path)
        self.image = pygame.transform.rotozoom(self.image, 0, 0.02)
        self.rect = self.image.get_rect()

        # Start each new alien near the top left of the screen
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Store the alien's exact horizontal position
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)
        self.amplitude = random.randint(10, 15)
        self.frequency = random.uniform(0.005, 0.007)
    
    def blitme(self):
        """Draw the bullet on the screen."""
        # Blit the bullet onto the screen at its current position
        self.screen.blit(self.image, self.rect)
    
    def update(self):
        """Move the alien to the up and down."""
        timer = pygame.time.get_ticks()
        self.y = (800 // 2 + self.amplitude * math.sin(self.frequency * timer)) + 250
        self.rect.y = self.y