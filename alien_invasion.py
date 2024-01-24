import sys

import pygame

from settings import Settings
from ship import Ship


class AlienInvasion:
    def __init__(self):
        # Game resources
        pygame.init()
        self.clock = pygame.time.Clock()
        self.settings = Settings()

        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Alien Invasion")

        self.ship = Ship(self)

    def run_game(self):
        # Main loop
        while True:
            self._check_events
            self.ship.update()
            self._update_screen()
            self.clock.tick(60)
            
    def _check_events(self):
        # Watch for keyboard events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    self.ship.moving_right = True
                elif event.key == pygame.K_LEFT:
                    self.ship.moving_left = True
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT:
                    self.ship.moving_right = False
                elif event.key == pygame.K_LEFT:
                    self.ship.moving_left = False


    def _update_screen(self):
        # Redraw the screen
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()
        # Display the most recent screen
        pygame.display.flip()        


if __name__ == '__main__':
    # Make and run game instance
    ai = AlienInvasion()
    ai.run_game()