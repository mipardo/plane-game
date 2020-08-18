import pygame

# CONSTANTES
RED = (255, 0, 0)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
WHITE = (255, 255, 255)





class Shot:
    def __init__(self, starting_position):
        self.picture = pygame.image.load("singleShot.png")
        self.picture.set_colorkey(WHITE)
        self.position = starting_position
        self.starting_position = starting_position
        self.distance_traveled = 0
        self.damage = 100

    def get_picture(self):
        return self.picture

    def get_distance_traveled(self):
        return self.distance_traveled

    def get_position(self):
        return self.position

    def get_starting_position(self):
        return self.starting_position

    def get_damage(self):
        return self.damage

    def move_forward(self, distance):
        self.position[1] -= distance
        self.distance_traveled += 1


class Double_shot:
    def __init__(self, starting_position):
        self.picture = pygame.image.load("singleShot.png")
        self.picture.set_colorkey(WHITE)
        self.position = starting_position
        self.starting_position = starting_position
        self.distance_traveled = 0
        self.damage = 100

    def get_picture(self):
        return self.picture

    def get_distance_traveled(self):
        return self.distance_traveled

    def get_position(self):
        return self.position

    def get_starting_position(self):
        return self.starting_position

    def get_damage(self):
        return self.damage

    def move_forward(self, distance):
        self.position[1] -= distance
        self.distance_traveled += 1