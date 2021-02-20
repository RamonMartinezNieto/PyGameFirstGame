import pygame
import random
from pygame import draw

from CreateStars import CreateStarsInSeparateScreens
from ConfigurationCharger import ChargeConfigurationClass
from ShipMagamenet import PrincipalShip
from BulletManagement import Disparo

# Variables
GameRunning = True
black = (0,0,0,255)
height_screen = 0 
width_screen = 0 


# Init PayGame 
pygame.init()
fpsClock = pygame.time.Clock()

# Charge configurations
Configuration = ChargeConfigurationClass() 
height_screen = Configuration.GetHeightScreen()
width_screen = Configuration.GetWidthScreen()

# Create screen
screen = pygame.display.set_mode([width_screen,height_screen])

# Stars for the background 
Stars = CreateStarsInSeparateScreens(Configuration)
Stars.createRandomStars()

# Create principal ship & Control Bullets
Ship = PrincipalShip(Configuration)
Shoot = Disparo(Configuration.GetShootSurface())


def repaintAllelementsInTheScreen():
    screen.fill(black)
    Configuration.GetShootSurface().fill(black)
    Configuration.GetShipSurface().fill(black)

    #Stars.repainStars()
    Ship.createShipt()
    Shoot.repainShoot()

def checkMovementsAndExecuteIt(): 
    Ship.shipMovement()
    Shoot.moveShoots()
    if Shoot.canShoot():
        Ship.shipShooting(Shoot)


def blitAllElements(): 
    screen.blit(Configuration.GetShootSurface(), (0,0))
    screen.blit(Configuration.GetShipSurface(), (0,0))

    for star in Stars.GetListStars():
        screen.blit(star, (0,0))

    

# GameLoop
while GameRunning:
    
    # Draw
    repaintAllelementsInTheScreen()

    # Inputs and movements
    checkMovementsAndExecuteIt()

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