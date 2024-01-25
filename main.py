import pygame
import player_class
import draw_function

WIDTH, HEIGHT = 1000, 800
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Super Smash Python")

BG = pygame.transform.scale(pygame.image.load("python_game_bg_img.png"), (WIDTH, HEIGHT))





def main():

    run = True

    time_passed = 0
            

    # This sets the attriibutes for player1 to have
    player1 = player_class.player(200, 72, 102, 'mario_sprites.png')
    player2 = player_class.player(500, 48, 114, 'luigi_sprites.png')

    import sprite_class


    # Sets the frames per second that the program will run, so it is the same on all devices
    CLOCK = pygame.time.Clock()

    

    while run:

        # This sets the frames per second to 60 fps
        CLOCK.tick(60)


        # This is so the user can close the tab
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break



        # This is to take user imput for player1

        keys = pygame.key.get_pressed()

        
            
        # All of this code is for gravity
            
        if keys[pygame.K_w] and player1.in_air == False:
            player1.in_air = True
        
        # This function is responsible for the quadritic motion of the player
        if player1.in_air == True and player1.y <= HEIGHT - player1.height:
            player1.jump_vel -= 2
            player1.y -= player1.jump_vel
        
        # This function resets the player's jump stats to normal when the player reached the ground
        if HEIGHT - player1.height < player1.y and player1.in_air == True:
            player1.y = HEIGHT - player1.height
            player1.jump_vel = 40
            player1.in_air = False


        
        


        # All of this code is for gravity
            
        if keys[pygame.K_UP] and player2.in_air == False:
            player2.in_air = True
        
        # This function is responsible for the quadritic motion of the player
        if player2.in_air == True and player2.y <= HEIGHT - player2.height:
            player2.jump_vel -= 2
            player2.y -= player2.jump_vel
        
        # This function resets the player's jump stats to normal when the player reached the ground
        if HEIGHT - player2.height < player2.y and player2.in_air == True:
            player2.y = HEIGHT - player2.height
            player2.jump_vel = 40
            player2.in_air = False

            
        

        # This function calls a few classes for all of the objects on screen and puts it into the draw function
        draw_function.draw(time_passed, keys, player1, player2)
        
    
    
    pygame.quit()


# Calls the game to run
if __name__ == "__main__":
    main()