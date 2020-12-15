import random

from config import *
from sprite import Sprite
from math import radians, sin


class Solid_Block(Sprite):
    def __init__(self, x=None, y=None, size=64, speed=10, image=BLOCK_ASSETS['ground'][0]):
        super().__init__(x, y, size, speed, image)


class Consumable(Sprite):
    def __init__(self, x=None, y=None, size=100, speed=10, image=BLOCK_ASSETS['ground'][0]):
        super().__init__(x, y, size, speed, image)
        self.ticks = random.choice(range(0, 360, 5))
        self.forward = 1
        self.spawn = self.rect.topleft

    def update(self, *args):
        if self.ticks >= 360:
            self.ticks -= 360
        self.ticks += 5
        if not self.speed:
            return
        not_true_y = sin(radians(self.ticks)) * self.speed
        self.rect.y = self.spawn[1] + not_true_y


class Spike(Solid_Block):
    def __init__(self, x=None, y=None, damage=1, size=64, speed=10, image=SPIKE):
        if x is None:
            x = random.randint(0, WIN_SIZE[0] - size)
        if y is None:
            y = random.randint(0, WIN_SIZE[1] - size)
        super().__init__(x, y, size, speed, image)
        self.damage = damage


class Coin(Consumable):
    def __init__(self, x=None, y=None, value=5, size=50, speed=10, image=COINS[0]):
        if x is None:
            x = random.randint(0, WIN_SIZE[0] - size)
        if y is None:
            y = random.randint(0, WIN_SIZE[1] - size)
        super().__init__(x, y, size, speed, image)
        self.ticks = random.choice(range(0, 360, 5))
        self.forward = 1
        self.spawn = self.rect.topleft
        self.value = value


class Medicine(Consumable):
    def __init__(self, x=None, y=None, healing=500, size=50, speed=10, image=FOOD[0]):
        if x is None:
            x = random.randint(0, WIN_SIZE[0] - size)
        if y is None:
            y = random.randint(0, WIN_SIZE[1] - size)
        super().__init__(x, y, size, speed, image)
        self.heal = healing

        self.ticks = random.choice(range(0, 360, 5))
        self.forward = 1
        self.spawn = self.rect.topleft


class Speed_boost(Consumable):
    def __init__(self, x=None, y=None, boost=5, size=50, speed=10, image=FOOD[0]):
        if x is None:
            x = random.randint(0, WIN_SIZE[0] - size)
        if y is None:
            y = random.randint(0, WIN_SIZE[1] - size)
        super().__init__(x, y, size, speed, image)
        self.name = 'Speed_boost'
        self.boost = boost


class Jump_boost(Consumable):
    def __init__(self, x=None, y=None, boost=10, size=50, speed=10, image=FOOD[0]):
        if x is None:
            x = random.randint(0, WIN_SIZE[0] - size)
        if y is None:
            y = random.randint(0, WIN_SIZE[1] - size)
        super().__init__(x, y, size, speed, image)
        self.name = 'Jump_boost'
        self.boost = boost


class Level_end(Solid_Block):
    def __init__(self, x=None, y=None, size=64, speed=10, image=WELL):
        super().__init__(x, y, size, speed, image)
