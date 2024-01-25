import pygame
import main

# Sets propeties for the player(s)
class player:
    def __init__(self, x, width, height, sprites):
        self.x = x
        self.y = 800 - height
        self.width = width
        self.height = height
        self.side_vel = 5
        self.jump_vel = 40
        self.in_air = False
        self.direction = 'R'
        self.bottom_hitbox = self.height/2
        self.hitbox_range = 40
        self.atking = False
        self.sprites = pygame.image.load(sprites).convert_alpha()
        self.background_sprites = '#8CC6FF'
        self.last_update = pygame.time.get_ticks()
        self.animation_cooldown = 5
        self.time_passed = 0
        self.frame = 0
    # draws the hitbox for the player every frame
    def create_player(self):
        return pygame.Rect(self.x, self.y, self.width, self.height)
    def atk_left(self):
        return pygame.Rect(int(self.x - self.hitbox_range), int(self.y), int(self.hitbox_range), int(self.bottom_hitbox))
    def atk_right(self):
        return pygame.Rect(int(self.x + self.width), int(self.y), int(self.hitbox_range), int(self.bottom_hitbox))
    # idle animations
    def idle(self, x, y, width, height, distance, scale):
        self.width = width * scale
        self.height = height * scale
        self.time_passed += 1
        self.idle_step = pygame.Surface((width, height))
        self.idle_step.blit(self.sprites, (0, 0), (x + self.frame * distance, y, width, height))
        self.idle_step = pygame.transform.scale_by(self.idle_step, scale)
        self.idle_step.set_colorkey(self.background_sprites)
        if self.time_passed - self.last_update >= self.animation_cooldown:
            self.frame += 1
            self.last_update = self.time_passed
        if self.frame > 11: self.frame = 0
        return main.WIN.blit(self.idle_step, (self.x, self.y))
    # jump animations
    def jump(self, x, y, width, height, scale):
        self.width = width * scale
        self.height = height * scale
        self.time_passed += 1
        self.jump_step = pygame.Surface((width, height))
        self.jump_step.blit(self.sprites, (0, 0), (x, y, width, height))
        self.jump_step = pygame.transform.scale_by(self.jump_step, scale)
        self.jump_step.set_colorkey(self.background_sprites)
        if self.direction == 'L':
            self.jump_step = pygame.transform.flip(self.jump_step, True, False)
        self.last_update = self.time_passed
        return main.WIN.blit(self.jump_step, (self.x, self.y))
    # walikng animations
    def walk(self, x, y, width, height, distance, scale):
        self.width = width * scale
        self.height = height * scale
        self.time_passed += 1
        self.walk_step = pygame.Surface((width, height))
        self.walk_step.blit(self.sprites, (0, 0), (x + self.frame * distance, y, width, height))
        self.walk_step = pygame.transform.scale_by(self.walk_step, scale)
        self.walk_step.set_colorkey(self.background_sprites)
        if self.direction == 'L':
            self.walk_step = pygame.transform.flip(self.walk_step, True, False)
        if self.time_passed - self.last_update >= self.animation_cooldown:
            self.frame += 1
            self.last_update = self.time_passed
        if self.frame > 6: self.frame = 0
        return main.WIN.blit(self.walk_step, (self.x, self.y))
    # animations for attacks done on the ground
    def grd_atk(self, x, y, width, height, distance, scale):
        self.atking = True
        self.frame = 0
        self.width = width * scale
        self.height = height * scale
        self.time_passed += 1
        self.grd_atk_step = pygame.Surface((width, height))
        self.grd_atk_step.blit(self.sprites, (0, 0), (x + self.frame * distance, y, width, height))
        self.grd_atk_step = pygame.transform.scale_by(self.grd_atk_step, scale)
        self.grd_atk_step.set_colorkey(self.background_sprites)
        if self.direction == 'L':
            self.grd_atk_step = pygame.transform.flip(self.grd_atk_step, True, False)
        if self.time_passed - self.last_update >= self.animation_cooldown:
            self.frame += 1
            self.last_update = self.time_passed
        if self.frame > 12: self.atking = False
        return main.WIN.blit(self.grd_atk_step, (self.x, self.y))

                
                  
