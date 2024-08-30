import pygame

# constantes

HIGH = 35
WIDTH = 35
SPEED = 4
COLOR = 'red'
DAMAGE = 1
LIVES = 3
IMAGE = "media/images/enemies.svg"

class Enemies_basic:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.width = WIDTH
        self.high = HIGH
        self.speed = SPEED
        self.color = COLOR
        self.damage = DAMAGE
        self.lives = LIVES
        self.rect = pygame.Rect(self.x, self.y, self.width, self.high)
        self.image = pygame.image.load(IMAGE)
        self.image = pygame.transform.scale(self.image, (self.width,self.high))
        
    def paint(self, ventana):
        self.rect = pygame.Rect(self.x, self.y, self.width, self.high)
        ventana.blit(self.image, (self.x, self.y))
        
    def move(self):
        self.y += self.speed