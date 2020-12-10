import pygame as pg
from config import *


class Sprite(pg.sprite.Sprite):
    def __init__(self, x=0, y=0, size=100, speed=10, image=PLAYER_ASSETS['idle'][0]):
        pg.sprite.Sprite.__init__(self)
        self.size = size
        self.speed = speed
        self.x = x
        self.y = y
        self.image = pg.image.load(image)
        self.image = pg.transform.scale(self.image, (self.size, self.size))
        self.rect = self.image.get_rect()
        self.rect = self.rect.move(x, y)

    def draw(self, surface):
        surface.blit(self.image, self.rect.topleft)

    def border_check(self):
        if self.rect.left < 0:
            self.rect.left = 0

        if self.rect.right > WIN_SIZE[0]:
            self.rect.right = WIN_SIZE[0]

        if self.rect.top < 0:
            self.rect.top = 0

        if self.rect.bottom > WIN_SIZE[1]:
            self.rect.bottom = WIN_SIZE[1]

    def update(self, *args):
        pass
