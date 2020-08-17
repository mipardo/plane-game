class Player:
    # Player position corresponde a las coordenadas del jugador: player_position[WIDTH, HEIGTH] [X,Y]
    def __init__(self, player_position):
        self.health = 100
        self.position = player_position

    def get_position(self):
        return self.position

    def get_health(self):
        return self.health

    def set_damage(self, damage_points):
        self.health -= damage_points

    def set_healing(self, healing_points):
        self.health += healing_points

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


class Explosion:
    def __init__(self, position):
        self.position = position
        self.iterations = 0

    def get_position(self):
        return self.position

    def get_iterations(self):
        return self.iterations

    def increase_iterations(self):
        self.iterations += 1





