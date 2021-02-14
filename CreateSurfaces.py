import pygame

def createListOfSurfaces(quantity, widthScreen, heightScreen):

    listSurfaces = []    
    if quantity > 30: 
        raise Exception('No more than 30 is allowed')

    for i in range(quantity):
        listSurfaces.append(pygame.Surface((widthScreen,heightScreen), pygame.SRCALPHA))

    return listSurfaces
