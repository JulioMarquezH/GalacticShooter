import pygame

# constantes

ALTO = 20
ANCHO = 20
VELOCIDAD = 8
COLOR = '#ffffff'
DAÑO = 1
IMAGEN= "media/imagenes/balas.svg"

class Balas:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.ancho = ANCHO
        self.alto = ALTO
        self.velocidad = VELOCIDAD
        self.color = COLOR
        self.daño = DAÑO
        self.rect = pygame.Rect(self.x, self.y, self.ancho, self.alto)
        self.imagen = pygame.image.load(IMAGEN)
        self.imagen = pygame.transform.scale(self.imagen, (self.ancho,self.alto))
        self.imagen = pygame.transform.rotate(self.imagen, 90)
        
    def pintar(self, ventana):
        self.rect = pygame.Rect(self.x, self.y, self.ancho, self.alto)
        # pygame.draw.rect(ventana, self.color, self.rect)
        ventana.blit(self.imagen, (self.x, self.y))

        
    def movimiento(self):
        self.y -= self.velocidad