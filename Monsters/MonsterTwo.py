from Monsters.Monster import Monster

class MonsterTwo(Monster): 

    def __init__(self, x, y, monster_scale, config): 
        Monster.__init__(self, config, monster_scale)
        self.color_monster = (0,255,0,255)
        self.x = x
        self.y = y

    def _draw_basic_monster(self):
        self.clear_list_rect()
        # X start / y line / s heigh
        self.draw_new_line(5,0,2)

        self.draw_new_line(4,1,4)

        self.draw_new_line(3,2,6)
        
        self.draw_new_line(2,3,2)
        self.draw_new_line(5,3,2)
        self.draw_new_line(8,3,2)
        
        self.draw_new_line(2,4,8)
        
        self.draw_new_line(4,5,1)
        self.draw_new_line(7,5,1)
        
        self.draw_new_line(3,6,1)
        self.draw_new_line(5,6,2)
        self.draw_new_line(8,6,1)

        self.draw_new_line(2,7,1)
        self.draw_new_line(4,7,1)
        self.draw_new_line(7,7,1)
        self.draw_new_line(9,7,1)