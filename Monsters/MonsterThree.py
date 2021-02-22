from pygame.draw import rect
from Monsters.Monster import Monster 

class MonsterThree(Monster): 

    def __init__(self, x, y, monster_scale, config):
        Monster.__init__(self, config, monster_scale)
        self.color_monster = (255,0,0,255)
        self.x = x
        self.y = y
    
    def _draw_basic_monster(self):

        self.draw_new_line(3,0,1)
        self.draw_new_line(8,0,1)

        self.draw_new_line(4,1,1)
        self.draw_new_line(7,1,1)

        self.draw_new_line(5,2,2)

        self.draw_new_line(3,3,6)
        
        self.draw_new_line(2,4,2)
        self.draw_new_line(5,4,2)
        self.draw_new_line(8,4,2)

        self.draw_new_line(1,5,10)

        self.draw_new_line(1,6,1)
        self.draw_new_line(3,6,6)
        self.draw_new_line(10,6,1)

        self.draw_new_line(1,7,1)
        self.draw_new_line(3,7,1)
        self.draw_new_line(8,7,1)
        self.draw_new_line(10,7,1)
        
        self.draw_new_line(4,8,1)
        self.draw_new_line(7,8,1)
         
        self.draw_new_line(3,9,1)
        self.draw_new_line(8,9,1)         