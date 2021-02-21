import pygame
import random
import ConfigurationCharger
from BulletManagement import Disparo

class PrincipalShip: 
    
    start_w = 20 
    coordinates_ship = []

    def __init__(self,Config):
        self.surface = Config.GetShipSurface()
        self.height_screen = Config.GetHeightScreen() 
        self.width_screen = Config.GetWidthScreen() 
        self.speed = 5

        self.principal_color = (37,183,230,255)
        self.secondary_color = (158,194,228,255)
        self.color_ship = self.principal_color

        self.saveCoordinatesShipt(self.start_w,self.height_screen-40)
        
        self._createShipt(self.coordinates_ship[0][0],self.coordinates_ship[0][1],self.principal_color)

        
    def saveCoordinatesShipt(self,x,y):
        self.coordinates_ship.append([x,y])

    # Create principal ship
    def _createShipt(self,x,y,color):  

        pygame.draw.rect(self.surface, 
            color, 
            (x, y, 110, 25), 
            border_top_left_radius=7, 
            border_top_right_radius=7, 
            border_bottom_left_radius=2, 
            border_bottom_right_radius=2)

        pygame.draw.rect(self.surface, 
            color, 
            (x + 30, y - 15, 50, 20), 
            border_top_left_radius=7, 
            border_top_right_radius=7)

        pygame.draw.rect(self.surface, 
            color, 
            (x + 50, y - 25, 10, 10), 
            border_top_left_radius=60, 
            border_top_right_radius=60)
            

    def repaint_ship(self): 
        self._createShipt(self.coordinates_ship[0][0],self.coordinates_ship[0][1],self.principal_color)
      
    def shipMovement(self):
        if pygame.key.get_pressed()[pygame.K_a] or pygame.key.get_pressed()[pygame.K_LEFT]:
            if self._can_move_left():
                self._move_ship_left()

        if pygame.key.get_pressed()[pygame.K_d] or pygame.key.get_pressed()[pygame.K_RIGHT]:
            if self._can_move_right():
                self._move_ship_right()


    def _move_ship_right(self):
        self.coordinates_ship[0][0] += self.speed
        self._createShipt(self.coordinates_ship[0][0]-5,self.coordinates_ship[0][1],self.secondary_color)
        self._createShipt(self.coordinates_ship[0][0],self.coordinates_ship[0][1],self.principal_color)
        


    def _move_ship_left(self):
        self.coordinates_ship[0][0] -= self.speed
        self._createShipt(self.coordinates_ship[0][0]+5,self.coordinates_ship[0][1],self.secondary_color)
        self._createShipt(self.coordinates_ship[0][0],self.coordinates_ship[0][1],self.principal_color)
        


    def _can_move_left(self):
        if self.coordinates_ship[0][0] >= 0:
            return True
        else: 
            return False

    def _can_move_right(self):
        if self.coordinates_ship[0][0] <= self.width_screen - 100:
            return True
        else: 
            return False
        
            
    def shipShooting(self, shoot):
        if pygame.key.get_pressed()[pygame.K_SPACE]:
            shoot.createShoot(self.coordinates_ship[0][0],self.coordinates_ship[0][1])
