from config import *
import pygame as pg
from player import Player
from utility import *

clock = pg.time.Clock()


class Game:
    def __init__(self):
        pg.init()
        self.current_level = 0
        self.running = True
        self.screen = pg.display.set_mode(WIN_SIZE)
        self.background = pg.image.load(BACKGROUND)
        self.background = pg.transform.scale(self.background, WIN_SIZE)
        self.right = False
        self.left = False
        self.jump = False
        self.fall = False
        self.player = Player()
        self.objects = pg.sprite.Group()
        self.coins = pg.sprite.Group()
        self.enemies = pg.sprite.Group()
        self.solid_blocks = pg.sprite.Group()
        self.help = pg.sprite.Group()
        self.exits = pg.sprite.Group()
        self.buffs = pg.sprite.Group()
        self.current_level = 0
        self.load_map()
        self.player.help = self.help
        self.player.coins = self.coins
        self.player.enemies = self.enemies
        self.player.exits = self.exits
        self.player.buffs = self.buffs
        self.player.solid_blocks = self.solid_blocks

    def load_sprites(self):
        self.objects = pg.sprite.Group()
        self.coins = pg.sprite.Group()
        self.enemies = pg.sprite.Group()
        self.solid_blocks = pg.sprite.Group()
        self.help = pg.sprite.Group()
        self.exits = pg.sprite.Group()
        self.buffs = pg.sprite.Group()
        self.load_map()
        self.player.help = self.help
        self.player.coins = self.coins
        self.player.enemies = self.enemies
        self.player.exits = self.exits
        self.player.buffs = self.buffs
        self.player.solid_blocks = self.solid_blocks

    def restart(self):
        self.load_sprites()
        self.current_level = 0

    def start_next_level(self):
        self.load_sprites()

    def events(self):
        events = pg.event.get()
        for event in events:
            if event.type == pg.QUIT:
                self.running = False
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_d:
                    self.right = True
                if event.key == pg.K_a:
                    self.left = True
                if event.key == pg.K_SPACE:
                    self.jump = True
                if event.key == pg.K_s:
                    self.fall = True
                if event.key == pg.K_r:
                    self.restart()
            if event.type == pg.KEYUP:
                if event.key == pg.K_d:
                    self.right = False
                if event.key == pg.K_a:
                    self.left = False
                if event.key == pg.K_SPACE:
                    self.jump = False
                if event.key == pg.K_s:
                    self.fall = False

    def load_map(self):
        map_path = LEVELS[self.current_level]
        with open(map_path, 'r', encoding='UTF-8') as file:
            for y, line in enumerate(file):
                for x, letter in enumerate(line):
                    if letter in MAP_BLOCKS.keys():
                        pos = (x * TILE_SIZE, y * TILE_SIZE)
                        image = MAP_BLOCKS[letter]
                        if letter == 'P':
                            block = self.player
                            block.set_position(*pos)
                        if letter in SOLID_BLOCKS:
                            block = Solid_Block(*pos, image=image)
                            block.add(self.solid_blocks)
                        if letter in CONSUMABLES:
                            if letter == 'C':
                                block = Coin(*pos, image=image)
                                block.add(self.coins)
                            elif letter == 'F':
                                block = Medicine(*pos, image=image)
                                block.add(self.help)
                            elif letter == 'H':
                                block = Speed_boost(*pos, image=image)
                                self.buffs.add(block)
                            elif letter == 'J':
                                block = Jump_boost(*pos, image=image)
                                self.buffs.add(block)
                            elif letter == 'R':
                                block = Jump_boost(*pos, image=image)
                                block.name = 'Jump_down'
                                self.buffs.add(block)
                            elif letter == 'L':
                                block = Speed_boost(*pos, image=image)
                                block.name = 'Speed_down'
                                self.buffs.add(block)
                        if letter == 'E':
                            block = Level_end(*pos, image=image)
                            block.add(self.exits)
                        if letter == 'S':
                            block = Spike(*pos, image=image)
                            block.add(self.enemies)
                        block.add(self.objects)

    def update(self):
        ms = clock.tick(FPS)
        end = self.player.update(self.jump, self.fall, self.left, self.right, ms)
        self.help.update()
        self.coins.update()
        self.buffs.update()
        pg.display.set_caption(f'Player`s money: {self.player.money} HP: {self.player.hp}')
        if end == 'end':
            self.current_level = (self.current_level + 1) % 2
            self.start_next_level()

    def render(self):
        self.screen.blit(self.background, (0, 0))
        self.objects.draw(self.screen)
        pg.display.update()

    def run(self):
        while self.running:
            self.events()
            self.update()
            self.render()


if __name__ == '__main__':
    game = Game()
    game.run()
    pg.quit()
