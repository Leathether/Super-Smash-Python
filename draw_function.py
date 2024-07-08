import pygame
import main

def draw(time_passed, keys, player1, player2):
    main.WIN.blit(main.BG, (0,0))



    #draws hitbox for player1
    pygame.draw.rect(main.WIN, "blue", player1.create_player())


    # first sees if the player is in air to do animation
    if player1.in_air == False:
        # this is to avoid the side animation playing aswell
        if ((not keys[pygame.K_a] and not keys[pygame.K_d]) or (keys[pygame.K_a] and keys[pygame.K_d])) and player1.atking == False:
            player1.side_vel = 1
            player1.idle(2, 41, 23, 34, 25, 3)
    else:
        # player1.jump(x, y, width, height, scale)
        player1.jump(64, 325, 20, 36, 3)


    # P1 move to the left speed up
    if keys[pygame.K_a] and not keys[pygame.K_d]:
        player1.direction = "L"
        player1.walk_func()
        # player1.walk(x, y, width, height, distance, scale)
        if player1.in_air == False:
            player1.walk_anime(0, 228, 24, 34, 25, 3)
    
    # P1 move to the right speed up
    if keys[pygame.K_d] and not keys[pygame.K_a]:
        player1.direction = "R"
        player1.walk_func()
        # player1.walk(x, y, width, height, distance, scale)
        if player1.in_air == False:
            player1.walk_anime(0, 228, 24, 34, 25, 3)
    




    pygame.draw.rect(main.WIN, "purple", player2.create_player())

    #first sees if the player is in the air to do animation
    if player2.in_air == False:
        if (not keys[pygame.K_LEFT] and not keys[pygame.K_RIGHT]) or (keys[pygame.K_RIGHT] and keys[pygame.K_LEFT]):
            player2.side_vel = 1
            player2.idle(9, 37, 16, 38, 20, 3)
    else:
        # player2.jump(x, y, width, height, scale)
        player2.jump(8, 508, 24, 38, 3)


    # This is to take the input for player2
    # P2 move to the left
    if keys[pygame.K_LEFT] and not keys[pygame.K_RIGHT]:
        player2.direction = "L"
        player2.walk_func()
        # prevents double animations
        if player2.in_air == False:
            # player2.walk(x, y, width, height, scale)
            player2.walk_anime(8, 236, 16, 38, 20, 3)
    
    # P2 move to the right
    if keys[pygame.K_RIGHT] and not keys[pygame.K_LEFT]:
        player2.direction = "R"
        player2.walk_func()
        # prevents double animations
        if player2.in_air == False:
            # player2.walk(x, y, width, height, scale)
            player2.walk_anime(8, 236, 16, 38, 20, 3)

    


    
    # This is attack function
    if keys[pygame.K_f]:
        if player1.in_air == False:
            # player1.grd_atk(x, y, width, height, distance, scale)
            player1.grd_atk(8, 540, 40, 80, 40, 3)

    if keys[pygame.K_SLASH]:
        pass

    pygame.display.update()