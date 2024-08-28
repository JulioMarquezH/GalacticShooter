import pygame
import random
from personajes.buenos.personajes_principales import Protagonista
from personajes.malos.enemigos import Enemigos_basicos
from utils import utils

pygame.init()

modo_juego = input('Seleccione el modo de juego: 1 jugador (1) / 2 jugadores (2): ')
modo_juego_2 = modo_juego == '2'
# constantes
FPS = 60
ALTO = 800
ANCHO = 900
dimensiones = {
    'ALTO': ALTO,
    'ANCHO': ANCHO
}
CLOCK = pygame.time.Clock()
VENTANA = pygame.display.set_mode([ANCHO, ALTO])
FUENTE = pygame.font.SysFont('Comic Sans MS', 16)

# jugador 1
jugador_1 = Protagonista(100, ALTO - 100)
jugador_1.teclas = [pygame.K_w, pygame.K_s, pygame.K_a, pygame.K_d, pygame.K_SPACE]
# jugador_1.color = '#ffffff'
jugador_1.vida = 3
# jugador_1. = 3

# jugador 2	
if modo_juego_2:
    jugador_2 = Protagonista(ANCHO - 100,  ALTO -100)
    jugador_2.teclas = [pygame.K_UP, pygame.K_DOWN, pygame.K_LEFT, pygame.K_RIGHT, pygame.K_MINUS]
    # jugador_2.color = 'purple'
    jugador_2.vida = 3 

# variables
jugando = True
enemigos = []
balas = []
tiempo = 0
tiempo_pasado = 0
tiempo_entre_enemigos = 500

# Bucle principal del juego
while jugando:
    # 1. Gestión del tiempo y eventos
    tiempo += CLOCK.tick(FPS)
    tiempo_pasado += CLOCK.tick(FPS)

    eventos = pygame.event.get()
    teclas = pygame.key.get_pressed()

    for evento in eventos:
        if evento.type == pygame.QUIT:
            jugando = False

    # 2. Lógica del juego
    # Generación de enemigos
    if tiempo_pasado > tiempo_entre_enemigos:
        enemigo_temporal = Enemigos_basicos(0, -10)
        enemigo_temporal.x = random.randint(0, ANCHO - enemigo_temporal.ancho)
        enemigos.append(enemigo_temporal)
        tiempo_pasado = 0        

    # Procesa entradas solo para jugadores vivos
    if jugador_1.vida > 0:
        utils.gestionar_teclas(teclas, jugador_1, dimensiones, balas)
    if modo_juego_2:
        if jugador_2.vida > 0:
            utils.gestionar_teclas(teclas, jugador_2, dimensiones, balas)
    
    # Actualización de balas
    for bala in balas:
        bala.movimiento()
        if bala.y < 0:
            balas.remove(bala)
    
    # Actualización de enemigos
    for enemigo in enemigos:
        enemigo.movimiento()
        
        # Colisiones con jugadores
        if jugador_1.vida > 0 and pygame.Rect.colliderect(enemigo.rect, jugador_1.rect):
            jugador_1.vida -= enemigo.daño
            enemigos.remove(enemigo)
            continue
        elif modo_juego_2:
            if jugador_2.vida > 0 and pygame.Rect.colliderect(enemigo.rect, jugador_2.rect):
                jugador_2.vida -= enemigo.daño
                enemigos.remove(enemigo)
                continue

        # Enemigos fuera de pantalla
        if enemigo.y + enemigo.alto > ALTO + enemigo.alto:
            enemigos.remove(enemigo)
            continue
        
        # Colisiones con balas
        for bala in balas:
            if pygame.Rect.colliderect(enemigo.rect, bala.rect):
                balas.remove(bala)
                enemigo.vida -= bala.daño
                
        # Enemigos derrotados
        if enemigo.vida <= 0:
            enemigos.remove(enemigo)
            continue

    # 3. Dibujar en pantalla
    VENTANA.fill('black')

    # Dibujar jugadores
    if jugador_1.vida > 0:
        jugador_1.pintar(VENTANA)
    if modo_juego_2:
        if jugador_2.vida > 0:
            jugador_2.pintar(VENTANA)

    # Dibujar balas
    for bala in balas:
        bala.pintar(VENTANA)

    # Dibujar enemigos
    for enemigo in enemigos:
        enemigo.pintar(VENTANA)

    # Actualizar textos en pantalla
    text_tiempo = FUENTE.render(f'Tiempo: {tiempo//1000}', True, 'white')
    text_jugador_1_vida = FUENTE.render(f'Vida: {jugador_1.vida}', True, 'white')
    if modo_juego_2:
        text_jugador_2_vida = FUENTE.render(f'Vida: {jugador_2.vida }', True, 'white')

    VENTANA.blit(text_tiempo, (ANCHO/2 - text_tiempo.get_width()/2, 10))
    VENTANA.blit(text_jugador_1_vida, (10, 10))
    if modo_juego_2:
        VENTANA.blit(text_jugador_2_vida, (ANCHO - 20 - text_jugador_1_vida.get_width(), 10))

    # 4. Verificación del estado del juego
    if modo_juego_2:
        estado_juego = utils.verificar_estado_jugadores(jugador_1, jugador_2)
    else:
        estado_juego = utils.verificar_estado_jugadores(jugador_1, False)
    if estado_juego == "game_over":
        text_game_over = FUENTE.render('Game Over', True, 'red')
        VENTANA.blit(text_game_over, (ANCHO/2 - text_game_over.get_width()/2, ALTO/2 - text_game_over.get_height()/2))
        pygame.display.update()
        pygame.time.wait(3000)  # Espera 3 segundos antes de cerrar el juego
        jugando = False

    # Actualizar la pantalla
    pygame.display.update()
