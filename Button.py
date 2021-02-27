from pygame import surface
from pygame.draw import rect
from pygame.surface import Surface
from pygame import Surface 
from pygame import Rect 
import pygame 
from TextInScreen.TextGeneratorOnScreen import TextoGenerico

class GenericButton(): 

    def __init__(self, x, y, text, surface: Surface, screen): 
        self.height_button = 230
        self.width_button = 75

        self.x = x 
        self.y = y - (self.height_button//2) 
      
        self.text = text
        self.surface = surface
        self.rect_button = Rect
        self.screen = screen
        self.hover = False

        self.color_background_button = (255,255,255,255)
        self.color_front_button = (21,185,165,255)
        self.color_hover_button = (185,165,21,255)

    def new_button(self,text,y_correction=0,x_correction=0): 

        if not self.hover:
            self.draw_background_button(self.color_background_button)
            self.rect_button = self.draw_button(self.color_front_button,y_correction,x_correction)
            self.text_button_show(text,40,11)
        else: 
            self.draw_background_button(self.color_background_button)
            self.rect_button = self.draw_button(self.color_hover_button,y_correction,x_correction)
            self.text_button_show(text,49,20)

        

    def text_button_show(self,text,h_correction,w_correction):
        texto_boton = TextoGenerico(self.screen,self.surface)
        texto_boton.paint_concrete_text(text,self.y + (self.height_button//2-h_correction),self.x + (self.width_button//2-w_correction),28)

    def draw_button(self,color,y_correction=0,x_correction=0): 
        #Background button
        return rect(
            self.surface, 
            color, 
            (self.y-y_correction,self.x-x_correction,self.height_button,self.width_button),
            border_radius=10)

    def draw_background_button(self,color):
            rect(
            self.surface,
            color, 
            (self.y-8,self.x-8,self.height_button,self.width_button),
            border_radius=10)
    

    def check_button_hover(self): 
        mouse = pygame.mouse.get_pos() 
        if self.y <= mouse[0] <= self.y+self.height_button and self.x <= mouse[1] <= self.x+self.width_button: 
            self.hover = True
            return True
        else: 
            self.hover = False
            return False


    def click_button_play(self): 
        mouse = pygame.mouse.get_pos() 
        if self.y <= mouse[0] <= self.y+self.height_button and self.x <= mouse[1] <= self.x+self.width_button: 
            print('presionado play')
            return True