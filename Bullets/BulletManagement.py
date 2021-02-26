from Score import ScorePlayer
from Bullets.Bullet import Bullet
from Bullets.BulletMonster import BulletMonster
from Monsters.MonsterManager import MonsterManager
import random 

class BulletManagement:

    def __init__(self, surface):
        self.surface = surface
        self.list_bullets_shooted = []
        self.list_bullets_shooted_monsters = []
        self.delay_between_shoots = 0
        self.delay_between_shoots_monster = 0


    def create_new_shoot(self,x,y): 
        self.delay_between_shoots += 1
        new_bullet = Bullet(self.surface).create_shoot(x,y)
        self.list_bullets_shooted.append(new_bullet)

    def create_new_shoot_monster(self,x,y): 
        new_bullet_monster = BulletMonster(self.surface).create_shoot(x,y)
        self.list_bullets_shooted_monsters.append(new_bullet_monster)

    def can_shoot(self):
        if self.delay_between_shoots != 0 and self.delay_between_shoots <= 30:
            self.delay_between_shoots += 1
            return False
        else:
            self.delay_between_shoots = 0
            return True


    def move_all_shoots(self):
        for i in self.list_bullets_shooted:
            i.movement_shoot()
            self.__destroy_bullet_depens_screen(i)
            

    def __destroy_bullet_depens_screen(self,bullet: Bullet): 
        if bullet.rect_bullet.y <= 0:
            self.destroy_bullet(bullet)

    def __destroy_bullet_mosnter_depens_screen(self,bullet: Bullet): 
        if bullet.rect_bullet.y >= 900:
            print('destroy bullet')
            self.destroy_bullet_monster(bullet)


    def destroy_bullet_monster(self,bullet):
        self.list_bullets_shooted_monsters.remove(bullet)
        del bullet

    def destroy_bullet(self,bullet):
        self.list_bullets_shooted.remove(bullet)
        del bullet


    def get_all_bullets(self):
        return self.list_bullets_shooted


    def check_collider_bullet_contact(self,monsterController: MonsterManager, score_player: ScorePlayer):
        bullet_to_delete = None
        monster_to_destroy = None
        
        for bullet in self.list_bullets_shooted:
            for i in monsterController.get_all_monster_gen():
                for monster in i:
                    if bullet.rect_bullet.collidelistall(monster.get_rect_monster()):
                        bullet_to_delete = bullet
                        monster_to_destroy = monster
                        
                        
        if bullet_to_delete != None:
            print('whaaaaaaaaaaaaaaaaaaat ')
            self.destroy_bullet(bullet_to_delete)
            monsterController.destroy_monster(monster_to_destroy, score_player)

    def enemy_shooting_bullets(self, monsterController: MonsterManager):
        if self.delay_between_shoots_monster <= 0:
            try:
                index_row_monster = int(random.uniform(0,len(monsterController.list_monsters)))
                index_column_monster = int(random.uniform(0, len(monsterController.list_monsters[index_row_monster])))
                x = monsterController.list_monsters[index_row_monster][index_column_monster].x
                y = monsterController.list_monsters[index_row_monster][index_column_monster].y

                self.create_new_shoot_monster(x,y)
                self.delay_between_shoots_monster = len(monsterController.list_monsters)*3
            except:
                print('error')
                pass
        else:
            self.delay_between_shoots_monster -= 1
            
        
    def move_all_enemy_shoots(self):
        for i in self.list_bullets_shooted_monsters:
            i.movement_shoot_monster()
            self.__destroy_bullet_mosnter_depens_screen(i)