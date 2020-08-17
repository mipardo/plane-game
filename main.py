import pygame
import sys
from enemies import Enemy1
from shots import Shot
from player import Player, Explosion
import random

# CONSTANTES
RED = (255, 0, 0)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
WHITE = (255, 255, 255)
BACKGROUNG_COLOR = BLACK
SCREEN_WIDTH = 600
SCREEN_HEIGTH = 600
PLANE_SIZE = 40         # Ancho y alto del avion (JUGADOR Y  TODOS LOS TIPOS DE ENEMIGOS)
PLANE_MOVEMENT = 20     # Numero de pixeles que se mueve el avion (el jugador)

# Definiendo posiciones y jugadores

PLAYER_ONE_POSITION = [SCREEN_WIDTH // 2, SCREEN_HEIGTH - 60]

player_one = Player(PLAYER_ONE_POSITION)

# Definiendo lista de disparos : Cada disparo se guardará en esta lista hasta que alcance su max distancia
shots = []
# Definiendo lista de enemigos: Cada enemigo se guarda en la lista hasta que sea eliminado
enemies = []
# Definiendo lista de explosiones
explosions = []

score = 0

# Defino los metodos de los movimientos, lo que hacen son eliminar el rasto (pixeles) de la posicion anterior y actualizar la posicion
def move_left(player):
    pygame.draw.rect(screen, BACKGROUNG_COLOR, (player.get_position()[0], player.get_position()[1], PLANE_SIZE, PLANE_SIZE))
    player.move_left(PLANE_MOVEMENT)


def move_right(player):
    pygame.draw.rect(screen, BACKGROUNG_COLOR, (player.get_position()[0], player.get_position()[1], PLANE_SIZE, PLANE_SIZE))
    player.move_right(PLANE_MOVEMENT)


def move_up(player):
    pygame.draw.rect(screen, BACKGROUNG_COLOR, (player.get_position()[0], player.get_position()[1], PLANE_SIZE, PLANE_SIZE))
    player.move_up(PLANE_MOVEMENT)


def move_down(player):
    pygame.draw.rect(screen, BACKGROUNG_COLOR, (player.get_position()[0], player.get_position()[1], PLANE_SIZE, PLANE_SIZE))
    player.move_down(PLANE_MOVEMENT)


def create_enemy():
    ENEMY_RESPAWN = [(random.randint(0, SCREEN_WIDTH - PLANE_SIZE) // PLANE_MOVEMENT) * PLANE_MOVEMENT, 0]
    enemy = Enemy1(ENEMY_RESPAWN.copy())
    enemies.append(enemy)


def create_shot(shot_position):
    # Modifico ligeramente la posicion para que dispare desde el pixel central al jugador
    shot_position_copied = shot_position.copy()
    shot_position_copied[0] += (PLANE_SIZE // 2) - 1
    shot = Shot(shot_position_copied)
    shots.append(shot)


def create_explosion(position):
    explosion = Explosion(position)
    explosions.append(explosion)
    screen.blit(boom_picture, (explosion.get_position()[0], explosion.get_position()[1]))


def move_enemy(enemy):
    pygame.draw.rect(screen, BACKGROUNG_COLOR, (enemy.get_position()[0], enemy.get_position()[1], PLANE_SIZE, PLANE_SIZE))
    enemy.move_fordward(1)
    screen.blit(enemy_picture, (enemy.get_position()[0], enemy.get_position()[1]))


def move_shot(shot):
    pygame.draw.rect(screen, BACKGROUNG_COLOR, (shot.get_position()[0], shot.get_position()[1], 2, 15))
    shot.move_forward(20)
    pygame.draw.rect(screen, RED, (shot.get_position()[0], shot.get_position()[1], 2, 15))


def contact(shot, enemy):
    if shot.get_position()[0] == enemy.get_position()[0] + (PLANE_SIZE // 2) - 1 \
            and enemy.get_position()[1] - shot.get_position()[1] > 5:
        return True
    else:
        return False


def end_menu():
    print(score)

pygame.init()
clock = pygame.time.Clock()

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGTH))
screen.fill(BACKGROUNG_COLOR)

plane_picture = pygame.image.load("nave1.png")
enemy_picture = pygame.image.load("marciano.png")
boom_picture = pygame.image.load("boom.png")

fuente = pygame.font.Font(None, 30)
texto = fuente.render("Score: ", 0, WHITE)

plane_picture.set_colorkey(WHITE)
enemy_picture.set_colorkey(WHITE)
boom_picture.set_colorkey(WHITE)

game_over = False

while not game_over:
    # Control de fps:
    dt = clock.tick(10)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT and player_one.get_position()[0] >= PLANE_MOVEMENT:
                move_left(player_one)
            elif event.key == pygame.K_RIGHT and player_one.get_position()[0] < SCREEN_WIDTH - PLANE_MOVEMENT:
                move_right(player_one)
            elif event.key == pygame.K_UP and player_one.get_position()[1] >= PLANE_MOVEMENT:
                move_up(player_one)
            elif event.key == pygame.K_DOWN and player_one.get_position()[1] < SCREEN_HEIGTH - PLANE_MOVEMENT:
                move_down(player_one)
            elif event.key == pygame.K_SPACE:
                score -= 1
                create_shot(player_one.get_position())

    # Creamos los enemigos aleatoriamente:
    if random.randint(0, 1000) >= 990:
        create_enemy()

    for shot in shots:
        if shot.get_distance_traveled() < 20:
            move_shot(shot)
        else:
            pygame.draw.rect(screen, BACKGROUNG_COLOR, (shot.get_position()[0], shot.get_position()[1], 2, 15))
            shots.remove(shot)
        # Comprobamos si hay contacto con algun enemigo:
        for enemy in enemies:
            if contact(shot, enemy):
                score += 10
                enemy.set_damage(shot.get_damage())
                pygame.draw.rect(screen, BACKGROUNG_COLOR, (shot.get_position()[0], shot.get_position()[1], 2, 15))
                create_explosion(enemy.get_position())
                shots.remove(shot)

    # Dibujamos los enemigos y hacemos que avancen:
    for enemy in enemies:
        # Comprobamos que tenga vida y que siga dentro de la pantalla
        if enemy.get_health() > 0 and enemy.get_position()[1] <= SCREEN_HEIGTH:
            move_enemy(enemy)
        # Si ha llegado al final de la pantalla quitamos vida al jugador:
        elif enemy.get_position()[1] > SCREEN_HEIGTH:
            player_one.set_damage(20)
            enemies.remove(enemy)
        else:
            enemies.remove(enemy)

    # Explosiones:
    for explosion in explosions:
        if explosion.get_iterations() >= 2:
            pygame.draw.rect(screen, BACKGROUNG_COLOR, (explosion.get_position()[0], explosion.get_position()[1], PLANE_SIZE, PLANE_SIZE))
            explosions.remove(explosion)
        else:
            explosion.increase_iterations()

    # Comprobamos si ha acabado el juego:
    if player_one.get_health() <= 0:
        game_over = True

    # Dibujamos la posicion del jugador
    screen.blit(plane_picture, (player_one.get_position()[0], player_one.get_position()[1]))
    screen.blit(texto, (100, 100))
    pygame.display.update()

end_menu()


