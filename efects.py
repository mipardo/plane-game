import pygame

# CONSTANTES
RED = (255, 0, 0)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
WHITE = (255, 255, 255)


class Explosion:
    def __init__(self, position):
        self.position = position
        self.picture = pygame.image.load("pictures/boom.png")
        self.picture.set_colorkey(WHITE)
        self.iterations = 0
        self.sound = pygame.mixer.Sound("sounds/explosion.ogg")


    def get_picture(self):
        return self.picture

    def get_position(self):
        return self.position

    def play_sound(self):
        self.sound.play()

    def get_iterations(self):
        return self.iterations

    def increase_iterations(self):
        self.iterations += 1


class LevelUp:

    def __init__(self, position):
        self.position = position
        self.picture = pygame.image.load("pictures/.png")
        self.picture.set_colorkey(WHITE)