import os
import sys
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
images_path = os.path.join(images_dir, 'alien.bmp')

class Alien(Sprite):
    def __init__(self, ai_game):
        """Initialize the alien and set its starting position."""
        super().__init__()
        # Store the screen object and game settings
        self.screen = ai_game.screen
        self.settings = ai_game.settings

        # Load the alien image and scale it
        self.image = pygame.image.load(images_path)
        self.image = pygame.transform.rotozoom(self.image, 0, 0.05)
        self.rect = self.image.get_rect()

        # Start each new alien near the top left of the screen
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Store the alien's exact horizontal position
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

    def _check_edges(self):
        """Return True if alien is at edge of screen."""
        # Get the rectangle object for the screen
        screen_rect = self.screen.get_rect()
        # Check if alien is at either edge of the screen
        return (self.rect.right >= screen_rect.right) or (self.rect.left <= 0)
    
    def update(self):
        """Move the alien to the right or left."""
        # Update the horizontal position of the alien based on fleet direction
        self.x += self.settings.alien_speed * self.settings.fleet_direction
        # Update the rect object from self.x
        self.rect.x = self.x