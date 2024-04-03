import sys, random
from time import sleep
import json
from pathlib import Path

import pygame

import sounds
from settings import Settings
from game_stats import GameStats
from scoreboard import Scoreboard
from button import Button
from overlay import Overlay
from ship import Ship
from bullet import Bullet
from alien_bullet import Alien_Bullet
from alien import Alien
from shield import Shield
from background import Background
from powerup import Powerup

class AlienInvasion:
    def __init__(self):
        """Initialize the game and create game resources."""
        # Initialize pygame
        pygame.init()
        pygame.display.set_caption("Alien Invasion")
        # Initialize clock for controlling frame rate
        self.clock = pygame.time.Clock()
        
        # Play the game soundtrack
        sounds.soundtrack.play(100)

        # Initialize game settings
        self.settings = Settings()

        # Set up the game window
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        self.screen_rect = self.screen.get_rect()

        # Create game statistics and scoreboard
        self.stats = GameStats(self)
        self.sb = Scoreboard(self)
        
        # Create the player's ship, bullet group, and alien group
        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()
        self.alien_bullets = pygame.sprite.Group()
        self.powerups = pygame.sprite.Group()

        # test - shields
        self.shields = pygame.sprite.Group()

        # Create background images and add the background
        self.background_images = pygame.sprite.Group()
        self.background = Background(self)
        self.background_images.add(self.background)

        self.game_active = False

        # Create play button and set its color and text
        self.play_button = Button(self, "Play", 500, 360)
        self.play_button.text_color = (0, 255, 255)
        self.play_button._prep_msg("Play")

        # Create difficulty buttons
        self.easy_button = Button(self, "Easy", 250, 435)
        self.medium_button = Button(self, "Medium", 500, 435)
        self.hard_button = Button(self, "Hard", 750, 435)
        
        # Create overlay for non-active game state
        self.overlay = Overlay(self)

        # Set intervals for when a powerup activates 
        self.last_powerup_time = pygame.time.get_ticks()
        self.next_powerup_time = random.randint(7000, 10000)

        # Set colors and text for difficulty buttons
        self.easy_button.text_color = (255, 105, 180)
        self.easy_button._prep_msg("Easy")

        # Initialize variables for Powerups
        self.pick_powerup = 0

        self.powerup_states = {
            1: {"activated": False, "start_time": None},
            2: {"activated": False, "start_time": None},
            3: {"activated": False, "start_time": None},
            4: {"activated": False, "start_time": None}
        }

        self.blink = False

        self.pause = False

    def run_game(self):
        """Start the main loop for the game."""
        while True:
            # Check events
            for event in pygame.event.get():
                self._check_events(event)
            # Update game elements if game is active
            if self.pause == False:
                if self.game_active:
                    self.ship.update()
                    self._update_bullets()
                    self._update_alien_bullets()
                    self._update_shields()

                    # Powerup Functions
                    self._aliens_freeze_powerup()

                    self._activate_powerup()
                    self._update_powerup()

                # Draw background images
                self.background_images.draw(self.screen)
                self.background_images.update()

                # Update screen
                self._update_screen()                
                # Control frame rate
                self.clock.tick(60)

# ----CHECK EVENTS---- #
                        
    def _check_events(self, event):
        """Respond to keyboard and mouse events."""
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
    
    def _check_keydown_events(self, event):
        """Respond to keypresses."""
        # Check for keydown events
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
            self._double_bullet_powerup()
        elif event.key == pygame.K_p:
            pygame.mixer.pause()
            self.pause = True
        elif event.key == pygame.K_u:
            pygame.mixer.unpause()
            self.pause = False

    def _check_keyup_events(self, event):
        """Respond to key releases."""
        # Check for keyup events
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False
        if event.key == pygame.K_UP:
            self.ship.moving_up = False
        elif event.key == pygame.K_DOWN:
            self.ship.moving_down = False

