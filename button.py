import pygame

class Button(pygame.sprite.Sprite):
    def __init__(self, surf, pos, groups, value, enabled=True):
        super().__init__(groups)

        self.image = surf
        self.rect = self.image.get_frect(center=pos)
        self.enabled = enabled
        if value == '':
            self.enabled = False

        ### for the letter
        self.value = value
        self.font = pygame.font.Font("graphics/font/BD_Cartoon_Shout.ttf", 30)
        
        self.text_surf = self.font.render(self.value, True, 'black')
        self.text_rect = self.text_surf.get_frect(center=pos)

        self.display_surface = pygame.display.get_surface()

        self.collision_rect = self.rect.scale_by(0.5)


    def draw(self):
        if self.enabled:
            self.display_surface.blit(self.image, self.rect)
            self.display_surface.blit(self.text_surf, self.text_rect)
    
    def check_click(self):
        mouse_pos = pygame.mouse.get_pos()
        left_click = pygame.mouse.get_pressed()[0]
        if left_click and self.collision_rect.collidepoint(mouse_pos) and self.enabled:
            return True
        else:
            return False

    def update(self):
        self.draw()
