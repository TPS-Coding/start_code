import pygame
import sys
from settings import *


class Game():
    def __init__(self):

        pygame.init()
        
        self.display_surface = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("MY PYTHON GAME")
        self.clock = pygame.time.Clock()
        self.running = True


        ### groups
        self.all_sprites = pygame.sprite.Group()
        



    def run(self):
        while self.running:
            self.clock.tick(60)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                    pygame.quit()
                    sys.exit()


            ### draw
            self.display_surface.fill("black")

            ### update
            pygame.display.update()


if __name__ == "__main__":
    game = Game()
    game.run()