# ----BUTTONS---- #
    
    def _check_play_button(self, mouse_pos):
        """Start a new game when the player clicks Play."""
        # Check if play button is clicked
        play_button_clicked = self.play_button.rect.collidepoint(mouse_pos)
        if not self.game_active:
            if play_button_clicked:
                sounds.game_start.play()
                # Reset game stats
                self.stats.reset_stats()
                self.sb.prep_score()
                self.sb.prep_level()
                self.sb.prep_lives()
                self.game_active = True

                # Empty bullets and aliens, create new fleet, center ship
                self.bullets.empty()
                self.alien_bullets.empty()
                self.aliens.empty()
                self._create_fleet()
                self._create_shield_wall()
                self.ship.center_ship()

                pygame.mouse.set_visible(False)
    
    def _set_button_colors(self, difficulty_button, color_1, color_2):
        """Set the colors of difficulty buttons."""
        # Set colors for difficulty buttons
        if difficulty_button == 'easy':
            self.easy_button.text_color = color_1
            self.easy_button._prep_msg("Easy")

            self.medium_button.text_color = color_2
            self.medium_button._prep_msg("Medium")

            self.hard_button.text_color = color_2
            self.hard_button._prep_msg("Hard")
        elif difficulty_button == 'medium':
            # Set colors for medium difficulty
            self.easy_button.text_color = color_2
            self.easy_button._prep_msg("Easy")

            self.medium_button.text_color = color_1
            self.medium_button._prep_msg("Medium")

            self.hard_button.text_color = color_2
            self.hard_button._prep_msg("Hard")
        elif difficulty_button == 'hard':
            # Set colors for hard difficulty
            self.easy_button.text_color = color_2
            self.easy_button._prep_msg("Easy")

            self.medium_button.text_color = color_2
            self.medium_button._prep_msg("Medium")

            self.hard_button.text_color = color_1
            self.hard_button._prep_msg("Hard")

    def _check_difficulty_buttons(self, mouse_pos):
        """Check if difficulty buttons are clicked."""
        # Check if difficulty buttons are clicked
        easy_button_clicked = self.easy_button.rect.collidepoint(mouse_pos)
        medium_button_clicked = self.medium_button.rect.collidepoint(mouse_pos)
        hard_button_clicked = self.hard_button.rect.collidepoint(mouse_pos)
        
        if not self.game_active:
            if easy_button_clicked:
                # Set settings for easy difficulty
                self.settings.initialize_dynamic_settings(0.3, 10.0, 1.0, 2)
                sounds.blip_select.play()
                self._set_button_colors('easy',  (255, 105, 180), (0, 200, 200))
            elif medium_button_clicked:
                # Set settings for medium difficulty
                self.settings.initialize_dynamic_settings(0.4, 10.0, 2.0, 3)
                sounds.blip_select.play()
                self._set_button_colors('medium', (255,105,180), (0, 200, 200))
            elif hard_button_clicked:
                # Set settings for hard difficulty
                self.settings.initialize_dynamic_settings(0.5, 10.0, 3.0, 4)
                sounds.blip_select.play()
                self._set_button_colors('hard',  (255,105,180), (0, 200, 200))            

# ----POWERUPS---- #
    
    def _activate_powerup(self):
        current_time = pygame.time.get_ticks()
        # Check if it's time to activate a powerup
        if current_time - self.last_powerup_time >= self.next_powerup_time:
            new_powerup = Powerup(self)
            self.powerups.add(new_powerup)

            # Reset the timer for the next powerup
            self.last_powerup_time = current_time
            self.next_powerup_time = random.randint(5000, 10000) # 7000, 10000

    def _update_powerup(self):
        self.powerups.update()

        for powerup in self.powerups.copy():
            if powerup.rect.bottom >= self.screen_rect.bottom:
                self.powerups.remove(powerup)
        
        self._check_powerup_collisions()
    
    def _check_powerup_collisions(self):
        for powerup in self.powerups.copy():

            if pygame.sprite.spritecollideany(self.ship, self.powerups):
                sounds.power_up.set_volume(0.5)
                sounds.power_up.play()
                self.pick_powerup = random.randint(1, 4)
                # Delete the powerup if collided
                self.powerups.remove(powerup)

    def _do_powerup(self, powerup_num, powerup_time, normal_function, powerup_function = None):
        powerup_state = self.powerup_states[powerup_num]
        
        if self.pick_powerup == powerup_num and not powerup_state["activated"]:
            powerup_state["activated"] = True
            powerup_state["start_time"] = pygame.time.get_ticks()

            if not powerup_state["start_time"]:
                powerup_state["start_time"] = pygame.time.get_ticks()
        
        if not powerup_state["activated"]:
            normal_function()
        
        if powerup_state["activated"]:
            current_time = pygame.time.get_ticks()
            if powerup_function:
                powerup_function()
            
            if current_time - powerup_state["start_time"] >= powerup_time - 2000:
                self.blink = True
            
            if current_time - powerup_state["start_time"] >= powerup_time:
                powerup_state["activated"] = False
                self.pick_powerup = 0
                powerup_state["start_time"] = None
                self.blink = False
                self.overlay.transparency = 0
                self.overlay.increasing = True
                self.overlay.blink = False
         
