import sys
from time import sleep
import json
from pathlib import Path

import pygame

from settings import Settings
from game_stats import GameStats
from scoreboard import Scoreboard
from button import Button
from ship import Ship
from bullet import Bullet
from alien import Alien
from background import Background

class AlienInvasion:
    def __init__(self):
        # Game resources
        pygame.init()
        pygame.display.set_caption("Alien Invasion")
        self.clock = pygame.time.Clock()
        self.settings = Settings()

        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))

        self.stats = GameStats(self)
        self.sb = Scoreboard(self)

        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()

        self.background_images = pygame.sprite.Group()
        self.background = Background(self)
        self.background_images.add(self.background)

        self._create_fleet()
        self.game_active = False

        self.play_button = Button(self, "Play", 250)
        self.easy_button = Button(self, "Easy", 350)
        self.medium_button = Button(self, "Medium", 450)
        self.hard_button = Button(self, "Hard", 550)

        self.easy_button.button_color = (0, 0, 0)
        self.easy_button.text_color = (0,200,200)
        self.easy_button._prep_msg("Easy")

    def run_game(self):
        # Main loop
        while True:
            for event in pygame.event.get():
                self._check_events(event)
            if self.game_active:
                self.ship.update()
                self._update_bullets()
                self._update_aliens()

            self.background_images.draw(self.screen)
            self.background_images.update()

            self._update_screen()
            self.clock.tick(60)
            
    def _check_events(self, event):
        # Watch for keyboard events
        if event.type == pygame.QUIT:
            self._close_game()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            self._check_play_button(mouse_pos)
            self._check_difficulty_buttons(mouse_pos)
        elif event.type == pygame.KEYDOWN:
            self._check_keydown_events(event)
        elif event.type == pygame.KEYUP:
            self._check_keyup_events(event)
    
    def _check_play_button(self, mouse_pos):
        play_button_clicked = self.play_button.rect.collidepoint(mouse_pos)
        if not self.game_active:
            if play_button_clicked:
                # self.settings.initialize_dynamic_settings()

                self.stats.reset_stats()
                self.sb.prep_score()
                self.sb.prep_level()
                self.sb.prep_ships()
                self.game_active = True

                self.bullets.empty()
                self.aliens.empty()
                self._create_fleet()
                self.ship.center_ship()

                pygame.mouse.set_visible(False)
    
    def _set_button_colors(self, difficulty_button, text_color, button_color):
        if difficulty_button == 'easy':
            self.easy_button.button_color = button_color
            self.easy_button.text_color = text_color
            self.easy_button._prep_msg("Easy")

            self.medium_button.button_color = text_color
            self.medium_button.text_color = button_color
            self.medium_button._prep_msg("Medium")

            self.hard_button.button_color = text_color
            self.hard_button.text_color = button_color
            self.hard_button._prep_msg("Hard")
        elif difficulty_button == 'medium':
            self.easy_button.button_color = text_color
            self.easy_button.text_color = button_color
            self.easy_button._prep_msg("Easy")

            self.medium_button.button_color = button_color
            self.medium_button.text_color = text_color
            self.medium_button._prep_msg("Medium")


            self.hard_button.button_color = text_color
            self.hard_button.text_color = button_color
            self.hard_button._prep_msg("Hard")
        elif difficulty_button == 'hard':
                self.easy_button.button_color = text_color
                self.easy_button.text_color = button_color
                self.easy_button._prep_msg("Easy")

                self.medium_button.button_color = text_color
                self.medium_button.text_color = button_color
                self.medium_button._prep_msg("Medium")

                self.hard_button.button_color = button_color
                self.hard_button.text_color = text_color
                self.hard_button._prep_msg("Hard")

    def _check_difficulty_buttons(self, mouse_pos):
        easy_button_clicked = self.easy_button.rect.collidepoint(mouse_pos)
        medium_button_clicked = self.medium_button.rect.collidepoint(mouse_pos)
        hard_button_clicked = self.hard_button.rect.collidepoint(mouse_pos)
        
        if not self.game_active:
            if easy_button_clicked:
                self.settings.initialize_dynamic_settings(5.0, 10.0, 1.0)

                self._set_button_colors('easy', (0,200,200), (0, 0, 0))
            elif medium_button_clicked:
                self.settings.initialize_dynamic_settings(5.0, 10.0, 2.0)

                self._set_button_colors('medium', (0,200,200), (0, 0, 0))
            elif hard_button_clicked:
                self.settings.initialize_dynamic_settings(10.0, 10.0, 3.0)

                self._set_button_colors('hard', (0,200,200), (0, 0, 0))


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
            self._close_game()
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()

    def _check_keyup_events(self, event):
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False
        if event.key == pygame.K_UP:
            self.ship.moving_up = False
        elif event.key == pygame.K_DOWN:
            self.ship.moving_down = False
    
    def _fire_bullet(self):
        if len(self.bullets) < self.settings.bullets_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)
    
    def _update_bullets(self):
        self.bullets.update()
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)
        
        self._check_bullet_alien_collisions()
    
    def _check_bullet_alien_collisions(self):
        collisions = pygame.sprite.groupcollide(self.bullets, self.aliens, True, True)

        if collisions:
            for aliens in collisions.values():
                self.stats.score += self.settings.alien_points * len(aliens)
            self.sb.prep_score()
            self.sb.check_high_score()


        if not self.aliens:
            # delete aliens and make a new group
            self.bullets.empty()
            self._create_fleet()
            self.settings.increase_speed()

            # increase level
            self.stats.level += 1
            self.sb.prep_level()
    
    def _create_fleet(self):
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size

        current_x, current_y = alien_width, alien_height
        while current_y < (self.settings.screen_height - 2 * alien_height) - 100:
            while current_x < (self.settings.screen_width - 2 * alien_width):
                self._create_alien(current_x, current_y)
                current_x += 2 * alien_width
            
            current_x = alien_width
            current_y += 2 * alien_height
    
    def _create_alien(self, x_position, y_position):
        new_alien = Alien(self)
        new_alien.x = x_position
        new_alien.rect.x = x_position
        new_alien.rect.y = y_position
        self.aliens.add(new_alien)
    
    def _update_aliens(self):
        self._check_fleet_edges()
        self.aliens.update()

        if pygame.sprite.spritecollideany(self.ship, self.aliens):
            self._ship_hit()
        
        self._check_aliens_bottom()
    
    def _check_fleet_edges(self):
        for alien in self.aliens.sprites():
            if alien._check_edges():
                self._change_fleet_direction()
                break
    
    def _change_fleet_direction(self):
        for alien in self.aliens.sprites():
            alien.rect.y += self.settings.fleet_drop_speed
        self.settings.fleet_direction *= -1

    def _update_screen(self):
        # Redraw the screen
        # self.screen.fill(self.settings.bg_color)
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        self.ship.blitme()
        self.aliens.draw(self.screen)
        
        # Draw score info
        self.sb.show_score()
        if not self.game_active:
            self.play_button.draw_button()
            self.easy_button.draw_button()
            self.medium_button.draw_button()
            self.hard_button.draw_button()
        # Display the most recent screen
        pygame.display.flip()
    
    def _ship_hit(self):
        if self.stats.ships_left > 0:
            self.stats.ships_left -= 1
            self.sb.prep_ships()
            self.bullets.empty()
            self.aliens.empty()

            self._create_fleet()
            self.ship.center_ship()

            sleep(0.5)
        else:
            self.game_active = False
            pygame.mouse.set_visible(True)
    
    def _check_aliens_bottom(self):
        for alien in self.aliens.sprites():
            if alien.rect.bottom >= self.settings.screen_height:
                self._ship_hit()
                break
    
    def _close_game(self):
        saved_high_score = self.stats.get_high_score()
        if self.stats.high_score > saved_high_score:
            path = Path('high_score.json')
            path.write_text(json.dumps(self.stats.high_score))
        
        sys.exit()

if __name__ == '__main__':
    # Make a game instance, and run the game.
    ai = AlienInvasion()
    ai.run_game()