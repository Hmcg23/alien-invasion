import math, random
import pygame
from pygame.sprite import Sprite

from ship import Ship

class Alien_Bullet(Sprite):
    def __init__(self, ai_game, aliens, angle):
        """Initialize the bullet."""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings

        # Load and transform bullet image
        self.original_bullet = pygame.image.load('images/alien-bullet.bmp').convert()
        self.bullet = pygame.image.load('images/alien-bullet.bmp')
        self.bullet = pygame.transform.rotozoom(self.bullet, 90, 1)
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
        self.x += self.settings.alien_bullet_speed * (ship_x - self.x) / self.alien_ship_dist
        self.y += ((ship_x - self.x) / self.alien_ship_dist) + self.settings.alien_bullet_speed

        # Update the bullet's rect position
        self.rect.x = int(self.x)
        self.rect.y = int(self.y)    
        
        # Rotate the bullet based on its angle
        self.bullet = pygame.transform.rotozoom(self.original_bullet, (self.angle-90)*-1.1, 1)
    
    def blitme(self):
        """Draw the bullet on the screen."""
        # Blit the bullet onto the screen at its current position
        self.screen.blit(self.bullet, self.rect)