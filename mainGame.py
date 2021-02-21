
import pygame
import random
from pygame import draw

from CreateStars import CreateStarsInSeparateScreens
from ConfigurationCharger import ChargeConfigurationClass
from ShipMagamenet import PrincipalShip
from Bullets.BulletManagement import BulletManagement
from Monsters.MonsterManager import MonsterManager

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
BulletsManagement = BulletManagement(Configuration.GetShootSurface())

#Create enemies 
MonsterController = MonsterManager(Configuration)  



def repaintAllelementsInTheScreen():
    screen.fill(black)
    Configuration.GetShootSurface().fill(black)
    Configuration.GetShipSurface().fill(black)
    Configuration.GetMonsterSurface().fill(black)

    Ship.repaint_ship()
    MonsterController.repaint_monsters()

def checkMovementsAndExecuteIt(): 
    Ship.shipMovement()
    BulletsManagement.move_all_shoots()
    MonsterController.monster_movement()

    if BulletsManagement.canShoot():
        Ship.shipShooting(BulletsManagement)


def blitAllElements(): 
    for surface_on_screen in Configuration.GetTotalSurfaces():
        screen.blit(surface_on_screen, (0,0))   


# GameLoop
while GameRunning:
    
    # Draw
    repaintAllelementsInTheScreen()

    # Inputs and movements
    checkMovementsAndExecuteIt()

    
    #MonsterController.check_shoot_contact_monster(Shoot.get_shoots())


    # Draw imagens "onto" anothers (blit)   
    blitAllElements()

    # Exit game
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            GameRunning = False
    
    
    #End Loop
    pygame.display.update()
    pygame.display.flip()
    fpsClock.tick(30)

pygame.quit()   