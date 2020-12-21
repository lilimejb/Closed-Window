from config import *
from main_classes import Sprite
import pygame as pg


# Класс, отвечающий за всё что связано с игроком
class Player(Sprite):
    coins = None
    enemies = None
    help = None
    solid_blocks = None
    exits = None
    buffs = None

    def __init__(self, x=300, y=300, size=64, speed=.2, image=PLAYER_ASSETS['idle'][0]):
        super().__init__(x, y, size, speed, image)
        self.x_start = x
        self.y_start = y
        self.money = 0
        self.max_hp = 10
        self.start_hp = self.hp = self.max_hp - 4
        self.image_true = self.image
        self.damaged_image = PLAYER_ASSETS['take_hit'][1]
        self.image_flipped = pg.transform.flip(self.image, True, False)
        self.speed_y = 0
        self.speed_x = 0
        self.speed_start = 2
        self.speed_max = 5
        self.speed_max_buffed = 10
        self.jump_power_start = self.jump_power = 12
        self.jump_power_max_buffed = 18
        self.on_the_ground = False
        self.damage_delay = 1000
        self.cooldown = self.damage_delay

    def set_position(self, x, y):
        self.rect.x, self.rect.y = x, y
        self.x_start, self.y_start = x, y

    def update(self, jump, fall, left, right, ms):
        collide = self.collide_check(ms)
        self.move(jump, fall, left, right)
        if self.hp > self.max_hp:
            self.hp = self.max_hp
        elif self.hp <= 0:
            self.respawn()
        if collide == 'end':
            return 'end'

    def move(self, jump, fall, left, right):
        # обработка движения по оси x
        if left == right:
            self.speed_x *= .9
            if abs(self.speed_x) < .5:
                self.speed_x = 0
        elif left:
            self.speed_x -= self.speed
            self.image = self.image_flipped
            if abs(self.speed_x) > self.speed_max:
                self.speed_x = -self.speed_max
        elif right:
            self.speed_x += self.speed
            self.image = self.image_true
            if abs(self.speed_x) > self.speed_max:
                self.speed_x = self.speed_max

        self.rect.x += self.speed_x

        # обработка столкновений по оси x
        for block in self.solid_blocks:
            if pg.sprite.collide_rect(self, block):
                if self.speed_x < 0:
                    self.rect.left = block.rect.right
                    self.speed_x = 0
                else:
                    self.rect.right = block.rect.left
                    self.speed_x = 0

        # обработка движения по оси y
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
        if self.rect.top <= 0:
            self.rect.top = 0

        # обработка столкновений по оси y
        is_collide = False

        for block in self.solid_blocks:
            if pg.sprite.collide_rect(self, block):
                if self.speed_y < 0:
                    self.rect.top = block.rect.bottom
                    self.speed_y = 0
                else:
                    self.rect.bottom = block.rect.top
                    self.on_the_ground = True
            if -TILE_SIZE < self.rect.x - block.rect.x < TILE_SIZE:
                if block.rect.top == self.rect.bottom:
                    is_collide = True
        if self.rect.y < 0:
            self.rect.y = 0
            self.speed_y = 0
        self.on_the_ground = is_collide

    def collide_check(self, ms):
        # сбор монет
        for coin in self.coins:
            if pg.sprite.collide_rect(self, coin):
                self.money += coin.value
                coin.kill()

        # столкновение с противниками
        for enemy in self.enemies:
            if pg.sprite.collide_rect(self, enemy):
                self.hp -= self.take_damage(ms, enemy.damage)

        # сбор еды
        for food in self.help:
            if pg.sprite.collide_rect(self, food):
                self.hp += self.take_hp(food.heal)
                food.kill()

        # сбор положительных/отрицательных эффектов
        # TODO реалицовать функцию нормально
        for buff in self.buffs:
            if pg.sprite.collide_rect(self, buff):
                if buff.name == 'Speed_boost':
                    self.speed_max += buff.boost
                    if self.speed_max > self.speed_max_buffed:
                        self.speed_max = self.speed_max_buffed
                if buff.name == 'Jump_boost':
                    self.jump_power += buff.boost
                    if self.jump_power > self.jump_power_max_buffed:
                        self.jump_power = self.jump_power_max_buffed
                if buff.name == 'Speed_down':
                    self.speed_max -= buff.boost
                    if self.speed_max < self.speed_start:
                        self.speed_max = self.speed_start
                if buff.name == 'Jump_down':
                    self.jump_power -= buff.boost
                    if self.jump_power < self.jump_power_start:
                        self.jump_power = self.jump_power_start
                buff.kill()

        # столкновение с "колодцем"
        for block in self.exits:
            if pg.sprite.collide_rect(self, block) and len(self.coins) < 2:
                return 'end'

    def respawn(self):
        self.rect.topleft = (self.x_start, self.y_start)
        self.money = self.money // 10
        self.max_hp = 10
        self.start_hp = self.hp = self.max_hp - 4
        self.speed_y = 0
        self.speed_x = 0
        self.speed_max = 5
        self.jump_power = self.jump_power_start

    def take_damage(self, ms, damage):
        if self.cooldown < self.damage_delay:
            self.cooldown += ms
            return 0
        if self.cooldown >= self.damage_delay:
            self.cooldown = 0
        if self.cooldown == self.damage_delay or self.cooldown == 0:
            self.cooldown = 0
            return damage

    def take_hp(self, heal):
        return heal
