import pygame as pg
from config import *
from sprite import Sprite


class Player(Sprite):
    coins = None
    enemies = None
    help = None
    solid_blocks = None

    def __init__(self, x=300, y=300, size=100, speed=.2, image=PLAYER_ASSETS['idle'][0]):
        super().__init__(x, y, size, speed, image)
        self.money = 0
        self.max_hp = 10
        self.start_hp = self.hp = self.max_hp - 4
        self.image_true = self.image
        self.damaged_image = PLAYER_ASSETS['take_hit'][1]
        self.image_flipped = pg.transform.flip(self.image, True, False)
        self.speed_y = 0
        self.speed_x = 0
        self.speed_max = 10
        self.jump_power = 12
        self.on_the_ground = False
        self.damage_delay = 1000
        self.cooldown = self.damage_delay

    def update(self, jump, fall, left, right, ms):
        self.move(jump, fall, left, right)
        self.collide_check(ms)
        if self.hp > self.max_hp:
            self.hp = self.max_hp
        elif self.hp <= 0:
            self.respawn()

    def move(self, jump, fall, left, right):
        if left == right:
            self.speed_x = 0
        elif left:
            self.speed_x -= self.speed
            self.image = self.image_flipped
        else:
            self.speed_x += self.speed
            self.image = self.image_true
        if self.speed_x > self.speed_max:
            self.speed_x = self.speed_max
        self.rect.x += self.speed_x
        for block in self.solid_blocks:
            if pg.sprite.collide_rect(self, block):
                if self.speed_x < 0:
                    self.rect.left = block.rect.right
                    self.speed_x = 0
                else:
                    self.rect.right = block.rect.left
                    self.speed_x = 0
        if jump == fall:
            pass
        if not self.on_the_ground:
            self.speed_y += GRAVITY
        else:
            self.speed_y = 0
        if jump and self.on_the_ground:
            self.speed_y -= self.jump_power
            self.on_the_ground = False
        self.rect.bottom += self.speed_y
        for block in self.solid_blocks:
            if pg.sprite.collide_rect(self, block):
                if self.speed_y < 0:
                    self.rect.top = block.rect.bottom
                    self.speed_y = 0
                else:
                    self.rect.bottom = block.rect.top
                    self.on_the_ground = True

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
