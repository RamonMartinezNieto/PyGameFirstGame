from pygame.draw import rect
from Monsters.Monster import Monster 

class MonsterFive(Monster): 

    def __init__(self, x, y, monster_scale, config):
        Monster.__init__(self, config, monster_scale)
        self.color_monster = (255, 191, 0,255)
        self.x = x
        self.y = y
    
    def _draw_basic_monster(self):

        self.draw_new_line(4,0,3)

        self.draw_new_line(2,1,7)

        self.draw_new_line(1,2,9)
        
        self.draw_new_line(0,3,11)

        self.draw_new_line(0,4,3)
        self.draw_new_line(4,4,3)
        self.draw_new_line(8,4,3)

        self.draw_new_line(0,5,11)
        
        self.draw_new_line(3,6,2)
        self.draw_new_line(6,6,2)

        self.draw_new_line(2,7,2)
        self.draw_new_line(5,7,1)
        self.draw_new_line(7,7,2)

        self.draw_new_line(3,8,2)
        self.draw_new_line(6,8,2)
