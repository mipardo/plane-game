import pygame

# CONSTANTES
RED = (255, 0, 0)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
WHITE = (255, 255, 255)


class Shot(object):
    def __init__(self, starting_position, picture, damage, max_distance, sound):
        self.position = starting_position
        self.starting_position = starting_position
        self.picture = pygame.image.load(picture)
        self.picture.set_colorkey(WHITE)
        self.distance_traveled = 0
        self.max_distance = max_distance
        self.damage = damage
        self.sound = pygame.mixer.Sound(sound)

    def get_picture(self):
        return self.picture

    def play_sound(self):
        self.sound.play()

    def get_distance_traveled(self):
        return self.distance_traveled

    def get_position(self):
        return self.position

    def get_starting_position(self):
        return self.starting_position

    def get_damage(self):
        return self.damage

    def get_max_distance(self):
        return self.max_distance

    def move_forward(self, distance):
        self.position[1] -= distance
        self.distance_traveled += 1


class SingleShot(Shot):
    def __init__(self, starting_position):
        Shot.__init__(self, starting_position, "pictures/singleShot.png", 50, 10, "sounds/shot.ogg")


class LongShot(Shot):
    def __init__(self, starting_position):
        Shot.__init__(self, starting_position, "pictures/singleShot.png", 50, 30, "sounds/shot.ogg")


class DoubleShot(Shot):
    def __init__(self, starting_position):
        Shot.__init__(self, starting_position, "pictures/doubleShot.png", 100, 20, "sounds/shot.ogg")


class TripleShot(Shot):
    def __init__(self, starting_position):
        Shot.__init__(self,starting_position, "pictures/tripleShot.png", 150, 20, "sounds/tripleShot.ogg")


class Missile(Shot):
    def __init__(self, starting_position):
        Shot.__init__(self, starting_position, "pictures/misil.png", 300, 40, "sounds/shot.ogg")