# ----SHIELDS---- #
    def _create_shield_wall(self):
        pass
        """Create the wall of shields."""
        # Create a shield and find the number of shields in a row
        shield = Shield(self)
        shield_width, shield_height = shield.rect.size

        # Spacing between each ship 
        current_x, current_y = shield_width, shield_height
        while current_x < (self.settings.screen_width - 2 * shield_width):
            # Create an ship and place it in the row
            self._create_shield(current_x)
            current_x += 2 * shield_width
                    
        current_x = shield_width
        current_y += shield_height

    def _create_shield(self, x_position):
        new_shield = Shield(self)
        new_shield.x = x_position
        new_shield.y = 700

        new_shield.rect.x = x_position
        new_shield.rect.y = 700
        self.shields.add(new_shield)
    
    def _update_shields(self):
        """Update the positions of all aliens in the fleet."""
        self.shields.update()

# ----ALIENS---- #
    def _create_fleet(self):
        """Create the fleet of aliens."""
        # Create an alien and find the number of aliens in a row
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size

        # Spacing between each alien (x and y)
        current_x, current_y = alien_width, alien_height
        while current_y < (self.settings.screen_height - 2 * alien_height) - 100:
            while current_x < (self.settings.screen_width - 2 * alien_width):
                # Create an alien and place it in the row
                self._create_alien(current_x, current_y)
                current_x += 2 * alien_width
            
            # Move to the next row
            current_x = alien_width
            current_y += 2 * alien_height
    
    def _create_alien(self, x_position, y_position):
        """Create an alien and place it in the row."""
        # Create an alien and set its position
        new_alien = Alien(self)
        new_alien.x = x_position
        new_alien.rect.x = x_position
        new_alien.rect.y = y_position
        self.aliens.add(new_alien)
    
    def _aliens_freeze_powerup(self):
        self._do_powerup(1, 5000, self._update_aliens)

        self._invinsible_ship_powerup()
            
        self._check_aliens_bottom()

    def _update_aliens(self):
        """Update the positions of all aliens in the fleet."""
        self._check_fleet_edges()
        self.aliens.update()

    def _check_fleet_edges(self):
        """Respond appropriately if any aliens have reached an edge."""
        for alien in self.aliens.sprites():
            if alien._check_edges():
                self._change_fleet_direction()
                break
    
    def _change_fleet_direction(self):
        """Drop the entire fleet and change the fleet's direction."""
        for alien in self.aliens.sprites():
            alien.rect.y += self.settings.fleet_drop_speed
        self.settings.fleet_direction *= -1
    
    def _check_alien_bullet_and_ship_collisions(self):
        # Check for alien-ship collisions
        if pygame.sprite.spritecollideany(self.ship, self.alien_bullets):
            self._ship_hit()
    
    def _invincible_ship_alien_bullet_collisions(self):
        alien_bullets_to_remove = []

        # Check for collisions between the ship and aliens
        for bullet in self.alien_bullets:
            if pygame.sprite.collide_rect(self.ship, bullet):
                # If a collision is detected, mark the alien for removal
                alien_bullets_to_remove.append(bullet)

        # Remove the collided aliens from the group
        for bullet in alien_bullets_to_remove:
            self.alien_bullets.remove(bullet)
    
    def _check_aliens_bottom(self):
            """Check if any aliens have reached the bottom of the screen."""
            for alien in self.aliens.sprites():
                # Check if the bottom of the alien's rectangle reaches the bottom of the screen
                if alien.rect.bottom >= self.settings.screen_height:
                    self._ship_hit()
                    break

