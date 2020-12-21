from config import *
from main_classes import Sprite, Solid_Block
import pygame as pg


# Главный класс для всех врагов в игре
class Enemy(Sprite):
    solid_blocks = None

    def __init__(self, x=300, y=300, size=64, speed=2, damage=2, image=ENEMIES['bearded_idle'][0]):
        super().__init__(x, y, size, speed, image)
        self.way = 'right'
        self.name = 'enemy'
        self.damage = damage
        self.image_flipped = pg.transform.flip(self.image, True, False)
        self.image_true = self.image
        self.spawn_point = self.rect.topleft
        self.delta = 100

    def update(self):
        self.move()

    def move(self):
        # обработка перемещения по оси x
        if self.way == 'right':
            self.rect.x += self.speed
            self.image = self.image_true
        elif self.way == 'left':
            self.rect.x -= self.speed
            self.image = self.image_flipped
        if self.rect.x >= self.spawn_point[0] + self.delta:
            self.way = 'left'
        elif self.rect.x <= self.spawn_point[0]:
            self.way = 'right'

        # обработка столкновений по оси x
        for block in self.solid_blocks:
            if pg.sprite.collide_rect(self, block):
                if self.rect.left >= block.rect.right:
                    self.rect.left = block.rect.right
                    self.way = 'right'
                else:
                    self.rect.right = block.rect.left
                    self.way = 'left'


# Класс для врага "Бородач"
class Bearded(Enemy):
    def __init__(self, x=300, y=300, size=64, speed=1, damage=4, image=ENEMIES['bearded_idle'][0]):
        super().__init__(x, y, size, speed, damage, image)
        self.name = 'bearded'
        self.delta = 200


# Класс для блока-врага
class Spike(Solid_Block):
    def __init__(self, x=None, y=None, damage=1, size=64, speed=10, image=ENEMIES['spike']):
        super().__init__(x, y, size, speed, image)
        self.damage = damage
