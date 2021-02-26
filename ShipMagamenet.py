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
    

    def __init__(self,Config: ChargeConfigurationClass):
        self.surface = Config.get_principal_surface()
        self.height_screen = Config.GetHeightScreen() 
        self.width_screen = Config.GetWidthScreen() 
        self.speed = 5
        self.coordinates_ship = []
        self.rect_list_ship = []
        self.mini_ships = []
        self.start_w = ( self.width_screen // 2 ) - 55
        self.lives_ship = 3
        self.principal_color = (37,183,230,255)
        self.secondary_color = (158,194,228,255)
        self.color_ship = self.principal_color

        self.save_coordinates_ship(self.start_w,self.height_screen-70)
        self._create_principal_ship(self.coordinates_ship[0][0],self.coordinates_ship[0][1],self.principal_color)
        
    def save_coordinates_ship(self,x,y):
        self.coordinates_ship.append([x,y])

    def _create_principal_ship(self,x,y,color):
        self.rect_list_ship.clear()

        rect_one, rect_two, rect_three = self._create_ship(x,y,color,1)

        self.rect_list_ship.append(rect_one)
        self.rect_list_ship.append(rect_two)
        self.rect_list_ship.append(rect_three)

    def _create_mini_ships_lives(self,x,y,color):
        self._create_ship(x,y,color,0.5)
    
    # Create principal ship
    def _create_ship(self,x,y,color,s):  

        rect_one = rect(self.surface, 
            color, 
            (x*s, y*s, 110*s, 25*s), 
            border_top_left_radius=5, 
            border_top_right_radius=5, 
            border_bottom_left_radius=2, 
            border_bottom_right_radius=2)

        rect_two = rect(self.surface, 
            color, 
            ((x + 30 )*s, (y - 15)*s, 50*s, 20*s), 
            border_top_left_radius=5, 
            border_top_right_radius=5)

        rect_trhee = rect(self.surface, 
            color, 
            ((x + 50)*s, (y - 25)*s, 10*s, 10*s), 
            border_top_left_radius=60, 
            border_top_right_radius=60)
            
        return rect_one, rect_two, rect_trhee        

    def repaint_ship(self): 
        self._create_principal_ship(self.coordinates_ship[0][0],self.coordinates_ship[0][1],self.principal_color)

    def paint_mini_ships(self):
        color_green = (0,255,0,255)
        x_correction = -535
        y_correction = 750
        for i in range(self.lives_ship):
            self._create_mini_ships_lives(self.width_screen+(x_correction+(i*135)),self.height_screen+y_correction,color_green)

    def check_inputs_movement_ship(self):
        if get_pressed()[K_a] or get_pressed()[K_LEFT]:
            if self._can_move_left():
                self._move_ship_left()

        if get_pressed()[K_d] or get_pressed()[K_RIGHT]:
            if self._can_move_right():
                self._move_ship_right()


    def _move_ship_right(self):
        self.coordinates_ship[0][0] += self.speed
        self._create_principal_ship(self.coordinates_ship[0][0]-5,self.coordinates_ship[0][1],self.secondary_color)
        self._create_principal_ship(self.coordinates_ship[0][0],self.coordinates_ship[0][1],self.principal_color)
        


    def _move_ship_left(self):
        self.coordinates_ship[0][0] -= self.speed
        self._create_principal_ship(self.coordinates_ship[0][0]+5,self.coordinates_ship[0][1],self.secondary_color)
        self._create_principal_ship(self.coordinates_ship[0][0],self.coordinates_ship[0][1],self.principal_color)
        


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

    def check_bullet_contact_monster_to_ship(self, bullet_manager: BulletManagement):
        for rects in self.rect_list_ship:
            for bullet in bullet_manager.list_bullets_shooted_monsters:
                if rects.colliderect(bullet.rect_bullet):
                    self.damage_ship()
                    bullet_manager.destroy_bullet_monster(bullet)
                    return True
        else: 
            return False

    def damage_ship(self):
        if self.lives_ship > 0:
            self.lives_ship -= 1
        else:
            print('GAME OVER !!!!!!!')