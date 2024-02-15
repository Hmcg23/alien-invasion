import pygame
from pygame.sprite import Sprite


class Background(Sprite):
    def __init__(self, ai_game):
        super().__init__()

        self.sprites = []

        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()

        for i in range(0, 376):
            image = f'images/background/galaxy-bg-resize-{i}.bmp'
            self.sprites.append(pygame.image.load(image))
        
        
        self.current_sprite = 0
        self.image = self.sprites[self.current_sprite]
        self.image = pygame.transform.rotozoom(self.image, 0, 1)


        self.rect = self.image.get_rect()
        self.rect.center = self.screen_rect.center
    
    def update(self):
        self.current_sprite += 1

        if self.current_sprite >= len(self.sprites):
            self.current_sprite = 0
        
        self.image = self.sprites[int(self.current_sprite)]