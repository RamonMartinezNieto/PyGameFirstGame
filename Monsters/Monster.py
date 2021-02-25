from abc import abstractmethod
from ConfigurationCharger import ChargeConfigurationClass
from pygame.draw import rect

class Monster(): 

    def __init__(self, config_class: ChargeConfigurationClass, monster_scale):

        # Changed in subclases
        self.color_monster = (0,0,0,255)
        self.x = 0 
        self.y = 0 
        self.list_rect_monster = []

        # Same for all subclases
        self.monster_scale = monster_scale
        self.surface = config_class.get_principal_surface()
        self.height_screen = config_class.GetHeightScreen() 
        self.width_screen = config_class.GetWidthScreen() 

    @abstractmethod
    def _draw_basic_monster(self):
        pass   

    def clear_list_rect(self):
        self.list_rect_monster.clear()

    def draw_new_line(self,x,y,h):
        s = self.monster_scale
        new_rect = rect(self.surface, self.color_monster, (self.x+(s*x), self.y+(s*y), s*h, s))
        self.list_rect_monster.append(new_rect)

    def reapint_monster(self):
        for my_rec in self.list_rect_monster:
            rect(self.surface, self.color_monster, my_rec)

    def get_rect_monster(self):
        return self.list_rect_monster

    def take_damage(self): 
        print('me has dado!')