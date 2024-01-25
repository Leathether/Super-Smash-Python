import pygame
import player_class
import main
class sprite_class():
    def __init__(self):
        animation_list = []
        animation_steps = 11
        last_update = pygame.time.get_ticks()
        anamation_cooldown = 500
        frame = 0
    def load_animations (self):
        for x in range(self.animation_steps):
            self.animation_list.append(player_class.player1.load_sprites())