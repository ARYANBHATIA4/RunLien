#seprate file for settings as it would be changed alot
#class name with first letter capital
class Settings():
    """class to store all the settings of Alien Invasion"""
    def __init__(self):
        """initialize game settings"""
        #screen settings
        self.screen_width = 1200
        #blank screen of 1200 x 800 dimension 
        self.screen_height = 800
        #bgcolor in RGB
        self.bg_color = (164,218,244)    
        #Ship Settings
        self.ship_speed_factor = 1.5
