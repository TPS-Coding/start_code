import pygame
from settings import *



class Sprite(pygame.sprite.Sprite):
    def __init__(self, groups, surf, pos, collision_sprites=None):
        super().__init__(groups)

        self.image = surf
        self.rect = self.image.get_frect(center = pos)


class Player(Sprite):
    def __init__(self, groups, surf, pos, collision_sprites=None):
        super().__init__(groups, surf, pos, collision_sprites=None)

        self.image = surf
        self.rect = self.image.get_frect(center = pos)

        ### movement
        self.direction = pygame.Vector2()
        self.speed = 400

        ## coliisions
        self.collision_sprites


    def input(self):

        keys = pygame.key.get_pressed()

        ### horizontal
        self.direction.x = int(keys[pygame.K_RIGHT] or keys[pygame.K_d]) - int(keys[pygame.K_LEFT] or keys[pygame.K_s])

        self.direction.y = int(keys[pygame.K_DOWN] or keys[pygame.K_s]) - int(keys[pygame.K_UP] or keys[pygame.K_w])
        
    def move(self, dt):
        ## horizontal
        self.rect.x += self.direction.x * self.speed * dt
        self.check_boundaries('horizontal')

        ### vertical
        self.rect.y += self.direction.y * self.speed * dt
        self.check_boundaries('vertical')


    def check_boundaries(self, direction):
        if direction == 'horizontal':
            if self.rect.left <= 0:
                self.rect.left = 0
            if self.rect.right >= WINDOW_WIDTH:
                self.rect.right = WINDOW_WIDTH
        
        if direction == 'vertical':
            if self.rect.top <= 0:
                self.rect.top = 0
            if self.rect.bottom >= WINDOW_HEIGHT:
                self.rect.bottom = WINDOW_HEIGHT


    def update(self, dt):
        self.input()
        self.move(dt)


class Enemy(Sprite):
    def __init__(self, groups, surf, pos, collision_sprites=None):
        def super().__init__(groups, surf, pos, collision_sprites=None)


        self.direction = pygame.Vector2(uniform(-0.5,0.5), 1)
        self.speed  = randint(500,800)
    

    def update(self,dt):
        self.move(dt)


class AnimatedSprite(Enemy):
    def __init__(self, groups, frames, pos, collision_sprites=None, animation_speed = ANIMATION_SPEED):
        self.frames = frames
        self.frame_index = 0
        super().__init__(groups, self.frames[self.frame_index], pos, collision_sprites=None)

        self.animation_speed = animation_speed


    def animate(self, dt):
        self.frame_index += self.animation_speed * dt
        self.image = pygame.transform.scale_by(self.frames[int(self.frame_index % len(self.frames))])

    def update(self,dt):
        self.animate(dt)

