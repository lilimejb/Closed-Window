from config import *
import pygame as pg
from player import Player
from utility import Coin, Medicine, Solid_Block, Spike

clock = pg.time.Clock()


class Game:
    def __init__(self):
        pg.init()
        self.running = True
        self.screen = pg.display.set_mode(WIN_SIZE)
        self.background = pg.image.load(BACKGROUND)
        self.background = pg.transform.scale(self.background, WIN_SIZE)
        self.right = False
        self.left = False
        self.jump = False
        self.fall = False
        self.objects = pg.sprite.Group()
        self.coins = pg.sprite.Group()
        self.enemies = pg.sprite.Group()
        self.solid_blocks = pg.sprite.Group()
        self.help = pg.sprite.Group()
        self.load_map()
        Player.help = self.help
        Player.coins = self.coins
        Player.enemies = self.enemies
        Player.solid_blocks = self.solid_blocks
        self.player = Player()
        self.player.add(self.objects)

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
        map_path = 'lvl1'
        with open(map_path, 'r', encoding='UTF-8') as file:
            for y, line in enumerate(file):
                for x, letter in enumerate(line):
                    if letter in MAP_BLOCKS.keys():
                        pos = (x * TILE_SIZE, y * TILE_SIZE)
                        image = MAP_BLOCKS[letter]
                        if letter in SOLID_BLOCKS:
                            if letter == 'B':
                                block = Solid_Block(*pos, image=image)
                                block.add(self.solid_blocks)
                            elif letter == 'S':
                                block = Spike(*pos, image=image)
                                block.add(self.enemies)
                        if letter in CONSUMABLES:
                            if letter == 'C':
                                block = Coin(*pos, image=image)
                                block.add(self.coins)
                            elif letter == 'F':
                                block = Medicine(*pos, image=image)
                                block.add(self.help)
                        block.add(self.objects)

    def update(self):
        ms = clock.tick(FPS)
        self.player.update(self.jump, self.fall, self.left, self.right, ms)
        self.help.update()
        self.coins.update()
        pg.display.set_caption(f'Player`s money: {self.player.money} HP: {self.player.hp}')

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
