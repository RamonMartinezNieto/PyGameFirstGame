import pygame

class TextoGenerico(): 

    def __init__(self, screen, surface):
        
        self.color_white = (255, 255, 255)
        self.surface = surface
        self.width = screen.get_width()

    def paint_player_text(self,string):
        self.paint_concrete_text(string,10,10,24)    
    
    def paint_user_score(self,score): 
        self.paint_concrete_text(score,self.width-100,10,24)    

    def paint_concrete_text(self,text,x,y,size_font,color = (255, 255, 255)):
        self.font = pygame.font.Font('resources///space_invaders.ttf', size_font)
        text = self.font.render(text, True, color)
        self.surface.blit(text, (x,y))

        