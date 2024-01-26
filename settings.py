class Settings:
    def __init__(self):
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (50, 10, 77)
        self.ship_speed = 5.0
        self.ship_limit = 3

        self.bullet_speed = 3.0
        self.bullet_width = 3
        self.bullet_height = 20
        self.bullet_color = (200, 200, 200) #(43, 175, 227)
        self.bullets_allowed = 10

        self.alien_speed = 1.0
        self.fleet_drop_speed = 10
        self.fleet_direction = 1