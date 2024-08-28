import pygame


# constantes

ALTO = 50
ANCHO = 50
VELOCIDAD = 8
COLOR = 'blue'
TECLAS = []
VIDA = 0
INTERVALO = 250
IMAGEN = "media/imagenes/avion.svg"
ULTIMA_BALA = 0

class Protagonista:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.ancho = ANCHO
        self.alto = ALTO
        self.velocidad = VELOCIDAD
        self.color = COLOR
        self.teclas = TECLAS
        self.vida = VIDA
        self.intervalo_entre_balas = INTERVALO
        self.ultima_bala = ULTIMA_BALA
        self.rect = pygame.Rect(self.x, self.y, self.ancho, self.alto)
        self.imagen = pygame.image.load(IMAGEN)
        self.imagen = pygame.transform.scale(self.imagen, (self.ancho,self.alto))
        
    def pintar(self, ventana):
        self.rect = pygame.Rect(self.x, self.y, self.ancho, self.alto)
        # pygame.draw.rect(ventana, self.color, self.rect)
        ventana.blit(self.imagen, (self.x, self.y))
        
