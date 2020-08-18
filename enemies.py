import pygame

# CONSTANTES
RED = (255, 0, 0)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
WHITE = (255, 255, 255)


class Enemy1:
    def __init__(self, enemy_position):
        self.picture = pygame.image.load("marciano.png")
        self.picture.set_colorkey(WHITE)
        self.position = enemy_position
        self.health = 100

    def get_picture(self):
        return self.picture

    def move_fordward(self, distance):
        self.position[1] += distance

    def get_position(self):
        return self.position

    def get_health(self):
        return self.health

    def set_damage(self, damage_points):
        self.health -= damage_points

