from Score import ScorePlayer
from Monsters.Monster import Monster 
from Score import ScorePlayer

class MonsterOne(Monster): 

    def __init__(self, x, y, monster_scale, config):
        Monster.__init__(self, config, monster_scale)
        self.color_monster = (0,0,255,255)
        self.x += x
        self.y += y
    
    def take_damage_and_increase_score(self, score_object: ScorePlayer): 
        score_object.increase_score(100)
        
    def _draw_basic_monster(self):
        self.clear_list_rect()
        
        # X start / y line / h heigh
        self.draw_new_line(2,0,1)
        self.draw_new_line(8,0,1)

        self.draw_new_line(3,1,1)
        self.draw_new_line(7,1,1)

        self.draw_new_line(2,2,7)

        self.draw_new_line(1,3,9)

        self.draw_new_line(0,4,3)
        self.draw_new_line(4,4,3)
        self.draw_new_line(8,4,3)

        self.draw_new_line(0,5,1)
        self.draw_new_line(2,5,7)
        self.draw_new_line(10,5,1)

        self.draw_new_line(0,6,1)
        self.draw_new_line(2,6,1)
        self.draw_new_line(8,6,1)
        self.draw_new_line(10,6,1)

        self.draw_new_line(3,7,2)
        self.draw_new_line(6,7,2)