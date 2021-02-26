from Monsters.Monster import Monster 
from Score import ScorePlayer

class MonsterFour(Monster): 

    def __init__(self, x, y, monster_scale, config):
        Monster.__init__(self, config, monster_scale)
        self.color_monster = (255,0,255,255)
        self.x += x
        self.y += y
    
    def take_damage_and_increase_score(self, score_object: ScorePlayer): 
        score_object.increase_score(400)
        
    def _draw_basic_monster(self):
        self.clear_list_rect()
        self.draw_new_line(5,0,2)

        self.draw_new_line(4,1,4)

        self.draw_new_line(3,2,6)
        
        self.draw_new_line(2,3,2)
        self.draw_new_line(5,3,2)
        self.draw_new_line(8,3,2)

        self.draw_new_line(2,4,8)

        self.draw_new_line(3,5,1)
        self.draw_new_line(5,5,2)
        self.draw_new_line(8,5,1)

        self.draw_new_line(2,6,1)
        self.draw_new_line(9,6,1)

        self.draw_new_line(3,7,1)
        self.draw_new_line(8,7,1)
         