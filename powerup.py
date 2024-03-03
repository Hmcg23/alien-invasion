import os
import sys
import random
import pygame
from pygame.sprite import Sprite

# Check if the application is packaged by PyInstaller
if getattr(sys, 'frozen', False):
    # When packaged, use the temporary directory created by PyInstaller
    base_path = sys._MEIPASS
else:
    # When running as a script, use the current directory
    base_path = os.path.dirname(os.path.abspath(__file__))

# Define the path to the sounds directory relative to the base directory
images_dir = os.path.join(base_path, 'images')

# Define the paths to the sound files relative to the sounds directory
images_path = os.path.join(images_dir, 'mystery-powerup.bmp')


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