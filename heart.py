import pygame
from pygame.sprite import Sprite
from base_path import *

images_path = get_file_path('images', 'heart.bmp')

class Heart(Sprite):
    def __init__(self, ai_game):
        """Initialize the heart."""
        super().__init__()

        # Load and transform the heart image
        self.image = pygame.image.load(images_path)
        self.image = pygame.transform.rotozoom(self.image, 0, 0.05)

        # Get the rectangle bounding the heart image
        self.rect = self.image.get_rect()