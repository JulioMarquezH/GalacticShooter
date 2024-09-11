import pygame

# constantes

HIGH = 20
WIDTH = 20
SPEED = 15
COLOR = '#ffffff'
DAMAGE = 1
IMAGE= "media/images/bullets.svg"

class Bullets:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.width = WIDTH
        self.high = HIGH
        self.speed = SPEED
        self.color = COLOR
        self.damage = DAMAGE
        self.rect = pygame.Rect(self.x, self.y, self.width, self.high)
        self.image = pygame.image.load(IMAGE)
        self.image = pygame.transform.scale(self.image, (self.width,self.high))
        self.image = pygame.transform.rotate(self.image, 90)
        
    def paint(self, ventana):
        self.rect = pygame.Rect(self.x, self.y, self.width, self.high)
        ventana.blit(self.image, (self.x, self.y))

        
    def move(self):
        self.y -= self.speed
