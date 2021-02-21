import pygame
import random

class Disparo:
    

    def __init__(self, surface):
        self.surface = surface

        self.listCoordinatesShoots = []
        self.shootSpeed = 10
        self.delayShoot = 0
        self.correction_x = 50
        self.correction_y = 40
  
    def createShoot(self,x,y):    
        self.delayShoot += 1
        pygame.draw.rect(self.surface, (111,111,244,255), (x + self.correction_x, y - self.correction_y, 10,20))
        self.listCoordinatesShoots.append([x,y])
        
    def repainShoot(self):
        if len(self.listCoordinatesShoots) > 0:
            try:
                for i in range(len(self.listCoordinatesShoots)):

                    x = self.listCoordinatesShoots[i][0] + self.correction_x
                    y = self.listCoordinatesShoots[i][1] - self.correction_y

                    C1 = random.uniform(20,255)
                    C2 = random.uniform(20,255)
                    C3 = random.uniform(20,255)

                    pygame.draw.rect(self.surface, (C1,C2,C3,255), (x, y, 10,20))
            except:
                pass   

    def moveShoots(self):
        
        if len(self.listCoordinatesShoots) > 0:
            try:
                for i in range(len(self.listCoordinatesShoots)):
                    self.listCoordinatesShoots[i][1] -= self.shootSpeed
                            
                    x = self.listCoordinatesShoots[i][0]
                    y = self.listCoordinatesShoots[i][1]

                    if y < - 20:
                        del self.listCoordinatesShoots[i]
            except:
                pass   
        
    def canShoot(self):
        if self.delayShoot != 0 and self.delayShoot <= 20:
            self.delayShoot += 1
            return False
        else:
            self.delayShoot = 0
            return True
    