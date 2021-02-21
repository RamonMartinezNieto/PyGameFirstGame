import pygame
from Monsters.Monster import Monster 

class MonsterOne(Monster): 

    def __init__(self, x, y, monster_scale, config):
        Monster.__init__(self, config, monster_scale)
        self.color_monster = (0,0,255,255)
        self.x = x
        self.y = y
    
    def _draw_basic_monster(self):
        s = self.monster_scale
        x = self.x
        y = self.y

        pygame.draw.rect(self.surface, self.color_monster, (x+(s*2), y, s,s))
        pygame.draw.rect(self.surface, self.color_monster, (x+(s*8), y, s,s))

        pygame.draw.rect(self.surface, self.color_monster, (x+(s*3), y+s, s,s))
        pygame.draw.rect(self.surface, self.color_monster, (x+(s*7), y+s, s,s))

        pygame.draw.rect(self.surface, self.color_monster, (x+(s*2), y+(s*2), s*7,s))
        
        pygame.draw.rect(self.surface, self.color_monster, (x+(s), y+(s*3), s*9,s))

        pygame.draw.rect(self.surface, self.color_monster, (x, y+(s*4), s*3,s))
        pygame.draw.rect(self.surface, self.color_monster, (x+(s*4), y+(s*4), s*3,s))
        pygame.draw.rect(self.surface, self.color_monster, (x+(s*8), y+(s*4), s*3,s))

        pygame.draw.rect(self.surface, self.color_monster, (x, y+(s*5), s,s))
        pygame.draw.rect(self.surface, self.color_monster, (x+(s*2), y+(s*5), s*7,s))
        pygame.draw.rect(self.surface, self.color_monster, (x+(s*10), y+(s*5), s,s))

        pygame.draw.rect(self.surface, self.color_monster, (x, y+(s*6), s,s))
        pygame.draw.rect(self.surface, self.color_monster, (x+(s*2), y+(s*6), s,s))
        pygame.draw.rect(self.surface, self.color_monster, (x+(s*8), y+(s*6), s,s))
        pygame.draw.rect(self.surface, self.color_monster, (x+(s*10), y+(s*6), s,s))

        pygame.draw.rect(self.surface, self.color_monster, (x+(s*3), y+(s*7), s*2,s))
        pygame.draw.rect(self.surface, self.color_monster, (x+(s*6), y+(s*7), s*2,s))
         