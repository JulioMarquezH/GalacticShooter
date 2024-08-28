import pygame
from ataques.ataques_buenos.balas import Balas

pygame.init()
pygame.mixer.init()

#constante
SONIDO_BALAS = pygame.mixer.Sound('media/sonidos/sonidoBalas.mp3')

# funciones 
def validar_bordes(limite, rect, eje):
    if limite == 0:
        if limite >= rect[eje]:
            return False
        return True
    else:
        if limite >= rect[eje] + rect[eje + 2]:
            return False
        return True


def crear_bala(personaje, balas):
    
    if pygame.time.get_ticks() - personaje.ultima_bala > personaje.intervalo_entre_balas:
        balas.append(Balas(personaje.rect.centerx, personaje.rect.centery))
        personaje.ultima_bala = pygame.time.get_ticks()
        SONIDO_BALAS.play()
    

#imprimir que sale en la flech
def gestionar_teclas(teclas, personaje, dimensiones, balas):
    if teclas[personaje.teclas[0]]:
        if validar_bordes(0, personaje.rect, 1):
            personaje.y -= personaje.velocidad
    if teclas[personaje.teclas[1]]:
        if not validar_bordes(dimensiones['ALTO'], personaje.rect, 1):
             personaje.y += personaje.velocidad  
    if teclas[personaje.teclas[2]]:
        if validar_bordes(0, personaje.rect, 0):
            personaje.x -= personaje.velocidad
    if teclas[personaje.teclas[3]]:
        if not validar_bordes(dimensiones['ANCHO'], personaje.rect, 0):
            personaje.x += personaje.velocidad
    if teclas[personaje.teclas[4]]:
        crear_bala(personaje, balas)
        
# Función para verificar el estado de los jugadores
def verificar_estado_jugadores(jugador_1, jugador_2):
    if jugador_1.vida <= 0:
        if not jugador_2 or jugador_2.vida <= 0:
            return "game_over"
        else:
            return "jugador_1_muerto"
    elif jugador_2 and jugador_2.vida <= 0:
        return "jugador_2_muerto"
    else:
        return "jugando"
