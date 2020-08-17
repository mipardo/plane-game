class Enemy1:
    def __init__(self, enemy_position):
        self.position = enemy_position
        self.health = 100

    def move_fordward(self, distance):
        self.position[1] += distance

    def get_position(self):
        return self.position

    def get_health(self):
        return self.health

    def set_damage(self, damage_points):
        self.health -= damage_points
