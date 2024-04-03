import os
import sys
import math, random
import pygame
from pygame.sprite import Sprite

from ship import Ship

from base_path import *

images_path = get_file_path('images', 'alien-bullet.bmp')

class Alien_Bullet(Sprite):
    def __init__(self, ai_game, aliens, angle):
        """Initialize the bullet."""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings

        # Load and transform bullet image
        self.original_bullet = pygame.image.load(images_path).convert()
        self.bullet = pygame.image.load(images_path)
        self.bullet = pygame.transform.rotozoom(self.bullet, 90, 5)
        self.rect = self.bullet.get_rect()

        self.ship = Ship(self)

        enemies = []
        
        for alien in aliens:
            enemies.append(alien)
            alien = random.choice(enemies)
            self.rect.centerx = alien.rect.centerx
            self.rect.bottom = alien.rect.bottom

        self.x = self.rect.x
        self.y = self.rect.y

        self.angle = angle

        self.alien_ship_dist = math.dist((self.x, self.y), (self.ship.rect.x, self.ship.rect.y))
    
    def update(self, ship_x, ship_y):

        # Move the bullet based on its velocity
        self.x += self.settings.alien_bullet_speed * (ship_x - self.x) / (self.alien_ship_dist * 2)
        self.y += ((ship_x - self.x) / self.alien_ship_dist) + self.settings.alien_bullet_speed * 2

        # Update the bullet's rect position
        self.rect.x = int(self.x)
        self.rect.y = int(self.y)    
        
        # Rotate the bullet based on its angle
        self.bullet = pygame.transform.rotozoom(self.original_bullet, (abs(self.x)/2 + 90) % 180, 1.5)
    
    def blitme(self):
        """Draw the bullet on the screen."""
        # Blit the bullet onto the screen at its current position
        self.screen.blit(self.bullet, self.rect)