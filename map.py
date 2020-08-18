import pygame
import random

# CONSTANTES
RED = (255, 0, 0)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
WHITE = (255, 255, 255)
SCREEN_WIDTH = 600
SCREEN_HEIGTH = 600
BACKGROUNG_COLOR = BLACK


class Map:
    def __init__(self):
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGTH))
        self.screen.fill(BACKGROUNG_COLOR)
        for x in range(0, SCREEN_WIDTH):
            for y in range(0, SCREEN_HEIGTH):
                if random.randint(0,100) > 90:
                    pygame.draw.rect(self.screen, WHITE, (x, y, 1, 1))








