import math
import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    def __init__(self, ai_game, x, y, angle):
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings

        self.original_bullet = pygame.image.load('images/bullet.bmp').convert()
        self.bullet = pygame.image.load('images/bullet.bmp')
        self.bullet = pygame.transform.rotozoom(self.bullet, 90, 1)
        self.rect = self.bullet.get_rect()

        self.x = x
        self.y = y
        self.angle = angle - 90
        self.speed = self.settings.bullet_speed
        self.x_vel = (math.cos(self.angle * (2 * math.pi/360)) * self.speed) * 2
        self.y_vel = (math.sin(self.angle * (2 * math.pi/360)) * self.speed)
        
    # Edited the bullet movement based on the ship direction
    def update(self):
        self.x -= self.x_vel
        self.y += self.y_vel

        self.rect.x = int(self.x)
        self.rect.y = int(self.y)    
        
        self.bullet = pygame.transform.rotozoom(self.original_bullet, (self.angle + 180)*1.1, 1)
    
    def blitme(self): # change name to blitme
        self.screen.blit(self.bullet, self.rect)