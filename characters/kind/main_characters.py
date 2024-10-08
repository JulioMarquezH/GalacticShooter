import pygame


# constantes

HIGH = 50
WIDTH = 50
SPEED = 6
SPEED_MAX = 15
SPEED_MIN = 2
COLOR = 'blue'
KEY = []
LIVES = 0
INTERVAL = 150
LAST_BULLET = 0
IMAGE = "media/images/plane.svg"


class Protagonist:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.width = WIDTH
        self.high = HIGH
        self.speed = SPEED
        self.speed_max = SPEED_MAX
        self.speed_min = SPEED_MIN
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
        
