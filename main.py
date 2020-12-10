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
        self.right = False
        self.left = False
        self.jump = False
        self.fall = False
        self.objects = pg.sprite.Group()
        self.player = Player()
        self.objects.add(self.player)

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

    def update(self):
        ms = clock.tick(FPS)
        self.player.update(self.jump, self.fall, self.left, self.right, ms)

    def render(self):
        self.screen.fill(BG_COLOR)
        self.player.draw(self.screen)
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
