#import pygame
from pygame.draw import rect
from pygame.key import get_pressed
from pygame import K_a
from pygame import K_LEFT
from pygame import K_d
from pygame import K_RIGHT
from pygame import K_SPACE
from ConfigurationCharger import ChargeConfigurationClass
from Bullets.BulletManagement import BulletManagement

class PrincipalShip: 
    
    start_w = 20 
    coordinates_ship = []

    def __init__(self,Config: ChargeConfigurationClass):
        self.surface = Config.get_principal_surface()
        self.height_screen = Config.GetHeightScreen() 
        self.width_screen = Config.GetWidthScreen() 
        self.speed = 5

        self.principal_color = (37,183,230,255)
        self.secondary_color = (158,194,228,255)
        self.color_ship = self.principal_color

        self.save_coordinates_ship(self.start_w,self.height_screen-40)
        
        self._create_ship(self.coordinates_ship[0][0],self.coordinates_ship[0][1],self.principal_color)

        
    def save_coordinates_ship(self,x,y):
        self.coordinates_ship.append([x,y])

    # Create principal ship
    def _create_ship(self,x,y,color):  
        
        rect(self.surface, 
            color, 
            (x, y, 110, 25), 
            border_top_left_radius=5, 
            border_top_right_radius=5, 
            border_bottom_left_radius=2, 
            border_bottom_right_radius=2)

        rect(self.surface, 
            color, 
            (x + 30, y - 15, 50, 20), 
            border_top_left_radius=5, 
            border_top_right_radius=5)

        rect(self.surface, 
            color, 
            (x + 50, y - 25, 10, 10), 
            border_top_left_radius=60, 
            border_top_right_radius=60)
            

    def repaint_ship(self): 
        self._create_ship(self.coordinates_ship[0][0],self.coordinates_ship[0][1],self.principal_color)
      

    def check_inputs_movement_ship(self):
        if get_pressed()[K_a] or get_pressed()[K_LEFT]:
            if self._can_move_left():
                self._move_ship_left()

        if get_pressed()[K_d] or get_pressed()[K_RIGHT]:
            if self._can_move_right():
                self._move_ship_right()


    def _move_ship_right(self):
        self.coordinates_ship[0][0] += self.speed
        self._create_ship(self.coordinates_ship[0][0]-5,self.coordinates_ship[0][1],self.secondary_color)
        self._create_ship(self.coordinates_ship[0][0],self.coordinates_ship[0][1],self.principal_color)
        


    def _move_ship_left(self):
        self.coordinates_ship[0][0] -= self.speed
        self._create_ship(self.coordinates_ship[0][0]+5,self.coordinates_ship[0][1],self.secondary_color)
        self._create_ship(self.coordinates_ship[0][0],self.coordinates_ship[0][1],self.principal_color)
        


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
        
            
    def shipShooting(self, bullet_management: BulletManagement):
        if get_pressed()[K_SPACE]:
            bullet_management.create_new_shoot(self.coordinates_ship[0][0],self.coordinates_ship[0][1])
