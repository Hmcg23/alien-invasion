import sys

import pygame

from settings import Settings
from ship import Ship

# 238 - 246
# ~ p. 241

class AlienInvasion:
    def __init__(self):
        # Game resources
        pygame.init()
        pygame.display.set_caption("Alien Invasion")
        self.clock = pygame.time.Clock()
        self.settings = Settings()

        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        self.settings.screen_width = self.screen.get_rect().width
        self.settings.screen_height = self.screen.get_rect().height

        self.ship = Ship(self)

    def run_game(self):
        # Main loop
        while True:
            for event in pygame.event.get():
                self._check_events(event)
            self.ship.update()
            self._update_screen()
            self.clock.tick(60)
            
    def _check_events(self, event):
        # Watch for keyboard events
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            self._check_keydown_events(event)
        elif event.type == pygame.KEYUP:
            self._check_keyup_events(event)

    def _check_keydown_events(self, event):
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        elif event.key == pygame.K_UP:
            self.ship.moving_up = True
        elif event.key == pygame.K_DOWN:
            self.ship.moving_down = True
        elif event.key == pygame.K_q:
            sys.exit()

    def _check_keyup_events(self, event):
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False
        if event.key == pygame.K_UP:
            self.ship.moving_up = False
        elif event.key == pygame.K_DOWN:
            self.ship.moving_down = False


    def _update_screen(self):
        # Redraw the screen
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()
        # Display the most recent screen
        pygame.display.flip()    

if __name__ == '__main__':
    # Make a game instance, and run the game.
    ai = AlienInvasion()
    ai.run_game()