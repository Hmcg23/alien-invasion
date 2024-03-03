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
images_path = os.path.join(images_dir, 'heart.bmp')

class Heart(Sprite):
    def __init__(self, ai_game):
        """Initialize the heart."""
        super().__init__()

        # Load and transform the heart image
        self.image = pygame.image.load(images_path)
        self.image = pygame.transform.rotozoom(self.image, 0, 0.05)

        # Get the rectangle bounding the heart image
        self.rect = self.image.get_rect()