import pygame

# CONSTANTES
RED = (255, 0, 0)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
WHITE = (255, 255, 255)


class Enemy(object):
    def __init__(self, enemy_position, picture):
        self.position = enemy_position
        self.picture = pygame.image.load(picture)
        self.picture.set_colorkey(WHITE)
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


class OctopusAlien(Enemy):
    def __init__(self, enemy_position):
        Enemy.__init__(self, enemy_position, "pictures/marciano.png")


class ClassicAlien(Enemy):
    def __init__(self,enemy_position):
        Enemy.__init__(self, enemy_position, "pictures/alienClasico.png")


class ClassicAlien2(Enemy):
    def __init__(self, enemy_position):
        Enemy.__init__(self, enemy_position, "pictures/alienClasico2.png")


class AlienShip(Enemy):
    def __init__(self, enemy_position):
        Enemy.__init__(self, enemy_position, "pictures/naveMarciana.png")


class AlienShip2(Enemy):
    def __init__(self, enemy_position):
        Enemy.__init__(self, enemy_position, "pictures/naveMarciana2.png")

