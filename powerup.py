import random
import pygame
from pygame.sprite import Sprite
from base_path import *

images_path = get_file_path('images', 'mystery-powerup.bmp')


class Powerup(Sprite):
    def __init__(self, ai_game):
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings

        # Load and transform image image
        self.original_image = pygame.image.load(images_path).convert()
        self.image = pygame.image.load(images_path)
        self.image = pygame.transform.rotozoom(self.image, 0, 0.05)
        self.rect = self.image.get_rect()

        # Set initial position, angle, and speed of the image
        self.x = random.randint(self.rect.x, self.settings.screen_width - 100)
        self.y = 0

        self.rect.x = int(self.x)    

        self.angle = float(0)
        
    def update(self):
        """Update the bullet's position."""
        # Move the image based on its velocity
        self.y += 5

        # Update the image's rect position
        self.rect.y = int(self.y)    
        
        # Rotate the image based on its angle
        self.image = pygame.transform.rotozoom(self.original_image, self.angle, 0.1)

        self.angle += 5
        self.angle = self.angle % 360

        self.rect.center = (self.x, self.y)
    
    def blitme(self):
        """Draw the bullet on the screen."""
        # Blit the image onto the screen at its current position
        self.screen.blit(self.image, self.rect)