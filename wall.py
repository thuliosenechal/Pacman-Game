import pygame
from pygame.sprite import Sprite


class Wall(Sprite):
    def __init__(self, x, y, width, height, color, **kwargs):
        Sprite.__init__(self)
        self.image = pygame.Surface([width, height])
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.left = x
        self.rect.top = y