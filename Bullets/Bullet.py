from pygame.draw import rect
from pygame import Rect
import random

class Bullet:

    def __init__(self, surface):
        self.surface = surface
        self.rect_bullet = object
        self._shootSpeed = -8

    def create_shoot(self,x,y):    
        C1 = random.uniform(20,235)
        C2 = random.uniform(20,235)
        C3 = random.uniform(20,235)
        self.rect_bullet = rect(self.surface, (C1,C2,C3,255), (x + 50, y - 40, 10,20))
        return self

    def movement_shoot(self):
        C1 = random.uniform(20,235)
        C2 = random.uniform(20,235)
        C3 = random.uniform(20,235)
        self.rect_bullet = Rect.move(self.rect_bullet,0,self._shootSpeed)
        rect(self.surface, (C1,C2,C3,255), self.rect_bullet)
                