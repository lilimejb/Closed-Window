import random

import pygame as pg

from config import *


# Главный класс для всех объектов в игре
class Sprite(pg.sprite.Sprite):
    def __init__(self, x=0, y=0, size=100, speed=10, image=PLAYER_ASSETS['idle'][0]):
        super().__init__()
        self.name = 'basic_sprite'
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

    def update(self, *args):
        pass


# Главный класс для всех твёрдых блоков в игре
class Solid_Block(Sprite):
    def __init__(self, x=0, y=0, size=64, speed=10, image=BLOCK_ASSETS['ground'][0]):
        super().__init__(x, y, size, speed, image)


# Главный класс для всех подбираемых предметов в игре
class Consumable(Sprite):
    def __init__(self, x=None, y=None, size=100, speed=10, image=BLOCK_ASSETS['ground'][0]):
        super().__init__(x, y, size, speed, image)
        self.ticks = random.choice(range(0, 360, 5))
        self.forward = 1
        self.spawn = self.rect.topleft

    def update(self, *args):
        pass
        # if self.ticks >= 360:
        #     self.ticks -= 360
        # self.ticks += 5
        # if not self.speed:
        #     return
        # not_true_y = sin(radians(self.ticks)) * self.speed
        # self.rect.y = self.spawn[1] + not_true_y


class Camera:
    # зададим начальный сдвиг камеры
    def __init__(self):
        self.dx = 0
        self.dy = 0

    # сдвинуть объект obj на смещение камеры
    def apply(self, obj):
        obj.rect.x += self.dx
        obj.rect.y += self.dy

    # позиционировать камеру на объекте target
    def update(self, target):
        self.dx = -(target.rect.x + target.rect.w // 2 - WIN_SIZE[0] // 2)
        self.dy = -(target.rect.y + target.rect.h // 2 - WIN_SIZE[1] // 2)


class Animated_Sprite(Sprite):
    def __init__(self, x=0, y=0, size=100, speed=10, image_dictionary=PLAYER_ASSETS):
        super().__init__(x, y, size, speed, image_dictionary['idle'][0])
        self.size = size
        self.speed = speed
        self.x = x
        self.y = y
        self.speed_x = 0
        self.speed_y = 0
        self.images = {}
        self.flipped_images = {}
        self.animator_counters = 0
        self.frames = 0
        self.is_flipped = False

        for key in image_dictionary.keys():
            self.images[key] = [pg.transform.scale(pg.image.load(i), (size, size)) for i in
                                image_dictionary[key]]

        for key in self.images:
            self.flipped_images[key] = [pg.transform.flip(i, True, False) for i in self.images[key]]

    def make_animation(self, is_attacking, hp, collide):
        self.animator_counters += 1
        if is_attacking:
            if self.animator_counters == 3:
                self.make_attack_animation()
                self.frames += 1
                self.animator_counters = 0
        if collide == 'hit_taken':
            if self.animator_counters == 5:
                self.make_take_hit_animation()
                self.frames += 1
                self.animator_counters = 0
        if hp <= 0:
            if self.animator_counters == 5:
                self.make_death_animation()
                self.frames += 1
                self.animator_counters = 0
                return 'game_over'
        if self.animator_counters == 5:
            self.make_move_animation(self.speed_x, self.speed_y)
            self.frames += 1
            self.animator_counters = 0

    def make_death_animation(self):
        if self.is_flipped:
            self.image = self.flipped_images['death'][self.frames % len(self.images['death'])]
        else:
            self.image = self.images['death'][self.frames % len(self.images['death'])]

    def make_move_animation(self, speed_x, speed_y):
        if speed_x > 0:
            self.is_flipped = False
        if speed_x < 0:
            self.is_flipped = True
        if speed_x == 0 and speed_y == 0:
            if self.is_flipped:
                self.image = self.flipped_images['idle'][self.frames % len(self.images['idle'])]
            else:
                self.image = self.images['idle'][self.frames % len(self.images['idle'])]

        elif speed_y < 0:
            if self.is_flipped:
                self.image = self.flipped_images['jump'][self.frames % len(self.images['jump'])]
            else:
                self.image = self.images['jump'][self.frames % len(self.images['jump'])]

        elif speed_y > 0:
            if self.is_flipped:
                self.image = self.flipped_images['fall'][self.frames % len(self.images['fall'])]
            else:
                self.image = self.images['fall'][self.frames % len(self.images['fall'])]

        elif speed_x > 0:
            self.image = self.images['run'][self.frames % len(self.images['run'])]

        elif speed_x < 0:
            self.image = self.flipped_images['run'][self.frames % len(self.images['run'])]

    def make_attack_animation(self):
        if self.is_flipped:
            self.image = self.flipped_images['attack'][self.frames % len(self.images['attack'])]
        else:
            self.image = self.images['attack'][self.frames % len(self.images['attack'])]

    def make_take_hit_animation(self):
        if self.is_flipped:
            self.image = self.flipped_images['take_hit'][self.frames % len(self.images['take_hit'])]
        else:
            self.image = self.images['take_hit'][self.frames % len(self.images['take_hit'])]
