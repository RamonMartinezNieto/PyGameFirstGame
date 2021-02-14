import pygame
import random

class CreateStarsInSeparateScreens:
    

    def __init__(self, heightScreen, weightScreen, surfaceList):
        self.starsList = []
        self.surfaceList = surfaceList
        self.WEIGHT_SCREEN = weightScreen
        self.HEIGHT_SCREEN = heightScreen

    def createRandomStars(self,quantity):
        secure_random = random.SystemRandom()

        for i in range(quantity):
            if quantity > 30: 
                raise Exception('No more than 30 is allowed')

            H_random = secure_random.uniform(15,self.HEIGHT_SCREEN-15)
            W_random = secure_random.uniform(15,self.WEIGHT_SCREEN-15)
            
            self.starsList.append([H_random,W_random,self.surfaceList[i]])
            self.createStar(H_random,W_random,self.surfaceList[i])

    # This is only one star
    def createStar(self,H_random,W_random,surface):    
        pygame.draw.circle(surface, (10,10,10,0), (W_random, H_random), 7)
        pygame.draw.circle(surface, (25,25,25,40), (W_random, H_random), 6)
        pygame.draw.circle(surface, (55,55,55,80), (W_random, H_random), 5)
        pygame.draw.circle(surface, (100,100,100,130), (W_random, H_random), 4)
        pygame.draw.circle(surface, (155,155,155,180), (W_random, H_random), 3)
        pygame.draw.circle(surface, (222,222,222,220), (W_random, H_random), 2)
        pygame.draw.circle(surface, (255,255,255,255), (W_random, H_random), 1)

    def giveListStars(self):
        return self.starsList