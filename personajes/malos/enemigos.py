import pygame

# constantes

ALTO = 35
ANCHO = 35
VELOCIDAD = 4
COLOR = 'red'
DAÑO = 1
VIDA = 3
IMAGEN = "media/imagenes/enemigo.svg"



class Enemigos_basicos:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.ancho = ANCHO
        self.alto = ALTO
        self.velocidad = VELOCIDAD
        self.color = COLOR
        self.daño = DAÑO
        self.vida = VIDA
        self.rect = pygame.Rect(self.x, self.y, self.ancho, self.alto)
        self.imagen = pygame.image.load(IMAGEN)
        self.imagen = pygame.transform.scale(self.imagen, (self.ancho,self.alto))
        
    def pintar(self, ventana):
        self.rect = pygame.Rect(self.x, self.y, self.ancho, self.alto)
        # pygame.draw.rect(ventana, self.color, self.rect)
        ventana.blit(self.imagen, (self.x, self.y))

        
    def movimiento(self):
        self.y += self.velocidad