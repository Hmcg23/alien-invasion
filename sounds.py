import pygame

pygame.mixer.init()

soundtrack = pygame.mixer.Sound('sounds/Space - Magic Fly ( 8-bit Sounds ).mp3')
game_start = pygame.mixer.Sound('sounds/game-start.mp3')
death_sound = pygame.mixer.Sound('sounds/death-sound.mp3')
shoot = pygame.mixer.Sound('sounds/8-bit-kit-lazer-5.wav')
blip_select = pygame.mixer.Sound('sounds/blipSelect.wav')
ship_hit = pygame.mixer.Sound('sounds/hitHurt.wav')
explosion = pygame.mixer.Sound('sounds/explosion.wav')