import pygame
import sys
from enemies import OctopusAlien, AlienShip, AlienShip2, ClassicAlien, ClassicAlien2
from shots import SingleShot, Missile, DoubleShot, LongShot, TripleShot
from player import Player
from efects import Explosion
from map import Map
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
PLANE_MOVEMENT = 10     # Numero de pixeles que se mueve el avion (el jugador)

# Definiendo posicion y jugador

PLAYER_ONE_POSITION = [SCREEN_WIDTH // 2, SCREEN_HEIGTH - 60]
player = Player(PLAYER_ONE_POSITION)

# Definiendo lista de disparos : Cada disparo se guardará en esta lista hasta que alcance su max distancia
shots = []
# Definiendo lista de enemigos: Cada enemigo se guarda en la lista hasta que sea eliminado
enemies = []
# Definiendo lista de explosiones
explosions = []

heart_picture = pygame.image.load("pictures/corazon.png")
heart_picture.set_colorkey(WHITE)

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGTH))
screen.fill(BACKGROUNG_COLOR)


def run_game():
    pygame.init()
    pygame.key.set_repeat(1, 25)

    clock = pygame.time.Clock()

    fondo = Map()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGTH))

    score = 0
    game_over = False

    while not game_over:
        # Control de fps:
        clock.tick(15)
        screen.blit(fondo.get_picture(), [0, 0])
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT and player.get_position()[0] >= PLANE_MOVEMENT:
                    player.move_left(PLANE_MOVEMENT)
                elif event.key == pygame.K_RIGHT and player.get_position()[0] < SCREEN_WIDTH - PLANE_MOVEMENT:
                    player.move_right(PLANE_MOVEMENT)
                elif event.key == pygame.K_UP and player.get_position()[1] >= PLANE_MOVEMENT:
                    player.move_up(PLANE_MOVEMENT)
                elif event.key == pygame.K_DOWN and player.get_position()[1] < SCREEN_HEIGTH - PLANE_MOVEMENT:
                    player.move_down(PLANE_MOVEMENT)
                elif event.key == pygame.K_SPACE:
                    score -= 1
                    create_shot(player.get_position(), score)

        # Creamos los enemigos aleatoriamente:
        if random.randint(0, 1000) >= 980:
            create_enemy(score)

        for shot in shots:
            if shot.get_max_distance() > shot.get_distance_traveled():
                move_shot(shot)
            else:
                shots.remove(shot)
            # Comprobamos si hay contacto con algun enemigo:
            for enemy in enemies:
                if contact(shot, enemy):
                    score += 10
                    enemy.set_damage(shot.get_damage())
                    shots.remove(shot)

        # Dibujamos los enemigos y hacemos que avancen:
        for enemy in enemies:
            # Comprobamos que tenga vida y que siga dentro de la pantalla
            if enemy.get_health() > 0 and enemy.get_position()[1] <= SCREEN_HEIGTH:
                move_enemy(enemy)
            # Si ha llegado al final de la pantalla quitamos vida al jugador:
            elif enemy.get_position()[1] > SCREEN_HEIGTH:
                player.set_damage(20)
                enemies.remove(enemy)
            else:
                create_explosion(enemy.get_position())
                enemies.remove(enemy)

        # Explosiones:
        for explosion in explosions:
            if explosion.get_iterations() >= 2:
                explosions.remove(explosion)
            else:
                explosion.increase_iterations()

        # Comprobamos si ha acabado el juego:
        if player.get_health() <= 0:
            game_over = True


        # Dibujamos las vidas del jugador y la puntuacion:
        coordenada = 0
        fuente_score = pygame.font.Font(None, 30)
        text_score = str(score)
        text_score = fuente_score.render(text_score, 0, WHITE)
        screen.blit(text_score, (SCREEN_WIDTH - 45, coordenada))

        hearts = player.get_health() // 20
        for i in range(0, hearts):
            coordenada += 20
            screen.blit(heart_picture, (SCREEN_WIDTH - 20, coordenada))

        for i in range(hearts, 5):
            coordenada += 20

        # Dibujamos la posicion del jugador y los corazones:
        screen.blit(player.get_picture(), (player.get_position()[0], player.get_position()[1]))
        pygame.display.update()

    end_menu(score)


def end_menu(score):
    while True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    start_over()

        fuente_game_over = pygame.font.Font(None, 100)
        text_game_over = "GAME OVER"
        text_game_over = fuente_game_over.render(text_game_over, 0, RED)

        fuente_score = pygame.font.Font(None, 50)
        text_score = "        Score: " + str(score)
        text_score = fuente_score.render(text_score, 0, WHITE)

        fuente_try_again = pygame.font.Font(None, 30)
        text_try_again = "Press Space to try again"
        text_try_again = fuente_try_again.render(text_try_again, 0, WHITE)

        screen.blit(text_game_over, (100, 200))
        screen.blit(text_score, (180, 300))
        screen.blit(text_try_again, (200, 400))
        pygame.display.update()


def start_over():
    shots.clear()
    enemies.clear()
    explosions.clear()
    player.revive()
    player.move([SCREEN_WIDTH // 2, SCREEN_HEIGTH - 60])
    run_game()


def create_enemy(score):
    ENEMY_RESPAWN = [(random.randint(0, SCREEN_WIDTH - PLANE_SIZE) // PLANE_MOVEMENT) * PLANE_MOVEMENT, 0]
    if score < 100:
        enemy = OctopusAlien(ENEMY_RESPAWN.copy())
    elif score < 200:
        enemy = ClassicAlien(ENEMY_RESPAWN.copy())
    elif score < 300:
        enemy = ClassicAlien2(ENEMY_RESPAWN.copy())
    elif score < 400:
        enemy = AlienShip(ENEMY_RESPAWN.copy())
    else:
        enemy = AlienShip2(ENEMY_RESPAWN.copy())
    enemies.append(enemy)


def create_shot(shot_position, score):
    # Modifico ligeramente la posicion para que dispare desde el pixel central al jugador
    shot_position_copied = shot_position.copy()
    if score < 20:
        shot = SingleShot(shot_position_copied)
    elif score < 40:
        shot = LongShot(shot_position_copied)
    elif score < 60:
        shot = DoubleShot(shot_position_copied)
    elif score < 80:
        shot = TripleShot(shot_position_copied)
    else:
        shot = Missile(shot_position_copied)
    shots.append(shot)


def create_explosion(position):
    explosion = Explosion(position)
    explosions.append(explosion)
    screen.blit(explosion.get_picture(), (explosion.get_position()[0], explosion.get_position()[1]))


def move_enemy(enemy):
    enemy.move_fordward(5)
    screen.blit(enemy.get_picture(), (enemy.get_position()[0], enemy.get_position()[1]))


def move_shot(shot):
    shot.move_forward(20)
    screen.blit(shot.get_picture(), (shot.get_position()[0], shot.get_position()[1]))


def contact(shot, enemy):
    if shot.get_position()[0] - enemy.get_position()[0] in range(0, PLANE_SIZE + 1) \
            and enemy.get_position()[1] - shot.get_position()[1] in range(0, PLANE_SIZE + 1):
        return True
    else:
        return False


run_game()