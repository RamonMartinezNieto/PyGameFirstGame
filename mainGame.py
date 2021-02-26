import pygame

from CreateStars import CreateStarsInSeparateScreens
from ConfigurationCharger import ChargeConfigurationClass
from Bullets.BulletManagement import BulletManagement
from Monsters.MonsterManager import MonsterManager
from ShipMagamenet import PrincipalShip


# Global (?) Variables
GameRunning = True
black = (0,0,0,255)
height_screen = 0 
width_screen = 0 

# Init PayGame 
pygame.init()
fpsClock = pygame.time.Clock()

# Charge configurations
Configuration = ChargeConfigurationClass() 

# Create screen
screen = pygame.display.set_mode([Configuration.GetWidthScreen(),Configuration.GetHeightScreen()])

# Stars for the background 
Stars = CreateStarsInSeparateScreens(Configuration)
Stars.createRandomStars()

# Create principal ship & Control Bullets
Ship = PrincipalShip(Configuration)
BulletsManagement = BulletManagement(Configuration.get_principal_surface())

#Create enemies 
MonsterController = MonsterManager(Configuration)  

def repaint_all_elements_in_screen():
    screen.fill(black)
    Configuration.get_principal_surface().fill(black)
    Ship.repaint_ship()
    MonsterController.repaint_monsters()

def check_movements_inputs_and_execute_it(): 
    Ship.check_inputs_movement_ship()
    BulletsManagement.move_all_shoots()
    MonsterController.monster_movement()

    if BulletsManagement.can_shoot():
        Ship.shipShooting(BulletsManagement)


def blit_all_elements(): 
    for surface_on_screen in Configuration.GetTotalSurfaces():
        screen.blit(surface_on_screen, (0,0))   


# GameLoop
while GameRunning:
      
    # Draw
    repaint_all_elements_in_screen()

    # Inputs and movements
    check_movements_inputs_and_execute_it()
     
    BulletsManagement.check_collider_bullet_contact(MonsterController)

    # Draw imagens "onto" anothers (blit)   
    blit_all_elements()

    # Exit game
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            GameRunning = False
    
    #End Loop
    pygame.display.update()
    pygame.display.flip()
    fpsClock.tick(60)

pygame.quit()   