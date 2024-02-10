class Settings:
    def __init__(self):
        self.screen_width = 1400
        self.screen_height = 820
        self.bg_color = (50, 10, 77)
        self.ship_speed = 5.0
        self.ship_limit = 3

        self.bullet_speed = 3.0
        self.bullet_width = 3
        self.bullet_height = 20
        self.bullet_color = (230, 230, 230) #(43, 175, 227)
        self.bullets_allowed = 10

        self.alien_speed = 1.0
        self.fleet_drop_speed = 10
        self.fleet_direction = 1

        self.speedup_scale = 1.1
        self.initialize_dynamic_settings()
    
    def initialize_dynamic_settings(self, ship_speed = 5.0, bullet_speed = 1.0, alien_speed = 1.0):

        self.ship_speed = ship_speed
        self.bullet_speed = bullet_speed
        self.alien_speed = alien_speed

        self.fleet_direction = 1
    
    def increase_speed(self):
        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale