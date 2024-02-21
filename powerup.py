import math, random
import pygame
from pygame.sprite import Sprite


class Powerup(Sprite):
    def __init__(self, ai_game):
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings

        # Load and transform image image
        self.original_image = pygame.image.load('images/mystery-powerup.bmp').convert()
        self.image = pygame.image.load('images/mystery-powerup.bmp')
        self.image = pygame.transform.rotozoom(self.image, 0, 0.05)
        self.rect = self.image.get_rect()

        # Set initial position, angle, and speed of the image
        self.x = random.randint(10, self.settings.screen_width - 10)
        self.y = 0

        self.rect.x = int(self.x)    

        self.angle = float(0)

        # self.powerups = [i for i in range(0, 10)]
        self.powerups = 0
        
    def update(self):
        """Update the bullet's position."""
        # Move the image based on its velocity
        self.y += 5

        # Update the image's rect position
        self.rect.y = int(self.y)    
        
        # Rotate the image based on its angle
        self.image = pygame.transform.rotozoom(self.original_image, self.angle, 0.1)

        self.angle += 5 % 360

        self.rect.center = (self.x, self.y)
    
    def blitme(self):
        """Draw the bullet on the screen."""
        # Blit the image onto the screen at its current position
        self.screen.blit(self.image, self.rect)