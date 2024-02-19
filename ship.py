import pygame
from pygame.sprite import Sprite

class Ship(Sprite):
    def __init__(self, ai_game):
        super().__init__()

        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()

        self.original_image = pygame.image.load('images/spaceship.bmp').convert()
        self.image = pygame.image.load('images/spaceship.bmp')
        self.image = pygame.transform.rotozoom(self.image, 0, 0.5)

        self.rect = self.image.get_rect()

        self.rect.centerx = self.screen_rect.centerx
        self.rect.y = 735

        self.x = float(self.rect.x)
        self.y = float(self.rect.y)
        self.x_vel = 0
        self.y_vel = 0

        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False

        self.angle = float(0)
        self.angle_vel = 0
    
    def update(self):
        # Left and Right Movement
        if self.moving_right:
            self.x_vel += self.settings.ship_speed
            self.rotate(-40)
        if self.rect.right > self.screen_rect.right:
            self.x_vel = 0
            self.x = self.screen_rect.right - 60
        if self.moving_left:
            self.x_vel -= self.settings.ship_speed
            self.rotate(40)
        if self.rect.left < 0:
            self.x_vel = 0
            self.x = self.screen_rect.left + 5
        # Up and Down Movement
        if self.moving_up:
            self.y_vel -= self.settings.ship_speed
        if self.rect.top < self.screen_rect.top:
            self.y_vel = 0
            self.y = self.screen_rect.top + 5
        if self.moving_down:
            self.y_vel += self.settings.ship_speed
        if self.rect.bottom > self.screen_rect.bottom:
            self.y_vel = 0
            self.y = self.screen_rect.bottom - 80

        # Slow down ship        
        if not self.moving_up and not self.moving_down:
            self.y_vel = self.y_vel * 0.9
        if not self.moving_left and not self.moving_right:
            self.x_vel = self.x_vel * 0.9
        
        # Update values
        self.x += self.x_vel
        self.y += self.y_vel
        
        self.rect.x = self.x
        self.rect.y = self.y
        self.rotate(0)
    
    def rotate(self, angle):
        self.image = pygame.transform.rotozoom(self.original_image, self.angle, 0.5)
        if int(self.angle) != angle:
            self.angle += ((angle - self.angle) / 10)
        else:
            self.angle = angle
        x, y = self.rect.center
        self.rect.center = (x, y)

    def center_ship(self):
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)
        self.y = float(self.rect.y - 10)

    def blitme(self):
        self.screen.blit(self.image, self.rect)