import pygame
from pygame.sprite import Sprite
from base_path import *

images_path = get_file_path('images/background', 'mystery-powerup.bmp')

class Background(Sprite):
    def __init__(self, ai_game):
        """Initialize the background."""
        super().__init__()

        # List to store background images
        self.sprites = []

        # Reference to the screen and screen rectangle
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()

        # Load background images into the sprites list
        for i in range(0, 376):
            images_path = get_file_path('images/background', f'galaxy-bg-resize-{i}.bmp')
            self.sprites.append(pygame.image.load(images_path))
        
        # Initialize current sprite index and set initial background image
        self.current_sprite = 0
        self.image = self.sprites[self.current_sprite]
        self.image = pygame.transform.rotozoom(self.image, 0, 1)

        # Set the background image's rectangle to the screen's center
        self.rect = self.image.get_rect()
        self.rect.center = self.screen_rect.center
    
    def update(self):
        """Update the background image."""
        # Move to the next background image
        self.current_sprite += 1

        # If reached the end of the sprites list, reset to the first image
        if self.current_sprite >= len(self.sprites):
            self.current_sprite = 0
        
        # Update the background image with the current sprite
        self.image = self.sprites[int(self.current_sprite)]