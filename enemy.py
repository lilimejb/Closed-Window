from config import *
from main_classes import Animated_Sprite, Solid_Block
import pygame as pg


# Главный класс для всех врагов в игре
class Enemy(Animated_Sprite):
    solid_blocks = None

    def __init__(self, x=300, y=300, size=64, speed=2, damage=2, images=ENEMIES['bearded']):
        super().__init__(x, y, size, speed, images)
        self.way = 'right'
        self.name = 'enemy'
        self.damage = damage
        self.spawn_point = self.rect.topleft
        self.delta = 100
        self.speed_max = speed
        self.speed = speed / 10

    def update(self):
        self.move()
        self.make_animation()

    def move(self):
        # обработка перемещения по оси x
        if self.way == 'right':
            self.speed_x += self.speed
            if abs(self.speed_x) > self.speed_max:
                self.speed_x = self.speed_max
        elif self.way == 'left':
            self.speed_x -= self.speed
            if abs(self.speed_x) > self.speed_max:
                self.speed_x = -self.speed_max
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
        self.rect.x += self.speed_x


# Класс для врага "Бородач"
class Bearded(Enemy):
    def __init__(self, x=300, y=300, size=64, speed=1, damage=4, image=ENEMIES['bearded']):
        super().__init__(x, y, size, speed, damage, image)
        self.name = 'bearded'
        self.delta = 200

    def make_animation(self, **kwargs):
        self.animator_counters += 1
        if self.animator_counters == 5:
            if self.speed_x > 0:
                self.is_flipped = False
            if self.speed_x < 0:
                self.is_flipped = True
            if self.speed_x == 0 and self.speed_y == 0:
                if self.is_flipped:
                    self.image = self.flipped_images['idle'][self.frames % len(self.images['idle'])]
                else:
                    self.image = self.images['idle'][self.frames % len(self.images['idle'])]
                self.frames += 1
                self.animator_counters = 0

            elif self.speed_x > 0:
                self.image = self.images['run'][self.frames % len(self.images['run'])]
                self.frames += 1
                self.animator_counters = 0

            elif self.speed_x < 0:
                self.image = self.flipped_images['run'][self.frames % len(self.images['run'])]
                self.frames += 1
                self.animator_counters = 0


# Класс для блока-врага
class Spike(Solid_Block):
    def __init__(self, x=None, y=None, damage=1, size=64, speed=10, image=ENEMIES['spike']):
        super().__init__(x, y, size, speed, image)
        self.damage = damage
