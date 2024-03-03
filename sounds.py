import os
import pygame
import sys

pygame.mixer.init()

# Check if the application is packaged by PyInstaller
if getattr(sys, 'frozen', False):
    # When packaged, use the temporary directory created by PyInstaller
    base_path = sys._MEIPASS
else:
    # When running as a script, use the current directory
    base_path = os.path.dirname(os.path.abspath(__file__))

# Define the path to the sounds directory relative to the base directory
sounds_dir = os.path.join(base_path, 'sounds')

# Define the paths to the sound files relative to the sounds directory
soundtrack_path = os.path.join(sounds_dir, 'Space - Magic Fly ( 8-bit Sounds ).mp3')
game_start_path = os.path.join(sounds_dir, 'game-start.mp3')
death_sound_path = os.path.join(sounds_dir, 'death-sound.mp3')
shoot_path = os.path.join(sounds_dir, 'shoot.wav')
blip_select_path = os.path.join(sounds_dir, 'blipSelect.wav')
ship_hit_path = os.path.join(sounds_dir, 'hitHurt.wav')
explosion_path = os.path.join(sounds_dir, 'explosion.wav')
level_up_path = os.path.join(sounds_dir, 'level-up.mp3')
power_up_path = os.path.join(sounds_dir, 'power-up.mp3')
siren_path = os.path.join(sounds_dir, 'siren.wav')

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