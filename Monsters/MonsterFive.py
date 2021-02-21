from pygame.draw import rect
from Monsters.Monster import Monster 

class MonsterFive(Monster): 

    def __init__(self, x, y, monster_scale, config):
        Monster.__init__(self, config, monster_scale)
        self.color_monster = (255, 191, 0,255)
        self.x = x
        self.y = y
    
    def _draw_basic_monster(self):
        s = self.monster_scale
        x = self.x
        y = self.y

        rect(self.surface, self.color_monster, (x+(s*4), y, s*3,s))

        rect(self.surface, self.color_monster, (x+(s*2), y+s, s*7,s))

        rect(self.surface, self.color_monster, (x+(s), y+(s*2), s*9,s))
        
        rect(self.surface, self.color_monster, (x, y+(s*3), s*11,s))

        rect(self.surface, self.color_monster, (x, y+(s*4), s*3,s))
        rect(self.surface, self.color_monster, (x+(s*4), y+(s*4), s*3,s))
        rect(self.surface, self.color_monster, (x+(s*8), y+(s*4), s*3,s))

        rect(self.surface, self.color_monster, (x, y+(s*5), s*11,s))
        
        rect(self.surface, self.color_monster, (x+(s*3), y+(s*6), s*2,s))
        rect(self.surface, self.color_monster, (x+(s*6), y+(s*6), s*2,s))

        rect(self.surface, self.color_monster, (x+(s*2), y+(s*7), s*2,s))
        rect(self.surface, self.color_monster, (x+(s*5), y+(s*7), s,s))
        rect(self.surface, self.color_monster, (x+(s*7), y+(s*7), s*2,s))

        rect(self.surface, self.color_monster, (x+(s*3), y+(s*8), s*2,s))
        rect(self.surface, self.color_monster, (x+(s*6), y+(s*8), s*2,s))
