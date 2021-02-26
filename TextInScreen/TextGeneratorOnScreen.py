from ConfigurationCharger import ChargeConfigurationClass
import pygame



class TextoGenerico(): 

    def __init__(self, configuration: ChargeConfigurationClass):
        
        self.color_white = (255, 255, 255)
        self.surface = configuration.get_principal_surface()
        self.height = configuration.GetHeightScreen()
        self.width = configuration.GetWidthScreen()
        self.puntuacion = 0 
        self.font = pygame.font.Font('freesansbold.ttf', 32)



    def paint_concrete_text(self,string):    
        text = self.font.render(string, True, self.color_white)
        self.surface.blit(text, (10,10))

    def paint_user_score(self,score): 
        text = self.font.render(score, True, self.color_white)
        self.surface.blit(text, (self.width-100,10))
