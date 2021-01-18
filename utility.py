from config import *
from main_classes import Consumable, Solid_Block


# Класс Монеты
class Coin(Consumable):
    def __init__(self, x=None, y=None, value=5, size=50, speed=10, image=COINS[0]):
        super().__init__(x, y, size, speed, image)
        self.value = value


# Класс Аптечки
class Medicine(Consumable):
    def __init__(self, x=None, y=None, healing=2, size=50, speed=10, image=FOOD[0]):
        super().__init__(x, y, size, speed, image)
        self.heal = healing


# Класс положительного/отрицательного эффекта: Скорость
class Speed_boost(Consumable):
    def __init__(self, x=None, y=None, boost=2, size=50, speed=10, image=BUFFS[2]):
        super().__init__(x, y, size, speed, image)
        self.name = 'Speed_boost'
        self.boost = boost


# Класс положительного/отрицательного эффекта: Прыжок
class Jump_boost(Consumable):
    def __init__(self, x=None, y=None, boost=2, size=50, speed=10, image=BUFFS[3]):
        super().__init__(x, y, size, speed, image)
        self.name = 'Jump_boost'
        self.boost = boost


# Класс "колодца"
class Level_end(Solid_Block):
    def __init__(self, x=None, y=None, size=64, speed=10, image=WELL):
        super().__init__(x, y, size, speed, image)
