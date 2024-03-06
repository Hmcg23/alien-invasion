import pygame
from base_path import *

pygame.mixer.init()

# Define the paths to the sound files relative to the sounds directory
soundtrack_path = get_file_path('sounds', 'Space - Magic Fly ( 8-bit Sounds ).mp3')
game_start_path = get_file_path('sounds', 'game-start.mp3')
death_sound_path = get_file_path('sounds', 'death-sound.mp3')
shoot_path = get_file_path('sounds', 'shoot.wav')
blip_select_path = get_file_path('sounds', 'blipSelect.wav')
ship_hit_path = get_file_path('sounds', 'hitHurt.wav')
explosion_path = get_file_path('sounds', 'explosion.wav')
level_up_path = get_file_path('sounds', 'level-up.mp3')
power_up_path = get_file_path('sounds', 'power-up.mp3')
siren_path = get_file_path('sounds', 'siren.wav')

# Load the sound files using the constructed paths
soundtrack = pygame.mixer.Sound(soundtrack_path)
game_start = pygame.mixer.Sound(game_start_path)
death_sound = pygame.mixer.Sound(death_sound_path)
shoot = pygame.mixer.Sound(shoot_path)
blip_select = pygame.mixer.Sound(blip_select_path)
ship_hit = pygame.mixer.Sound(ship_hit_path)
explosion = pygame.mixer.Sound(explosion_path)
level_up = pygame.mixer.Sound(level_up_path)
power_up = pygame.mixer.Sound(power_up_path)
siren = pygame.mixer.Sound(siren_path)