import pygame
from Monsters.MonsterOne import MonsterOne
from Monsters.MonsterTwo import MonsterTwo
from Monsters.MonsterThree import MonsterThree
from Monsters.MonsterFour import MonsterFour
from Monsters.MonsterFive import MonsterFive
from ConfigurationCharger import ChargeConfigurationClass

class MonsterManager(): 

    rows_monsters = 5
    quanty_per_rows = 6
    monster_scale = 4
    monster_speed = 3
    list_monsters = []
    direction_right = True

    def __init__(self,config_class):
        self.config = config_class
        self.surface = self.config.GetMonsterSurface()
        self.height_screen = self.config.GetHeightScreen() 
        self.width_screen = self.config.GetWidthScreen() 
        
        self.create_monster()

    def create_monster(self): 
        for i in range(self.quanty_per_rows):
            for a in range(self.rows_monsters):
                if a == 0:
                    self.list_monsters.append(MonsterOne(10*((i*self.monster_scale)*1.5), 10*((a*self.monster_scale)*1.1), self.monster_scale, self.config))
                elif a == 1:
                    self.list_monsters.append(MonsterTwo(10*((i*self.monster_scale)*1.5),10*((a*self.monster_scale)*1.1),  self.monster_scale, self.config))
                elif a == 2:
                    self.list_monsters.append(MonsterThree(10*((i*self.monster_scale)*1.5),10*((a*self.monster_scale)*1.1),  self.monster_scale, self.config))
                elif a == 3:
                    self.list_monsters.append(MonsterFive(10*((i*self.monster_scale)*1.5), 10*((a*self.monster_scale)*1.1), self.monster_scale, self.config))
                elif a == 4: 
                    self.list_monsters.append(MonsterFour(10*((i*self.monster_scale)*1.5), 10*((a*self.monster_scale)*1.1), self.monster_scale, self.config))

    def repaint_monsters(self): 
        for i in self.list_monsters:
            i._draw_basic_monster()

    def monster_movement(self): 
        for i in self.list_monsters:
            control = False
            if self.direction_right:
                control = self._monster_movement_right()
            else: 
                control = self._monster_movement_left()
            
            if control:
                break

        
    def _monster_movement_right(self):
        if self.list_monsters[(self.quanty_per_rows*self.rows_monsters)-1].x <= self.width_screen - 50 and self.direction_right:      
            self._move_all_monsters_right()
            return True            
        elif self.list_monsters[(self.quanty_per_rows*self.rows_monsters)-1].x >= self.width_screen - 50 and self.direction_right:
            self._move_all_monsters_down()
            self.direction_right = False 
            return True

    def _monster_movement_left(self):
        if self.list_monsters[0].x > 10 and not self.direction_right: 
            self._move_all_monsters_left()
            return True
        elif not self.direction_right and self.list_monsters[0].x >= 0: 
            self._move_all_monsters_down()
            self.direction_right = True
            return True


    def _move_all_monsters_right(self):
        for i in range(len(self.list_monsters)):
            self.list_monsters[i].x += self.monster_speed

    def _move_all_monsters_down(self):
        for i in range(len(self.list_monsters)):
            self.list_monsters[i].y += (self.monster_speed*5)

    def _move_all_monsters_left(self): 
        for i in range(len(self.list_monsters)):
            self.list_monsters[i].x -= self.monster_speed