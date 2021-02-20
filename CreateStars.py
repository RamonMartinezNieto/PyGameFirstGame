import pygame
import random
import ConfigurationCharger

class CreateStarsInSeparateScreens:

    def __init__(self, Configuration):
        self.starsList = []

        self.back_stars = Configuration.GetTotalBackgroundStars()
        self.stars_per_surf = Configuration.GetStarsPerSurface()
        self.quantity = Configuration.GetTotalBackgroundStars()
        self.height = Configuration.GetHeightScreen()
        self.widht = Configuration.GetWidthScreen()
        self.surface_stars_list = Configuration.GetStarsSurfaces()
        
        print(self.surface_stars_list.count)

        self.max_stars = 50;


    def createRandomStars(self):
        secure_random = random.SystemRandom()
        for i in range(self.back_stars//self.stars_per_surf):
            if i <= self.max_stars:
                for a in range(self.stars_per_surf):
                    H_random = secure_random.uniform(15,self.height-105)
                    W_random = secure_random.uniform(15,self.widht-15)

                    self.starsList.append([H_random,W_random,self.surface_stars_list[i]])
                    self.createStar(H_random,W_random,self.surface_stars_list[i])

    # This is only one star
    def createStar(self,H_random,W_random,surface):    
        pygame.draw.circle(surface, (10,10,10,0), (W_random, H_random), 7)
        pygame.draw.circle(surface, (25,25,25,40), (W_random, H_random), 6)
        pygame.draw.circle(surface, (55,55,55,80), (W_random, H_random), 5)
        pygame.draw.circle(surface, (100,100,100,130), (W_random, H_random), 4)
        pygame.draw.circle(surface, (155,155,155,180), (W_random, H_random), 3)
        pygame.draw.circle(surface, (222,222,222,220), (W_random, H_random), 2)
        pygame.draw.circle(surface, (255,255,255,255), (W_random, H_random), 1)

    def GetListStars(self):
        list_surfaces = list(self.starsList[i][2] for i in range(len(self.starsList)))
        return list_surfaces

            
    def repainStars(self):
        if len(self.starsList) > 0:
            try:
                for i in range(len(self.starsList)):
                    self.createStar(self.starsList[0][0],self.starsList[0][1],self.starsList[0][2])
            except:
                pass 
