import pygame
import random

# CONSTANTES
RED = (255, 0, 0)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
WHITE = (255, 255, 255)
SCREEN_WIDTH = 600
SCREEN_HEIGTH = 600


class Map:
    def __init__(self):
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGTH))


