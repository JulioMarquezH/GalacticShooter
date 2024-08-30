import pygame


# constantes

HIGH = 50
WIDTH = 50
SPEED = 8
COLOR = 'blue'
KEY = []
LIVES = 0
INTERVAL = 250
LAST_BULLET = 0
IMAGE = "media/images/plane.svg"


class Protagonist:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.width = WIDTH
        self.high = HIGH
        self.speed = SPEED
        self.color = COLOR
        self.key = KEY
        self.lives = LIVES
        self.interval = INTERVAL
        self.last_bullet = LAST_BULLET
        self.rect = pygame.Rect(self.x, self.y, self.width, self.high)
        self.image = pygame.image.load(IMAGE)
        self.image = pygame.transform.scale(self.image, (self.width,self.high))
        
    def paint(self, ventana):
        self.rect = pygame.Rect(self.x, self.y, self.width, self.high)
        ventana.blit(self.image, (self.x, self.y))
        