# ----ALIEN BULLETS---- #

    def _fire_alien_bullet(self, enemy_bullets):
        if len(enemy_bullets) < self.settings.enemy_bullets_allowed:
            new_alien_bullet = Alien_Bullet(self, self.aliens, self.ship.angle)
            self.alien_bullets.add(new_alien_bullet)

    def _update_alien_bullets(self):
        ship_pos = self.ship.get_pos()
        self.alien_bullets.update(ship_pos[0], ship_pos[1])

        for alien_bullet in self.alien_bullets.copy():
            if alien_bullet.rect.bottom <= 0 or alien_bullet.rect.left <= self.screen_rect.left or alien_bullet.rect.right >= self.screen_rect.right or alien_bullet.rect.bottom >= self.screen_rect.bottom + 10:
                self.alien_bullets.remove(alien_bullet)
        
        if random.randrange(0, 50) == 1:
            self._fire_alien_bullet(self.alien_bullets)
        
        self._do_powerup(4, 5000, self._check_alien_bullet_and_ship_collisions, self._invincible_ship_alien_bullet_collisions)


    def yellow_bullets_powerup(self):
        self._do_powerup(3, 10000, self._check_bullet_alien_collisions, self._check_yellow_bullet_alien_collisions)
        
        if not self.aliens:
                # If all aliens destroyed, start a new level
                sounds.level_up.play()
                self.bullets.empty()
                self.alien_bullets.empty()
                self.ship.center_ship()
                self._create_fleet()
                self.settings.increase_speed()

                # Increase level
                self.stats.level += 1
                self.sb.prep_level()
        
    def _check_bullet_alien_collisions(self):
            """Respond to bullet-alien collisions."""
            # Check for any bullets that have hit aliens
            collisions = pygame.sprite.groupcollide(self.bullets, self.aliens, True, True)
            pygame.sprite.groupcollide(self.bullets, self.alien_bullets, True, True)

            if collisions:
                for aliens in collisions.values():
                    sounds.explosion.set_volume(0.2)
                    sounds.explosion.play()
                    # Increase score for each alien hit
                    self.stats.score += self.settings.alien_points * len(aliens)
                self.sb.prep_score()
                self.sb.check_high_score()
    
    def _check_yellow_bullet_alien_collisions(self):
            """Respond to bullet-alien collisions."""
            # Check for any bullets that have hit aliens
            collisions = pygame.sprite.groupcollide(self.bullets, self.aliens, False, True)
            pygame.sprite.groupcollide(self.bullets, self.alien_bullets, False, True)

            if collisions:
                for aliens in collisions.values():
                    sounds.explosion.set_volume(0.2)
                    sounds.explosion.play()
                    # Increase score for each alien hit
                    self.stats.score += self.settings.alien_points * len(aliens)
                self.sb.prep_score()
                self.sb.check_high_score()              

# ----SHIP BULLETS---- #
                
    def _double_bullet_powerup(self):
        self._do_powerup(2, 10000, self._fire_bullet, self._fire_double_bullet)
    
    def _fire_bullet(self):
        # Fire ONE bullet if limit not reached
        if len(self.bullets) < self.settings.bullets_allowed:
            new_bullet = Bullet(self, self.ship.x + 25, self.ship.y, self.ship.angle)
            self.bullets.add(new_bullet)

            if self.game_active:
                sounds.shoot.set_volume(0.1)
                sounds.shoot.play()
    
    def _fire_double_bullet(self):
        if len(self.bullets) < self.settings.bullets_allowed:
            new_bullet = Bullet(self, self.ship.x-5, self.ship.y + 20, self.ship.angle)
            self.bullets.add(new_bullet)

            new_bullet = Bullet(self, self.ship.x + 45, self.ship.y + 20, self.ship.angle)
            self.bullets.add(new_bullet)

        if self.game_active:
            sounds.shoot.set_volume(0.1)
            sounds.shoot.play()

    def _update_bullets(self):
        """Update position of bullets and get rid of old bullets."""
        # Update bullet positions
        self.bullets.update()
        # Get rid of bullets that have disappeared
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0 or bullet.rect.left <= self.screen_rect.left or bullet.rect.right >= self.screen_rect.right or bullet.rect.bottom >= self.screen_rect.bottom:
                self.bullets.remove(bullet)
        
        self.yellow_bullets_powerup()

