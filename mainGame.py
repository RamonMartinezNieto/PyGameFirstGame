import pygame

from CreateStars import CreateStarsInSeparateScreens
from ConfigurationCharger import ChargeConfigurationClass
from Bullets.BulletManagement import BulletManagement
from Monsters.MonsterManager import MonsterManager
from ShipMagamenet import PrincipalShip
from TextInScreen.TextGeneratorOnScreen import TextoGenerico
from Score import ScorePlayer


# Global (?) Variables
GameRunning = True
black = (0,0,0,255)
height_screen = 0 
width_screen = 0 

# Init PayGame 
pygame.init()
fpsClock = pygame.time.Clock()

# Charge configurations
Configuration = ChargeConfigurationClass() 
CurrentScore = ScorePlayer()
TextoGenericoBien = TextoGenerico(Configuration)
CurrentScorePlayer = ScorePlayer()

# Create screen
screen = pygame.display.set_mode([Configuration.GetWidthScreen(),Configuration.GetHeightScreen()])

# Stars for the background 
Stars = CreateStarsInSeparateScreens(Configuration)
Stars.createRandomStars()

# Create principal ship & Control Bullets
Ship = PrincipalShip(Configuration)
BulletsManagement = BulletManagement(Configuration.get_principal_surface())

#Create enemies 
MonsterController = MonsterManager(Configuration)  


def repaint_all_elements_in_screen():
    screen.fill(black)
    Configuration.get_principal_surface().fill(black)
    Ship.repaint_ship()
    MonsterController.repaint_monsters()
    TextoGenericoBien.paint_concrete_text('PlayerName')
    TextoGenericoBien.paint_user_score(CurrentScorePlayer.get_score_like_string())

def check_movements_inputs_and_execute_it(): 
    Ship.check_inputs_movement_ship()
    BulletsManagement.move_all_shoots()
    MonsterController.monster_movement()

    if BulletsManagement.can_shoot():
        Ship.shipShooting(BulletsManagement)


def blit_all_elements(): 
    for surface_on_screen in Configuration.GetTotalSurfaces():
        screen.blit(surface_on_screen, (0,0))   


# GameLoop
while GameRunning:
    

    # Draw
    repaint_all_elements_in_screen()

    # Inputs and movements
    check_movements_inputs_and_execute_it()
    
    #Check colision between bullets and monsters
    BulletsManagement.check_collider_bullet_contact(MonsterController, CurrentScorePlayer)

    # Draw imagens "onto" anothers (blit)   
    blit_all_elements()

    # Exit game
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            GameRunning = False
    
    #End Loopd
    pygame.display.update()
    pygame.display.flip()
    fpsClock.tick(30)

pygame.quit()   