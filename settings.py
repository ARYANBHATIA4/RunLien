#seprate file for settings as it would be changed alot
#class name with first letter capital
class Settings():
    """class to store all the settings of Alien Invasion"""
    def __init__(self):
        """initialize game's static settings"""
        #screen settings
        self.screen_width = 1299
        #blank screen of 1200 x 800 dimension 
        self.screen_height = 800
        #bgcolor in RGB
        self.bg_color = (164,218,244)    
        #Ship Settings
        self.ship_limit = 3
        #bullet settings
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 60, 60, 60
        self.bullets_allowed = 3
        #alien settings
        self.fleet_drop_speed = 20
        #game speedup speed
        self.speedup_scale = 1.1
        #alien point inc according to the level
        self.score_scale = 1.5
        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        """Initialize settings that change throughout the game."""
        self.ship_speed_factor = 1.5
        self.bullet_speed_factor = 3
        self.alien_speed_factor = 1
        #1=right -1=left
        self.fleet_direction = 1
        #scoring (single alien killing default point)
        self.alien_points = 100

    def increase_speed(self):
        """increases speed settings and point values"""
        self.ship_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.alien_speed_factor *= self.speedup_scale

        self.alien_points = int(self.alien_points * self.score_scale)
        print(self.alien_points)


