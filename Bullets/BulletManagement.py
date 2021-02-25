from Bullets.Bullet import Bullet
from Monsters.MonsterManager import MonsterManager

class BulletManagement:
    

    def __init__(self, surface):
        self.surface = surface
        self.list_bullets_shooted = []
        self.delay_between_shoots = 0


    def create_new_shoot(self,x,y): 
        self.delay_between_shoots += 1
        new_bullet = Bullet(self.surface).create_shoot(x,y)
        self.list_bullets_shooted.append(new_bullet)

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


    def destroy_bullet(self,bullet):
        self.list_bullets_shooted.remove(bullet)
        del bullet


    def get_all_bullets(self):
        return self.list_bullets_shooted


    def check_collider_bullet_contact(self,monsterController: MonsterManager):
        bullet_to_delete = None
        for bullet in self.list_bullets_shooted:
            for i in monsterController.get_all_monster_gen():
                for monster in i:
                    if bullet.rect_bullet.collidelistall(monster.get_rect_monster()):
                        bullet_to_delete = bullet 
                        monster.take_damage()
                        
        if bullet_to_delete != None:
            self.destroy_bullet(bullet_to_delete)
