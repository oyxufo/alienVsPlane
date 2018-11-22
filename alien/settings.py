class Settings():
    def __init__(self):
        self.screen_width = 1000
        self.screen_height = 700
        self.bg_color = (113,200,200)
        self.ship_speed = 1.5
        self.bullet_speed = 1
        self.bullet_width = 3
        self.bullet_height = 14.5
        self.bullet_color = 60,80,90
        self.bullets_allowed = 3
        self.alien_speed = 1
        self.alien_drop_speed = 10
        self.direction = 1
        self.ship_limit = 3
        self.speedup = 1.5
        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        self.ship_speed = 1.5
        self.bullet_speed = 3
        self.alien_speed = 1
        self.direction = 1
        self.alien_drop_speed = 10
        self.alien_points = 50

    def increase_speed(self):
        self.alien_drop_speed *= self.speedup
        self.bullet_speed *= self.speedup
        self.alien_speed *= self.speedup
        self.alien_points *= self.speedup





