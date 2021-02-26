from pygame.draw import rect
from pygame import Rect

class BulletMonster:

    def __init__(self, surface):
        self.surface = surface
        self.rect_bullet = object
        self._shootSpeed = 5
        self.color_bullet_monster = (255,0,0,255)

    def create_shoot(self,x,y):    
        self.rect_bullet = rect(self.surface, self.color_bullet_monster, (x+20, y+30, 5,10))
        return self

    def movement_shoot_monster(self):
        self.rect_bullet = Rect.move(self.rect_bullet,0,self._shootSpeed)
        rect(self.surface, self.color_bullet_monster, self.rect_bullet)

    def get_rect_of_bullet(self):
        return self.rect_bullet


