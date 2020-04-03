import random
import pygame
from pygame.sprite import Sprite


class Player(Sprite):
    def __init__(self, x, y, role_image_path):
        Sprite.__init__(self)
        self.role_name = role_image_path.split('/')[-1].split('.')[0]
        self.base_image = pygame.image.load(role_image_path).convert()
        self.image = self.base_image.copy()
        self.rect = self.image.get_rect()
        self.rect.left = x
        self.rect.top = y
        self.prev_x = x
        self.prev_y = y
        self.base_speed = [30, 30]
        self.speed = [0, 0]
        self.is_move = False
        self.tracks = []
        self.tracks_loc = [0, 0]

    def change_speed(self, direction):
        if direction[0] < 0:
            self.image = pygame.transform.flip(self.base_image, True, False)
        elif direction[0] > 0:
            self.image = self.base_image.copy()
        elif direction[1] < 0:
            self.image = pygame.transform.rotate(self.base_image, 90)
        elif direction[1] > 0:
            self.image = pygame.transform.rotate(self.base_image, -90)
        self.speed = [direction[0] * self.base_speed[0], direction[1] * self.base_speed[1]]
        return self.speed

    def update(self, wall_sprites, gate_sprites):
        if not self.is_move:
            return False
        x_prev = self.rect.left
        y_prev = self.rect.top
        self.rect.left += self.speed[0]
        self.rect.top += self.speed[1]
        is_collide = pygame.sprite.spritecollide(self, wall_sprites, False)
        if gate_sprites is not None:
            if not is_collide:
                is_collide = pygame.sprite.spritecollide(self, gate_sprites, False)
        if is_collide:
            self.rect.left = x_prev
            self.rect.top = y_prev
            return False
        return True

    def random_direction(self):
        return random.choice([[-0.5, 0], [0.5, 0], [0, 0.5], [0, -0.5]])