import pygame as pg
from config import *


# Класс, отвечающий за всё что связанно с начальным экраном
class End_window:
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

    def render_text(self, time, money, hp):
        text = [f'Вы прошли Клозед Виндоу!',
                f'Время в игре: {time}',
                f'Монеты: {money}']
        for i in range(len(text)):
            image = self.font.render(text[i], True, (69, 126, 172))
            image_rect = image.get_rect()
            image_rect.center = WIN_SIZE[0] // 2, int(WIN_SIZE[1] // 2 * 0.25) + i * 100
            self.screen.blit(image, image_rect)

    def render(self, time, money, hp):
        self.screen.blit(self.background, (0, 0))
        self.render_text(time, money, hp)
        pg.display.update()

    # функция запуска меню
    def run(self, time, money, hp):
        while self.running:
            self.events()
            self.render(time, money, hp)
