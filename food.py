import pygame
from pygame.sprite import Sprite


class Food(Sprite):
    def __init__(self, x, y, width, height, color, bg_color, **kwargs):
        Sprite.__init__(self)
        self.image = pygame.Surface([width, height])
        self.image.fill(bg_color)
        self.image.set_colorkey(bg_color)
        pygame.draw.ellipse(self.image, color, [0, 0, width, height])
        self.rect = self.image.get_rect()
        self.rect.left = x
        self.rect.top = y