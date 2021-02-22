from abc import abstractmethod
from ConfigurationCharger import ChargeConfigurationClass
from pygame.draw import rect

class Monster(): 

    def __init__(self, config_class: ChargeConfigurationClass, monster_scale):

        # Changed in subclases
        self.color_monster = (0,0,0,255)
        self.x = 0 
        self.y = 0 

        # Same for all subclases
        self.monster_scale = monster_scale
        self.surface = config_class.get_principal_surface()
        self.height_screen = config_class.GetHeightScreen() 
        self.width_screen = config_class.GetWidthScreen() 

    @abstractmethod
    def _draw_basic_monster(self):
        pass   

    def draw_new_line(self,x,y,h):
        s = self.monster_scale
        rect(self.surface, self.color_monster, (self.x+(s*x), self.y+(s*y), s*h, s))