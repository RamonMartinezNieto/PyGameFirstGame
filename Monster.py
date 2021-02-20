import pygame
import ConfigurationCharger

class Monster: 

    def __init__(self,configurationClass):
        self.monster_type = 'type_one'
        self.list_monsters = []

        self.monster_speed = 5
        self.monster_scale = 4

        self.Config = configurationClass 
        self.surface = self.Config.GetMonsterSurface()
        self.height_screen = self.Config.GetHeightScreen() 
        self.width_screen = self.Config.GetWidthScreen() 
        self.direction_right = True
        self.color_monster = (0,255,0,255)

        self.rows_monsters = 4
        self.quanty_per_rows = 6

        self.create_monster(self.quanty_per_rows,self.rows_monsters)

    def create_monster(self,quantityPerRow,rowsMonster): 
        self._draw_basic_monster(10,10)

        for i in range(quantityPerRow):
            for a in range(rowsMonster):
                self.list_monsters.append([10*((i*self.monster_scale)*1.5),10*((a*self.monster_scale)*1.1)])
    
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
            control = False
            if self.direction_right:
                control = self._monster_movement_right()
            else: 
                control = self._monster_movement_left()
            
            if control:
                break

        
    def _monster_movement_right(self):
        if self.list_monsters[(self.quanty_per_rows*self.rows_monsters)-1][0] <= self.width_screen - 100 and self.direction_right:      
            self._move_all_monsters_right()
            return True            
        elif self.list_monsters[(self.quanty_per_rows*self.rows_monsters)-1][0] >= self.width_screen - 100 and self.direction_right:
            self._move_all_monsters_down()
            self.direction_right = False 
            return True

    def _monster_movement_left(self):
        if self.list_monsters[0][0] > 50 and not self.direction_right: 
            self._move_all_monsters_left()
            return True
        elif not self.direction_right and self.list_monsters[0][0] >= 0: 
            self._move_all_monsters_down()
            self.direction_right = True
            return True


    def _move_all_monsters_right(self):
        for i in range(len(self.list_monsters)):
            self.list_monsters[i][0] += self.monster_speed

    def _move_all_monsters_down(self):
        for i in range(len(self.list_monsters)):
            self.list_monsters[i][1] += self.monster_speed

    def _move_all_monsters_left(self): 
        for i in range(len(self.list_monsters)):
            self.list_monsters[i][0] -= self.monster_speed


    def get_list_monsters(self): 
        return self.list_monsters
            