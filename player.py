import pygame

# CONSTANTES
RED = (255, 0, 0)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
WHITE = (255, 255, 255)
PLANE_SIZE = 40         # Ancho y alto del avion (JUGADOR Y  TODOS LOS TIPOS DE ENEMIGOS)


class Player:

    # Player position corresponde a las coordenadas del jugador: player_position[WIDTH, HEIGTH] [X,Y]
    def __init__(self, player_position):
        self.picture = pygame.image.load("pictures/nave1.png")
        self.picture.set_colorkey(WHITE)
        self.health = 100
        self.position = player_position
        self.level = 0

        # self.center = [player_position[0] + PLANE_SIZE // 2, player_position[1] + PLANE_SIZE // 2]
        # self.radius = PLANE_SIZE // 2

    def get_position(self):
        return self.position

    def get_picture(self):
        return self.picture

    def get_health(self):
        return self.health

    def set_damage(self, damage_points):
        self.health -= damage_points

    def set_healing(self, healing_points):
        self.health += healing_points

    def increase_level(self):
        self.level += 1

    def decrease_level(self):
        self.level -= 1

    def get_level(self):
        return self.level

    # Player movements
    def move(self, new_player_position):
        self.position = new_player_position

    def move_left(self, distance):
        self.position[0] -= distance

    def move_right(self, distance):
        self.position[0] += distance

    def move_up(self, distance):
        self.position[1] -= distance

    def move_down(self, distance):
        self.position[1] += distance

    def revive(self):
        self.health = 100







