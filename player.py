import pygame as pg
from config import *
from sprite import Sprite


class Player(Sprite):
    coins = None
    enemies = None
    help = None
    solid_blocks = None

    def __init__(self, x=0, y=0, size=100, speed=10, image=PLAYER_ASSETS['idle'][0]):
        super().__init__(x, y, size, speed, image)
        self.money = 0
        self.max_hp = 10
        self.start_hp = self.hp = self.max_hp - 4
        self.image_true = self.image
        self.damaged_image = PLAYER_ASSETS['take_hit'][1]
        self.image_flipped = pg.transform.flip(self.image, True, False)
        self.damage_delay = 1000
        self.cooldown = self.damage_delay

    def update(self, jump, fall, left, right, ms):
        self.move(jump, fall, left, right)
        self.border_check()
        self.collide_check(ms)
        if self.hp > self.max_hp:
            self.hp = self.max_hp
        elif self.hp <= 0:
            self.respawn()

    def collide_check(self, ms):
        for coin in self.coins:
            if pg.sprite.collide_rect(self, coin):
                self.money += coin.value
                coin.kill()

        for enemy in self.enemies:
            if pg.sprite.collide_rect(self, enemy):
                self.hp -= self.take_damage(ms, enemy.damage)

        for food in self.help:
            if pg.sprite.collide_rect(self, food):
                self.hp += food.heal
                food.kill()

    def move(self, jump, fall, left, right):
        if left == right:
            pass
        elif left:
            self.rect.x -= self.speed
            self.image = self.image_flipped
        else:
            self.rect.x += self.speed
            self.image = self.image_true
        if jump == fall:
            pass
        elif jump:
            self.rect.y -= self.speed
        else:
            self.rect.y += self.speed

    def respawn(self):
        self.__init__()

    def take_damage(self, ms, damage):
        if self.cooldown > 0:
            self.cooldown -= ms
            return 0
        if self.cooldown <= 0:
            self.cooldown = 0
        if self.cooldown == 0:
            self.cooldown = self.damage_delay
            return damage
