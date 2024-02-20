import json
from pathlib import Path

class GameStats:
    def __init__(self, ai_game):
        """Initialize game statistics."""
        # Store the game settings
        self.settings = ai_game.settings
        # Reset game statistics
        self.reset_stats()
        # Retrieve the high score
        self.high_score = self.get_high_score()

    def reset_stats(self):
        """Reset the statistics that can change during the game."""
        self.ships_left = self.settings.ship_limit
        self.score = 0
        self.level = 1
    
    def get_high_score(self):
        """Retrieve the high score from a file."""
        path = Path('high_score.json')
        try:
            # Try to read the contents of the high score file
            contents = path.read_text()
            high_score = json.loads(contents)
            return high_score
        except FileNotFoundError:
            return 0