# ----SHIP---- #
    
    def _invinsible_ship_powerup(self):
        self._do_powerup(4, 5000, self._ship_alien_collisions, self._invincible_ship_alien_collisions)
    
    def _ship_alien_collisions(self):
        # Check for alien-ship collisions
        if pygame.sprite.spritecollideany(self.ship, self.aliens):
            self._ship_hit()
    
    def _invincible_ship_alien_collisions(self):
        aliens_to_remove = []

        # Check for collisions between the ship and aliens
        for alien in self.aliens:
            if pygame.sprite.collide_rect(self.ship, alien):
                # If a collision is detected, mark the alien for removal
                sounds.explosion.set_volume(0.2)
                sounds.explosion.play()
                # Increase score for each alien hit
                self.stats.score += self.settings.alien_points
                aliens_to_remove.append(alien)

            self.sb.prep_score()
            self.sb.check_high_score()

        # Remove the collided aliens from the group
        for alien in aliens_to_remove:
            self.aliens.remove(alien)
            
    
    def _ship_hit(self):
        """Respond to the ship being hit by an alien."""
        if self.stats.ships_left > 0:
            sounds.ship_hit.set_volume(0.5)
            sounds.ship_hit.play()
            # Decrement ships_left and update scoreboard
            self.stats.ships_left -= 1
            self.sb.prep_lives()
            # Empty the list of aliens and bullets
            self.bullets.empty()
            self.alien_bullets.empty()
            self.aliens.empty()

            # Create a new fleet and center the ship
            self._create_fleet()
            self.ship.center_ship()

            sleep(0.2)
        else:
            # Reset ship velocity and end the game if no ships left
            self.ship.x_vel = 0
            self.ship.y_vel = 0

            sounds.death_sound.play()
            self.game_active = False
            pygame.mouse.set_visible(True)
            self.blink = False

            # Reset Powerups
            self.powerup_states = {
                1: {"activated": False, "start_time": None},
                2: {"activated": False, "start_time": None},
                3: {"activated": False, "start_time": None},
                4: {"activated": False, "start_time": None}
            }
            self.pick_powerup = 0

            self.settings.initialize_dynamic_settings(0.3, 10.0, 1.0, 2)

# ----SCREEN---- #

    def _update_screen(self):
        """Update images on the screen, and flip to the new screen."""
        # Redraw the screen during each pass through the loop
        for bullet in self.bullets.sprites():
            self._do_powerup(3, 10000, bullet.blitme, bullet.blitme_yellow)
                    
        for alien_bullet in self.alien_bullets.sprites():
            alien_bullet.blitme()
        
        for powerup in self.powerups.sprites():
            powerup.blitme()
        
        self._do_powerup(4, 5000, self.ship.blitme, self.ship.blitme_yellow)
        self.aliens.draw(self.screen)
        self.shields.draw(self.screen)

        self.overlay.blink_overlay(self.screen, self.blink)
        
        # Draw score info
        self.sb.show_score()
        if not self.game_active:
            # Draw overlay and buttons if game is inactive
            self.overlay.draw_overlay(self.screen)

            self.play_button.draw_button(self.screen, (255,20,147))
            self.easy_button.draw_button(self.screen, (0, 255, 255))
            self.medium_button.draw_button(self.screen, (0, 255, 255))
            self.hard_button.draw_button(self.screen, (0, 255, 255))
            
        # Display the most recent screen
        pygame.display.flip()

# ----CLOSE GAME---- #

    def _close_game(self):
        """Close the game and save high score if it's greater than the saved one."""
        saved_high_score = self.stats.get_high_score()
        # Check if the current high score is greater than the saved one
        if self.stats.high_score > saved_high_score:
            path = Path('high_score.json')
            path.write_text(json.dumps(self.stats.high_score))
        
        sys.exit()

if __name__ == '__main__':
    # Make a game instance, and run the game.
    ai = AlienInvasion()
    ai.run_game()