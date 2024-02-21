import pygame.font
from pygame.sprite import Group

from heart import Heart

class Scoreboard:
    def __init__(self, ai_game):
        """Initialize the scoreboard."""
        # Initialize attributes
        self.ai_game = ai_game
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()
        self.settings = ai_game.settings
        self.stats = ai_game.stats

        # Text color and font
        self.text_color = (255, 255, 255)
        self.font = pygame.font.Font("fonts/pixel.ttf", 32)

        # Prepare initial scoreboard elements
        self.prep_score()
        self.prep_high_score()
        self.prep_level()
        self.prep_lives()

    def prep_score(self):
        """Prepare the score image."""
        # Round the score and format it with commas
        rounded_score = round(self.stats.score, -1)
        score_str = f"{rounded_score:,}"
        # Render the score image
        self.score_image = self.font.render(score_str, True, self.text_color)

        # Position the score image
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 20

    def show_score(self):
        """Display/Blit the score, high score, level, and remaining lives onto the screen."""
        self.screen.blit(self.score_image, self.score_rect)
        self.screen.blit(self.high_score_image, self.high_score_rect)
        self.screen.blit(self.level_image, self.level_rect)
        self.hearts.draw(self.screen)

    def prep_high_score(self):
        """Prepare the high score image."""
        # Round the high score and format it with commas
        high_score = round(self.stats.high_score, -1)
        high_score_str = f"{high_score:,}"
        # Render the high score image
        self.high_score_image = self.font.render(high_score_str, True, self.text_color)

        # Position the high score image
        self.high_score_rect = self.high_score_image.get_rect()
        self.high_score_rect.centerx = self.screen_rect.centerx
        self.high_score_rect.top = self.score_rect.top  

    def check_high_score(self):
        """Check if the current score is a new high score."""
        if self.stats.score > self.stats.high_score:
            # Update the high score if the current score is higher
            self.stats.high_score = self.stats.score
            self.prep_high_score()
    
    def prep_level(self):
        """Prepare the level image."""
        # Convert the level number to a string
        level_str = str(self.stats.level)
        self.level_image = self.font.render(level_str, True, self.text_color)

        # Position the level image
        self.level_rect = self.level_image.get_rect()
        self.level_rect.right = self.score_rect.right
        self.level_rect.top = self.score_rect.bottom + 10
    
    def prep_lives(self):
        """Prepare the remaining lives."""
        # Create a group for heart sprites
        self.hearts = Group()
        # Add heart sprites to the group based on remaining lives
        for ship_number in range(self.stats.ships_left):
            heart = Heart(self.ai_game)
            heart.rect.x = 10 + ship_number * heart.rect.width
            heart.rect.y = 10
            self.hearts.add(heart)