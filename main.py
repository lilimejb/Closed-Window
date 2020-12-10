from config import *
import pygame as pg

clock = pg.time.Clock()


class Game:
    def __init__(self):
        pg.init()
        self.running = True
        self.screen = pg.display.set_mode(WIN_SIZE)

    def events(self):
        events = pg.event.get()
        for event in events:
            if event.type == pg.QUIT:
                self.running = False

    def update(self):
        clock.tick(FPS)

    def render(self):
        self.screen.fill(BG_COLOR)
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
