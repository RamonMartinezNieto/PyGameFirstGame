from ConfigurationCharger import ChargeConfigurationClass
import pygame

class TextoGenerico(): 

    def __init__(self, configuration: ChargeConfigurationClass):
        
        self.color_white = (255, 255, 255)
        
        self.surface = configuration.get_principal_surface()
        self.width = configuration.GetWidthScreen()
        self.font = pygame.font.Font('resources///space_invaders.ttf', 24)

    def paint_player_text(self,string):
        self.paint_concrete_text(string,10,10)    
    
    def paint_user_score(self,score): 
        self.paint_concrete_text(score,self.width-100,10)    

    def paint_concrete_text(self,text,x,y):
        text = self.font.render(text, True, self.color_white)
        self.surface.blit(text, (x,y))
