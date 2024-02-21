class Settings:
    def __init__(self):
        """Initialize game settings."""
        # Screen settings
        self.screen_width = 1200
        self.screen_height = 820
        self.bg_color = (50, 10, 77)

        # Ship settings
        self.ship_speed = 0.3 
        self.ship_limit = 3 

        # Bullet settings
        self.bullet_speed = 3.0
        self.bullet_width = 4
        self.bullet_height = 25
        self.bullet_color = (0, 200, 200)
        self.bullets_allowed = 10

        # Alien settings
        self.alien_speed = 1.0
        self.fleet_drop_speed = 10
        self.fleet_direction = 1
        self.enemy_bullets_allowed = 10
        self.alien_bullet_speed = 5

        # Speed settings
        self.speedup_scale = 1.1
        self.score_scale = 1.5
        
        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self, ship_speed=0.3, bullet_speed=10.0, alien_speed=1.0, alien_bullet_speed = 5):
        """Initialize settings that change throughout the game."""
        # Initialize ship, bullet, and alien speeds
        self.ship_speed = ship_speed
        self.bullet_speed = bullet_speed
        self.alien_speed = alien_speed
        self.alien_bullet_speed = alien_bullet_speed

        # Reset fleet direction to default
        self.fleet_direction = 1

        # Alien points earned for each shot down
        self.alien_points = 50

    def increase_speed(self):
        """Increase speed settings and alien point values."""
        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale
        self.alien_bullet_speed *= self.speedup_scale

        # Increase alien point value
        self.alien_points = int(self.alien_points * self.score_scale)