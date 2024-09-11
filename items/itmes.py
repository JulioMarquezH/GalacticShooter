import pygame
from items.typeItems import TYPE_ITEMS
from utils import utils


# constantes

HIGH = 30
WIDTH = 30
SPEED = 5
COLOR = '#ffffff'
# IMAGE= "media/images/bullets.svg"

class Items:
    def __init__(self, x, y, item):
        # item = utils.filter_by_type(type, TYPE_ITEMS)[0]
        self.x = x
        self.y = y
        self.width = WIDTH
        self.high = HIGH
        self.speed = SPEED
        self.color = COLOR
        self.attributes = item
        self.rect = pygame.Rect(self.x, self.y, self.width, self.high)
        self.image = pygame.image.load(item['icon'])
        self.image = pygame.transform.scale(self.image, (self.width,self.high))
        self.image = pygame.transform.rotate(self.image, item['direction'])
        
    def paint(self, ventana):
        self.rect = pygame.Rect(self.x, self.y, self.width, self.high)
        ventana.blit(self.image, (self.x, self.y))

        
    def move(self):
        self.y += self.speed