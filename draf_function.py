import pygame
import main

def draw(time_passed, keys, player1, player2):
    main.WIN.blit(BG, (0,0))

    pygame.draw.rect(WIN, "blue", player1.create_player())
    p1f0_idle = player1.load_sprites(3, 35, 28, 45, 2)
    main.WIN.blit(p1f0_idle, (player1.x, player1.y))
    pygame.draw.rect(WIN, "purple", player2.create_player())
    
    if keys[pygame.K_f]:
        if(time_passed - player1.last_atk >= 40):
            if(player1.direction == "L"):               
                pygame.draw.rect(WIN, "red", player1.atk_left())
                player1.last_atk = time_passed
            
            else:
                pygame.draw.rect(WIN, "red", player1.atk_right())
                player1.last_atk = time_passed

    if keys[pygame.K_SLASH]:
        if(time_passed - player2.last_atk >= 40):
            if(player2.direction == "L"):               
                pygame.draw.rect(WIN, "red", player2.atk_left())
                player2.last_atk = time_passed
            
            else:
                pygame.draw.rect(WIN, "red", player2.atk_right())
                player2.last_atk = time_passed

    pygame.display.update()