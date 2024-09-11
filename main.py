import pygame
import random
from characters.kind.main_characters import Protagonist
from characters.evil.enemies import Enemies_basic
from utils import utils

pygame.init()

game_mode = input('Seleccione el modo de juego: 1 jugador (1) / 2 jugadores (2): ')
game_mode_2 = game_mode == '2'
# constantes
FPS = 60
HIGH = 800
WIDTH = 900
dimensions = {
    'HIGH': HIGH,
    'WIDTH': WIDTH
}
CLOCK = pygame.time.Clock()
WINDOW = pygame.display.set_mode([WIDTH, HIGH])
FONT = pygame.font.SysFont('Comic Sans MS', 16)

# jugador 1
player_1 = Protagonist(100, HIGH - 100)
player_1.key = [pygame.K_w, pygame.K_s, pygame.K_a, pygame.K_d, pygame.K_SPACE]
# jugador_1.color = '#ffffff'
player_1.lives = 3
# jugador_1. = 3

# jugador 2	
if game_mode_2:
    player_2 = Protagonist(WIDTH - 100,  HIGH -100)
    player_2.key = [pygame.K_UP, pygame.K_DOWN, pygame.K_LEFT, pygame.K_RIGHT, pygame.K_MINUS]
    # jugador_2.color = 'purple'
    player_2.lives = 3 

# variables
playing = True
enemies = []
bullets = []
items = []
time = 0
last_time = 0
time_between_enemies = 250

# Bucle principal del juego
while playing:
    # 1. Gestión del tiempo y eventos
    time += CLOCK.tick(FPS)
    last_time += CLOCK.tick(FPS)

    events = pygame.event.get()
    keys = pygame.key.get_pressed()

    for event in events:
        if event.type == pygame.QUIT:
            playing = False

    # 2. Lógica del juego
    # Generación de enemigos
    if last_time > time_between_enemies:
        temporary_enemy = Enemies_basic(0, -10)
        temporary_enemy.x = random.randint(0, WIDTH - temporary_enemy.width)
        enemies.append(temporary_enemy)
        last_time = 0        

    # Procesa entradas solo para jugadores vivos
    if player_1.lives > 0:
        utils.manage_keys(keys, player_1, dimensions, bullets)
    if game_mode_2:
        if player_2.lives > 0:
            utils.manage_keys(keys, player_2, dimensions, bullets)
    
    # Actualización de balas
    for bullet in bullets:
        bullet.move()
        if bullet.y < 0:
            bullets.remove(bullet)
            
    for item in items:
        item.move()
        
        # Colisiones con jugadores
        if player_1.lives > 0 and pygame.Rect.colliderect(item.rect, player_1.rect):
            attribute_name = item.attributes['attribute']
            attribute_value = item.attributes['amount']
            if item.attributes['is_divided']:
                setattr(player_1, attribute_name, getattr(player_1, attribute_name, 0) / attribute_value)
            else:
                setattr(player_1, attribute_name, getattr(player_1, attribute_name, 0) + attribute_value)
            items.remove(item)
            continue
        elif game_mode_2:
            if player_2.lives > 0 and pygame.Rect.colliderect(item.rect, player_2.rect):
                attribute_name = item.attributes['attribute']
                attribute_value = item.attributes['amount']
                if item.attributes['is_divided']:
                    setattr(player_2, attribute_name, getattr(player_2, attribute_name, 0) / attribute_value)
                else:
                    setattr(player_2, attribute_name, getattr(player_2, attribute_name, 0) + attribute_value)
                items.remove(item)
                continue
        
        if item.y < 0:
            items.remove(item)
    
    # Actualización de enemigos
    for enemy in enemies:
        enemy.move()
        
        # Colisiones con jugadores
        if player_1.lives > 0 and pygame.Rect.colliderect(enemy.rect, player_1.rect):
            player_1.lives -= enemy.damage
            enemies.remove(enemy)
            continue
        elif game_mode_2:
            if player_2.lives > 0 and pygame.Rect.colliderect(enemy.rect, player_2.rect):
                player_2.lives -= enemy.damage
                enemies.remove(enemy)
                continue

        # Enemigos fuera de pantalla
        if enemy.y + enemy.high > HIGH + enemy.high:
            enemies.remove(enemy)
            continue
        
        # Colisiones con balas
        for bullet in bullets:
            if pygame.Rect.colliderect(enemy.rect, bullet.rect):
                bullets.remove(bullet)
                enemy.lives -= bullet.damage
                
        # Enemigos derrotados
        if enemy.lives <= 0:
            enemies.remove(enemy)
            utils.create_item(enemy, items)
            continue

    # 3. Dibujar en pantalla
    WINDOW.fill('black')

    # Dibujar jugadores
    if player_1.lives > 0:
        player_1.paint(WINDOW)
    if game_mode_2:
        if player_2.lives > 0:
            player_2.paint(WINDOW)

    # Dibujar balas
    for bullet in bullets:
        bullet.paint(WINDOW)
        
    for item in items:
        item.paint(WINDOW)
        
    # Dibujar enemigos
    for enemy in enemies:
        enemy.paint(WINDOW)

    # Actualizar textos en pantalla
    text_time = FONT.render(f'Tiempo: {time//1000}', True, 'white')
    text_player_1_lives = FONT.render(f'Vida: {player_1.lives}', True, 'white')
    if game_mode_2:
        text_player_2_lives = FONT.render(f'Vida: {player_2.lives }', True, 'white')

    WINDOW.blit(text_time, (WIDTH/2 - text_time.get_width()/2, 10))
    WINDOW.blit(text_player_1_lives, (10, 10))
    if game_mode_2:
        WINDOW.blit(text_player_2_lives, (WIDTH - 20 - text_player_2_lives.get_width(), 10))

    # 4. Verificación del estado del juego
    if game_mode_2:
        game_state = utils.check_player_status(player_1, player_2)
    else:
        game_state = utils.check_player_status(player_1, False)
    if game_state == "game_over":
        text_game_over = FONT.render('Game Over', True, 'red')
        WINDOW.blit(text_game_over, (WIDTH/2 - text_game_over.get_width()/2, HIGH/2 - text_game_over.get_height()/2))
        pygame.display.update()
        pygame.time.wait(3000)  # Espera 3 segundos antes de cerrar el juego
        playing = False

    # Actualizar la pantalla
    pygame.display.update()
