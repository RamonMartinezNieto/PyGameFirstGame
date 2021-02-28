import pygame
from CreateStars import CreateStarsInSeparateScreens
from ConfigurationCharger import ChargeConfigurationClass
from Bullets.BulletManagement import BulletManagement
from Monsters.MonsterManager import MonsterManager
from ShipMagamenet import PrincipalShip
from TextInScreen.TextGeneratorOnScreen import TextoGenerico
from Score import ScorePlayer
from Button import GenericButton

# Global (?) Variables
GameRunning = True
GameWin = False
GameOver = False
black = (0,0,0,255)
height_screen = 0 
width_screen = 0 

# Init PayGame 
pygame.init()
fpsClock = pygame.time.Clock()

# Charge configurations
Configuration = ChargeConfigurationClass() 

# Create screen
screen = pygame.display.set_mode([Configuration.GetWidthScreen(),Configuration.GetHeightScreen()])

CurrentScore = ScorePlayer()
TextoGenericoBien = TextoGenerico(screen, Configuration.get_principal_surface())
CurrentScorePlayer = ScorePlayer()
ButtonPlayGen = GenericButton(Configuration.GetHeightScreen()//2,Configuration.GetWidthScreen()//2,"Botoncico",Configuration.get_principal_surface(),screen)

# Stars for the background 
Stars = CreateStarsInSeparateScreens(Configuration)
Stars.createRandomStars()

# Create principal ship & Control Bullets
Ship = PrincipalShip(Configuration)
BulletsManagement = BulletManagement(Configuration.get_principal_surface())

#Create enemies 
MonsterController = MonsterManager(Configuration)  

def reset_game(): 
    global GameOver
    global GameWin
    GameWin = False
    GameOver = False
    CurrentScorePlayer.reset_score_player()
    #Stars.reset_stars()
    Ship.reset_ship()
    BulletsManagement.reset_bullets()
    MonsterController.reset_monsters()


def repaint_all_elements_in_screen():
    screen.fill(black)
    Configuration.get_principal_surface().fill(black)
    Ship.repaint_ship()
    Ship.paint_mini_ships()
    MonsterController.repaint_monsters()
    TextoGenericoBien.paint_player_text('PlayerName')
    TextoGenericoBien.paint_concrete_text(str(Ship.lives_ship),10,Configuration.GetHeightScreen()-40,24)
    TextoGenericoBien.paint_user_score(CurrentScorePlayer.get_score_like_string())

def check_movements_inputs_and_execute_it(): 
    Ship.check_inputs_movement_ship()
    BulletsManagement.move_all_shoots()
    BulletsManagement.move_all_enemy_shoots()
    MonsterController.monster_movement()

    if BulletsManagement.can_shoot():
        Ship.shipShooting(BulletsManagement)


def blit_all_elements(): 
    for surface_on_screen in Configuration.GetTotalSurfaces():
        screen.blit(surface_on_screen, (0,0))   

def shoot_controller(): 
    global GameOver

    #Check colision between bullets and monsters
    BulletsManagement.check_collider_bullet_contact(MonsterController, CurrentScorePlayer)
    BulletsManagement.enemy_shooting_bullets(MonsterController)
    if Ship.check_bullet_contact_monster_to_ship(BulletsManagement):
        GameOver = True
        

def button_play_win_and_game_over(text):
    # Game Over Screen
    #Background Text + GameOver Text
    TextoGenericoBien.paint_concrete_text(text,60,(Configuration.GetHeightScreen()//2)-145,78,(255,0,0,255))
    TextoGenericoBien.paint_concrete_text(text,60,(Configuration.GetHeightScreen()//2)-140,80)

    if not ButtonPlayGen.check_button_hover():
        ButtonPlayGen.new_button('Play') 
    else: 
        ButtonPlayGen.new_button('Play',5,5)

# GameLoop
while GameRunning:

    # Draw
    repaint_all_elements_in_screen()
    
    if not GameOver and not GameWin:
        # Playing 
        # Inputs and movements
        check_movements_inputs_and_execute_it()

        shoot_controller()
        
        if not GameOver:
            GameWin = MonsterController.check_if_you_win()
            GameOver = MonsterController.check_if_you_loss()
        
    elif GameWin: 
        button_play_win_and_game_over('   YOU WIN  ')

    elif GameOver:
        button_play_win_and_game_over('GAME OVER')

    # Draw imagens "onto" anothers (blit)   
    blit_all_elements()

    # Exit game
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            GameRunning = False
        if (GameOver or GameWin) and event.type == pygame.MOUSEBUTTONDOWN:
                if ButtonPlayGen.click_button_play():
                    reset_game()

    #End Loopd
    pygame.display.update()
    pygame.display.flip()
    fpsClock.tick(60)
