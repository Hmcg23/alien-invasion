import pygame
from pygame.sprite import Sprite
from base_path import *

spaceship_path = get_file_path('images', 'spaceship.bmp')
spaceship_yellow_path = get_file_path('images', 'spaceship-yellow.bmp')

class Ship(Sprite):
    def __init__(self, ai_game):
        """Initialize the ship and set its starting position."""
        super().__init__()

        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()

        # Load the ship image and set its size
        self.original_image = pygame.image.load(spaceship_path).convert_alpha()
        self.image = pygame.transform.rotozoom(self.original_image, 0, 0.5)
        self.rect = self.image.get_rect()

        # Yellow Ship
        self.original_yellow_image = pygame.image.load(spaceship_yellow_path).convert_alpha()
        self.yellow_image = pygame.transform.rotozoom(self.original_yellow_image, 0, 0.5)
        self.yellow_rect = self.image.get_rect()

        # Start each new ship at the bottom center of the screen
        self.rect.centerx = self.screen_rect.centerx
        self.rect.y = 735

        # Store the ship's horizontal and vertical positions
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)
        self.x_vel = 0
        self.y_vel = 0

        # Movement flags
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False

        # Ship angle
        self.angle = float(0)
        self.angle_vel = 0
    
    def update(self):
        """Update the ship's position based on movement flags."""
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
        """Rotate the ship image."""
        self.image = pygame.transform.rotozoom(self.original_image, self.angle, 0.5)
        self.yellow_image = pygame.transform.rotozoom(self.original_yellow_image, self.angle, 0.5)
        if int(self.angle) != angle:
            self.angle += ((angle - self.angle) / 10)
        else:
            self.angle = angle
        x, y = self.rect.center
        self.rect.center = (x, y)
    
    def get_pos(self):
        return (self.x, self.y)

    def center_ship(self):
        """Center the ship on the screen."""
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)
        self.y = float(self.rect.y - 10)

    def blitme(self):
        """Draw the ship at its current location."""
        self.screen.blit(self.image, self.rect)

    def blitme_yellow(self):
        """Draw the ship at its current location."""
        self.screen.blit(self.yellow_image, self.rect)
