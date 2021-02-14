import pygame
import random
from CreateStars import CreateStarsInSeparateScreens
from CreateSurfaces import createListOfSurfaces
from ConfigurationCharger import ChargeConfigurationClass

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
total_surfaces = Configuration.GetTotalBackgroundStars()

# Create screen and surfaces
screen = pygame.display.set_mode([width_screen,height_screen])
listSurfaces = createListOfSurfaces(total_surfaces,width_screen,height_screen)

# Stars for the background 
myStars = CreateStarsInSeparateScreens(height_screen,width_screen,listSurfaces) 
myStars.createRandomStars(total_surfaces)
listStars = myStars.giveListStars()


# GameLoop
while GameRunning:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            GameRunning = False

    
    screen.fill(black)  #Black background
    
    for star in listStars:
        screen.blit(star[2], (0,0))

    pygame.display.flip()

    #pygame.display.update()
    #Ojo que sin el fps tick se dispara el consumo por ir a tope de FPS 
    fpsClock.tick(30)

pygame.quit()