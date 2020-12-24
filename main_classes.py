from config import *
import random
import pygame as pg


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


class Animator:
    def __init__(self):
        self.frames = -1
        self.is_flipped = False

    def make_animation(self, sprite, pictures, flipped_pictures):
        if sprite.speed_x == 0 and sprite.speed_y == 0:
            self.frames += 1
            if self.is_flipped:
                return flipped_pictures['idle'][self.frames % len(pictures['idle'])]
            else:
                return pictures['idle'][self.frames % len(pictures['idle'])]

        elif sprite.speed_y < 0:
            self.frames += 1
            if self.is_flipped:
                return flipped_pictures['jump'][self.frames % len(pictures['jump'])]
            else:
                return pictures['jump'][self.frames % len(pictures['jump'])]

        elif sprite.speed_y > 0:
            self.frames += 1
            if self.is_flipped:
                return flipped_pictures['fall'][self.frames % len(pictures['fall'])]
            else:
                return pictures['fall'][self.frames % len(pictures['fall'])]

        elif sprite.speed_x > 0:
            self.frames += 1
            self.is_flipped = False
            return pictures['run'][self.frames % len(pictures['run'])]

        elif sprite.speed_x < 0:
            self.frames += 1
            self.is_flipped = True
            return flipped_pictures['run'][self.frames % len(pictures['run'])]
