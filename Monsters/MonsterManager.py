from Score import ScorePlayer
from Monsters.Monster import Monster
from Monsters.MonsterOne import MonsterOne
from Monsters.MonsterTwo import MonsterTwo
from Monsters.MonsterThree import MonsterThree
from Monsters.MonsterFour import MonsterFour
from Monsters.MonsterFive import MonsterFive
from ConfigurationCharger import ChargeConfigurationClass

class MonsterManager(): 

    rows_monsters = 5
    quanty_per_rows = 8
    monster_scale = 4
    monster_speed = 3
    list_monsters = []
    direction_right = True

    def __init__(self, config_class: ChargeConfigurationClass):
        self.config = config_class
        self.surface = self.config.get_principal_surface()
        self.height_screen = self.config.GetHeightScreen() 
        self.width_screen = self.config.GetWidthScreen() 
        
        for i in range(self.rows_monsters):
            self.list_monsters.append([])

        self.create_monster()

    def create_monster(self): 
        for i in range(self.quanty_per_rows):
            for a in range(self.rows_monsters):
                if a == 0:
                    self.list_monsters[0].append(MonsterOne(10*((i*self.monster_scale)*1.5), 10*((a*self.monster_scale)*1.1), self.monster_scale,  self.config))
                elif a == 1:
                    self.list_monsters[1].append(MonsterTwo(10*((i*self.monster_scale)*1.5),10*((a*self.monster_scale)*1.1),  self.monster_scale, self.config))
                elif a == 2:
                    self.list_monsters[2].append(MonsterThree(10*((i*self.monster_scale)*1.5),10*((a*self.monster_scale)*1.1),  self.monster_scale, self.config))
                elif a == 3:
                    self.list_monsters[3].append(MonsterFive(10*((i*self.monster_scale)*1.5), 10*((a*self.monster_scale)*1.1), self.monster_scale, self.config))
                elif a == 4: 
                    self.list_monsters[4].append(MonsterFour(10*((i*self.monster_scale)*1.5), 10*((a*self.monster_scale)*1.1), self.monster_scale, self.config))


    def repaint_monsters(self): 
        for monster in self.get_monster_gen():
            monster._draw_basic_monster()


    def monster_movement(self): 
        if self.direction_right:
            self._monster_movement_right()
        else: 
            self._monster_movement_left()

                
    def _monster_movement_right(self):
        try:
            monster = self._get_monster_more_close_to_screen('right')
            if monster.x <= self.width_screen - 50 and self.direction_right:      
                self._move_all_monsters_right()
            elif monster.x >= self.width_screen - 50 and self.direction_right:
                self._move_all_monsters_down()
                self.direction_right = False 
        except:
            pass

    def _monster_movement_left(self):
        monster = self._get_monster_more_close_to_screen('left')
        try:
            if monster.x > 0 and not self.direction_right:
                self._move_all_monsters_left()
            elif not self.direction_right and monster.x >= 0: 
                self._move_all_monsters_down()
                self.direction_right = True 
        except:
            pass

    def _get_monster_more_close_to_screen(self,slide):
        count_first = 0
        monster_to_return = Monster
        for monster in self.get_monster_gen():
            if count_first == 0: 
                monster_to_return = monster
                count_first +=1 
            else:
                if slide == 'right' and monster_to_return.x < monster.x:
                    monster_to_return = monster
                elif slide == 'left' and monster_to_return.x > monster.x:
                    monster_to_return = monster
        return monster_to_return


    def _move_all_monsters_right(self):
        for monster in self.get_monster_gen():
            monster.x += self.monster_speed


    def _move_all_monsters_down(self):
        for monster in self.get_monster_gen():
            monster.y += (self.monster_speed*5)


    def _move_all_monsters_left(self): 
        for monster in self.get_monster_gen():
            monster.x -= self.monster_speed     


    # Generator 
    def get_monster_gen(self): 
        for monster in self.list_monsters:
            yield from monster

    def get_all_monster_gen(self): 
        return self.list_monsters

    def destroy_monster(self,bye_monster: Monster, score_player: ScorePlayer):
        index_row = 0 
        index_column = 0
        for i in range(len(self.list_monsters)):
            for j in range(len(self.list_monsters[i])):
                if self.list_monsters[i][j] == bye_monster:
                    index_row = i
                    index_column = j

        bye_monster.take_damage_and_increase_score(score_player)
        del self.list_monsters[index_row][index_column]
        del bye_monster