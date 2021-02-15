import pygame
import random
from ConfigurationCharger import ChargeConfigurationClass
class PrincipalShip: 
    
    start_w = 20 
    coordinates_ship = []

    def __init__(self,surface,h,w,speed):
        self.surface = surface
        self.h = h 
        self.w = w
        self.speed = speed

        self.saveCoordinatesShipt(self.start_w,self.h-40)
        self.createShipt()

        
    def saveCoordinatesShipt(self,x,y):
        self.coordinates_ship.append([x,y])


    # Create principal ship
    def createShipt(self):  
        randomColor1 = random.uniform(20,255)
        randomColor2 = random.uniform(20,255)
        randomColor3 = random.uniform(20,255)
        self.color = (randomColor1,randomColor2,randomColor3,255)

        x = self.coordinates_ship[0][0]
        y = self.coordinates_ship[0][1]

        pygame.draw.rect(self.surface, 
            self.color, 
            (x, y, 110, 30), 
            border_top_left_radius=10, 
            border_top_right_radius=10, 
            border_bottom_left_radius=2, 
            border_bottom_right_radius=2)

        pygame.draw.rect(self.surface, 
            self.color, 
            (x + 30, y - 15, 50, 20), 
            border_top_left_radius=10, 
            border_top_right_radius=10)

        pygame.draw.rect(self.surface, 
            self.color, 
            (x + 50, y - 25, 10, 10), 
            border_top_left_radius=60, 
            border_top_right_radius=60)
        

            
    def shipMovement(self):
        if pygame.key.get_pressed()[pygame.K_a] or pygame.key.get_pressed()[pygame.K_LEFT]:
            self.surface.fill((0,0,0,255))
            self._move_ship_left()

        if pygame.key.get_pressed()[pygame.K_d] or pygame.key.get_pressed()[pygame.K_RIGHT]:
            self.surface.fill((0,0,0,255))
            self._move_ship_right()


    def _move_ship_right(self):
        self.coordinates_ship[0][0] += self.speed
        self.createShipt()


    def _move_ship_left(self):
        self.coordinates_ship[0][0] -= self.speed
        self.createShipt()

            
    def shipShooting(self):
        if pygame.key.get_pressed()[pygame.K_SPACE]:
            print('disparo')