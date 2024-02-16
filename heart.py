import pygame
from pygame.sprite import Sprite


class Heart(Sprite):
    def __init__(self, ai_game):
        super().__init__()

        self.image = pygame.image.load('images/heart.bmp')
        self.image = pygame.transform.rotozoom(self.image, 0, 0.05)

        self.rect = self.image.get_rect()