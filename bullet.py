import math, random
import pygame
from pygame.sprite import Sprite

from ship import Ship

class Bullet(Sprite):
    def __init__(self, ai_game, x, y, angle):
        """Initialize the bullet."""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings

        # Load and transform bullet image
        self.original_bullet = pygame.image.load('images/bullet.bmp').convert()
        self.bullet = pygame.image.load('images/bullet.bmp')
        self.bullet = pygame.transform.rotozoom(self.bullet, 90, 1)
        self.rect = self.bullet.get_rect()

        # Set initial position, angle, and speed of the bullet
        self.x = x
        self.y = y
        self.angle = angle - 90
        self.speed = self.settings.bullet_speed
        self.x_vel = (math.cos(self.angle * (2 * math.pi/360)) * self.speed) * 2
        self.y_vel = (math.sin(self.angle * (2 * math.pi/360)) * self.speed)
        
    def update(self):
        """Update the bullet's position."""
        # Move the bullet based on its velocity
        self.x -= self.x_vel
        self.y += self.y_vel

        # Update the bullet's rect position
        self.rect.x = int(self.x)
        self.rect.y = int(self.y)    
        
        # Rotate the bullet based on its angle
        self.bullet = pygame.transform.rotozoom(self.original_bullet, (self.angle + 180)*1.1, 1)
    
    def blitme(self):
        """Draw the bullet on the screen."""
        # Blit the bullet onto the screen at its current position
        self.screen.blit(self.bullet, self.rect)