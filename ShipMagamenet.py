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
        self.color_ship = (123,123,123,255)

        self.saveCoordinatesShipt(self.start_w,self.height_screen-40)
        
        self.createShipt()

        
    def saveCoordinatesShipt(self,x,y):
        self.coordinates_ship.append([x,y])

    # Create principal ship
    def createShipt(self):  
        x = self.coordinates_ship[0][0]
        y = self.coordinates_ship[0][1]

        pygame.draw.rect(self.surface, 
            self.color_ship, 
            (x, y, 110, 30), 
            border_top_left_radius=10, 
            border_top_right_radius=10, 
            border_bottom_left_radius=2, 
            border_bottom_right_radius=2)

        pygame.draw.rect(self.surface, 
            self.color_ship, 
            (x + 30, y - 15, 50, 20), 
            border_top_left_radius=10, 
            border_top_right_radius=10)

        pygame.draw.rect(self.surface, 
            self.color_ship, 
            (x + 50, y - 25, 10, 10), 
            border_top_left_radius=60, 
            border_top_right_radius=60)
        

            
    def shipMovement(self):
        if pygame.key.get_pressed()[pygame.K_a] or pygame.key.get_pressed()[pygame.K_LEFT]:
            if self._can_move_left():
                self._move_ship_left()

        if pygame.key.get_pressed()[pygame.K_d] or pygame.key.get_pressed()[pygame.K_RIGHT]:
            if self._can_move_right():
                self._move_ship_right()


    def _move_ship_right(self):
        self.coordinates_ship[0][0] += self.speed
        self.createShipt()


    def _move_ship_left(self):
        self.coordinates_ship[0][0] -= self.speed
        self.createShipt()


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
