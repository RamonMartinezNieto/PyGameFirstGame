from Bullets.Bullet import Bullet

class BulletManagement:
    

    def __init__(self, surface):
        self.surface = surface
        self.list_rect_shoots = []
        self.delay_between_shoots = 0


    def create_new_shoot(self,x,y): 
        self.delay_between_shoots += 1
        new_bullet = Bullet(self.surface).create_shoot(x,y)
        self.list_rect_shoots.append(new_bullet)


    def can_shoot(self):
        if self.delay_between_shoots != 0 and self.delay_between_shoots <= 30:
            self.delay_between_shoots += 1
            return False
        else:
            self.delay_between_shoots = 0
            return True


    def move_all_shoots(self):
        for i in self.list_rect_shoots:
            i.movement_shoot()
            self.__destroy_bullet_depens_screen(i)
            

    def __destroy_bullet_depens_screen(self,bullet: Bullet): 
        if bullet.rect_bullet.y <= 0:
            self.__destroy_bullet(bullet)


    def __destroy_bullet(self,bullet):
        self.list_rect_shoots.remove(bullet)
        del bullet