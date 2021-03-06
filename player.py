from config import *
from main_classes import Animated_Sprite
import pygame as pg


# Класс, отвечающий за всё что связано с игроком
class Player(Animated_Sprite):
    coins = None
    enemies = None
    spikes = None
    help = None
    solid_blocks = None
    exits = None
    buffs = None

    def __init__(self, x=300, y=300, size=64, speed=.2, images=PLAYER_ASSETS):
        super().__init__(x, y, size, speed, images)
        self.x_start = x
        self.y_start = y
        self.money = 0
        self.max_hp = 10
        self.start_hp = self.hp = self.max_hp - 4
        self.image_true = self.image
        self.image_flipped = pg.transform.flip(self.image, True, False)
        self.speed_y = 0
        self.speed_x = 0
        self.speed_start = 5
        self.speed_max = 10
        self.speed_max_buffed = 15
        self.jump_power_start = self.jump_power = 12
        self.jump_power_max_buffed = 18
        self.on_the_ground = False
        self.damage_delay = 1000
        self.cooldown = self.damage_delay
        self.attack_cooldown = self.damage_delay

    def set_position(self, x, y):
        self.rect.x, self.rect.y = x, y
        self.x_start, self.y_start = x, y

    def respawn(self):
        self.rect.topleft = (self.x_start, self.y_start)
        self.money = self.money // 10
        self.max_hp = 10
        self.start_hp = self.hp = self.max_hp - 4
        self.speed_y = 0
        self.speed_x = 0
        self.speed_max = self.speed_start
        self.jump_power = self.jump_power_start

    def update(self, jump, fall, left, right, is_attacking, ms):
        collide = self.collide_check(is_attacking, ms)
        self.move(jump, fall, left, right)
        game_state = self.make_animation(is_attacking, self.hp, collide)
        if self.hp > self.max_hp:
            self.hp = self.max_hp
        if self.hp <= 0:
            self.respawn()
            return 'dead'
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
            if abs(self.speed_x) > self.speed_max:
                self.speed_x = -self.speed_max
        elif right:
            self.speed_x += self.speed
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

    def collide_check(self, is_attacking, ms):
        # сбор монет
        for coin in self.coins:
            if pg.sprite.collide_rect(self, coin):
                self.money += coin.value
                coin.kill()

        # столкновение с противниками
        for enemy in self.enemies:
            if pg.sprite.collide_rect(self, enemy):
                damage = self.take_damage(ms, enemy.damage)
                self.hp -= damage
                if is_attacking:
                    enemy.kill()
                    self.money += 5

        for spike in self.spikes:
            if pg.sprite.collide_rect(self, spike):
                damage = self.take_damage(ms, spike.damage)
                self.hp -= damage

        # сбор еды
        for food in self.help:
            if pg.sprite.collide_rect(self, food):
                self.hp += self.take_hp(food.heal)
                food.kill()

        # сбор положительных/отрицательных эффектов
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
            if pg.sprite.collide_rect(self, block) and len(self.coins) < 2 and not self.enemies:
                self.speed_x = 0
                self.speed_y = 0
                return 'end'

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
