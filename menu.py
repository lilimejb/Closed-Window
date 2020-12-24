import pygame as pg
from config import *


# Класс, отвечающий за всё что связанно с начальным экраном
# TODO сделать не криво
class Menu:
    def __init__(self):
        self.font = pg.font.SysFont(None, 64)
        self.running = True
        self.screen = pg.display.set_mode(WIN_SIZE)
        self.background = pg.image.load(MENU_BACKGROUND)
        self.background = pg.transform.scale(self.background, WIN_SIZE)

    # обработка всех событий
    def events(self):
        events = pg.event.get()
        for event in events:
            if event.type == pg.QUIT:
                self.running = False
                return 'all down'
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_SPACE:
                    self.running = False
                    return 'window down'

    def render_text(self):
        text = f'Нажмите "Пробел" чтобы начать'
        image = self.font.render(text, True, (69, 126, 172))
        image_rect = image.get_rect()
        image_rect.center = WIN_SIZE[0] // 2, int(WIN_SIZE[1] // 2 * 0.25)
        self.screen.blit(image, image_rect)

    def render(self):
        self.screen.blit(self.background, (0, 0))
        self.render_text()
        pg.display.update()

    # функция запуска меню
    def run(self):
        while self.running:
            down = self.events()
            self.render()
        return down
