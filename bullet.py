import os
import sys
import math
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
images_path = os.path.join(images_dir, 'bullet.bmp')

class Bullet(Sprite):
    def __init__(self, ai_game, x, y, angle):
        """Initialize the bullet."""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings

        # Load and transform bullet image
        self.original_bullet = pygame.image.load(images_path).convert_alpha()
        self.bullet = pygame.transform.rotozoom(self.original_bullet, 90, 1)
        self.rect = self.bullet.get_rect()

        self.original_bullet_yellow = pygame.image.load(images_path).convert_alpha()

        for y_pos in range(self.original_bullet_yellow.get_height()):
            for x_pos in range(self.original_bullet_yellow.get_width()):
                color = self.original_bullet_yellow.get_at((x_pos, y_pos))
                if color[3] != 0:  # If pixel is not transparent
                    if not (200 <= color[0] <= 255 and 200 <= color[1] <= 255 and 200 <= color[2] <= 255):  # If not in the range of white and gray
                        self.original_bullet_yellow.set_at((x_pos, y_pos), (255, 255, 0, color[3]))  # Set color to yellow
        
        # Scale down the ship image
        self.bullet_yellow = pygame.transform.rotozoom(self.original_bullet_yellow, 90, 1)        


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
    
    def blitme_yellow(self):
        """Draw the bullet on the screen."""
        # Blit the bullet onto the screen at its current position
        self.screen.blit(self.bullet_yellow, self.rect)