import pygame
import ConfigurationCharger

class Monster: 

    def __init__(self,configurationClass):
        self.monster_type = 'type_one'
        self.list_monsters = []

        self.monster_speed = 5
        self.monster_scale = 2

        self.Config = configurationClass 
        self.surface = self.Config.GetMonsterSurface()
        self.height_screen = self.Config.GetHeightScreen() 
        self.width_screen = self.Config.GetWidthScreen() 
        self.direction_right = True
        self.color_monster = (0,255,0,255)

        self.create_monster()

    def create_monster(self): 
        self._draw_basic_monster(10,10)
        self.list_monsters.append([10,10])
    
    def repaint_monsters(self): 
        for i in range(len(self.list_monsters)):
            x = self.list_monsters[i][0]
            y = self.list_monsters[i][1]
            self._draw_basic_monster(x,y)

    def _draw_basic_monster(self,x,y):
        s = self.monster_scale
        
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




        

    def monster_movement(self): 

        for i in range(len(self.list_monsters)):

            self._monster_movement_right(i)
            self._monster_movement_left(i)

        
    def _monster_movement_right(self, positionMonsterList):
            if self.list_monsters[positionMonsterList][0] <= self.width_screen - 100 and self.direction_right: 
                self.list_monsters[positionMonsterList][0] += self.monster_speed

            elif self.list_monsters[positionMonsterList][0] >= self.width_screen - 100 and self.direction_right:
                self.list_monsters[positionMonsterList][1] += self.monster_speed
                self.direction_right = False 

    def _monster_movement_left(self,positionMonsterList):
        if self.list_monsters[positionMonsterList][0] > 50 and not self.direction_right: 
            self.list_monsters[positionMonsterList][0] -= self.monster_speed

        elif not self.direction_right and self.list_monsters[positionMonsterList][0] >= 0: 
            self.list_monsters[positionMonsterList][1] += self.monster_speed
            self.direction_right = True


    def get_list_monsters(self): 
        return self.list_monsters
            