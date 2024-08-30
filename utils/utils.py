import pygame
from attacks.kind_attacks.bullets import Bullets

pygame.init()
pygame.mixer.init()

#constante
SOUND_BULLETS = pygame.mixer.Sound('media/audio/soundBullets.mp3')

# funciones
def validate_edges(limit, rect, axis):
    if limit == 0:
        if limit >= rect[axis]:
            return False
        return True
    else:
        if limit >= rect[axis] + rect[axis + 2]:
            return False
        return True


def create_bullet(character, bullets):
    
    if pygame.time.get_ticks() - character.last_bullet > character.interval:
        bullets.append(Bullets(character.rect.centerx, character.rect.centery))
        character.last_bullet = pygame.time.get_ticks()
        SOUND_BULLETS.play()
    

#imprimir que sale en la flech
def manage_keys(keys, character, dimensions, bullets):
    if keys[character.key[0]]:
        if validate_edges(0, character.rect, 1):
            character.y -= character.speed
    if keys[character.key[1]]:
        if not validate_edges(dimensions['HIGH'], character.rect, 1):
             character.y += character.speed  
    if keys[character.key[2]]:
        if validate_edges(0, character.rect, 0):
            character.x -= character.speed
    if keys[character.key[3]]:
        if not validate_edges(dimensions['WIDTH'], character.rect, 0):
            character.x += character.speed
    if keys[character.key[4]]:
        create_bullet(character, bullets)
        
# Función para verificar el estado de los jugadores
def check_player_status(player_1, player_2):
    if player_1.lives <= 0:
        if not player_2 or player_2.lives <= 0:
            return "game_over"
        else:
            return "player_1 dead"
    elif player_2 and player_2.lives <= 0:
        return "player_2 dead"
    else:
        return "playing"
