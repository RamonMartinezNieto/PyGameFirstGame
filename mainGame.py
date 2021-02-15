import pygame
import random

from pygame.constants import K_a
from CreateStars import CreateStarsInSeparateScreens
from CreateSurfaces import createListOfSurfaces
from ConfigurationCharger import ChargeConfigurationClass
from CreatePrincipalShip import PrincipalShip

# Variables
height_screen = 0
width_screen = 0
total_surfaces = 0
listSurfaces = []
listStars = []
GameRunning = True

# Colors
black = (0,0,0,255)

# Init PayGame 
pygame.init()
fpsClock = pygame.time.Clock()

# Charge configurations
Configuration = ChargeConfigurationClass() 

height_screen = Configuration.GetHeightScreen()
width_screen = Configuration.GetWidthScreen()
total_surfaces = Configuration.GetTotalBackgroundSurfaces()

# Create screen and surfaces
screen = pygame.display.set_mode([width_screen,height_screen])
listSurfaces = createListOfSurfaces(total_surfaces,width_screen,height_screen)

# Stars for the background 
myStars = CreateStarsInSeparateScreens(height_screen,width_screen,listSurfaces) 
myStars.createRandomStars(total_surfaces)
listStars = myStars.giveListStars()

# Create principal ship
Ship = PrincipalShip(listSurfaces[0],height_screen,width_screen,5)


# GameLoop
while GameRunning:

    # Background
    screen.fill(black)

    # Ship Control
    Ship.shipMovement()
    Ship.shipShooting()

    # Exit game
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            GameRunning = False


    # Static elements
    for star in listStars:
        screen.blit(star[2], (0,0))
        

    #End Loop
    pygame.display.update()
    pygame.display.flip()
    fpsClock.tick(30)

pygame.quit()