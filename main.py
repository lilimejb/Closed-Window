# подключение библиотек
from end_window import End_window
from enemy import *
from main_classes import Camera
from menu import Menu
from player import Player
from utility import *

clock = pg.time.Clock()


# функция запуска музыки
def play_music(music):
    pg.mixer.init()
    pg.mixer.music.load(music)
    pg.mixer.music.play(-1)


# Главный класс игры
class Game:
    def __init__(self):
        pg.init()

        # инициализая будевых переменных для запуска игры
        self.running = True
        self.game_running = True

        # инициализация экзэмпляров классов
        self.menu = Menu()
        self.end_window = End_window()
        self.player = Player()
        self.camera = None

        # создание экрана
        self.screen = pg.display.set_mode(WIN_SIZE)
        self.background = pg.image.load(BACKGROUND)
        self.background = pg.transform.scale(self.background, WIN_SIZE)

        # инициализация булевых переменных для действий игрока
        self.right = False
        self.left = False
        self.jump = False
        self.fall = False
        self.is_attacking = False

        # инициалицация основных групп спрайтов
        self.objects = pg.sprite.Group()
        self.coins = pg.sprite.Group()
        self.enemies = pg.sprite.Group()
        self.spikes = pg.sprite.Group()
        self.solid_blocks = pg.sprite.Group()
        self.help = pg.sprite.Group()
        self.exits = pg.sprite.Group()
        self.buffs = pg.sprite.Group()

        # загрузка уровня
        self.current_level = 0
        self.load_map()

        self.camera_usage = True

        for enemy in self.enemies:
            if enemy.name == 'bearded':
                enemy.solid_blocks = self.solid_blocks

        self.player.help = self.help
        self.player.coins = self.coins
        self.player.enemies = self.enemies
        self.player.spikes = self.spikes
        self.player.exits = self.exits
        self.player.buffs = self.buffs
        self.player.solid_blocks = self.solid_blocks

        self.music = BATTLE_THEME
        self.is_playing = True
        self.has_changed = False
        self.played = 0

    # функция для запуска меню
    def start_menu(self):
        down = self.menu.run()
        return down

    # функция создающая группы спрайтов и экзэмпляры классов
    def load_sprites(self):
        self.objects.empty()
        self.coins.empty()
        self.enemies.empty()
        self.spikes.empty()
        self.solid_blocks.empty()
        self.help.empty()
        self.exits.empty()
        self.buffs.empty()
        self.load_map()
        for enemy in self.enemies:
            if enemy.name == 'bearded':
                enemy.solid_blocks = self.solid_blocks
        self.player.help = self.help
        self.player.coins = self.coins
        self.player.enemies = self.enemies
        self.player.spikes = self.spikes
        self.player.exits = self.exits
        self.player.buffs = self.buffs
        self.player.solid_blocks = self.solid_blocks
        self.has_changed = False
        if self.enemies:
            self.music = BATTLE_THEME
        play_music(self.music)

    # функция перезапуска игры
    def restart(self):
        self.player.speed_x = 0
        self.player.speed_y = 0
        self.played = 0
        self.player.hp = self.player.start_hp
        self.player.speed_max = self.player.speed_start
        self.player.jump_power = self.player.jump_power_start
        self.player.money = 0
        self.load_sprites()
        self.current_level = 0
        self.start_next_level()

    # функция загрузки следующего уровня
    def start_next_level(self):
        self.load_sprites()
        self.camera.blocks = self.objects

    def load_map(self):
        map_path = LEVELS[self.current_level]

        with open(map_path, 'r', encoding='UTF-8') as file:
            for y, line in enumerate(file):
                for x, letter in enumerate(line):
                    if letter in MAP_BLOCKS.keys():
                        pos = (x * TILE_SIZE, y * TILE_SIZE)
                        image = MAP_BLOCKS[letter]
                        # установка стартовых координат игрока
                        if letter == 'P':
                            block = self.player
                            block.set_position(*pos)
                        # установка координат для всех "твердых" объектов
                        # TODO перенести класс Spike в Solid_block
                        if letter in SOLID_BLOCKS:
                            block = Solid_Block(*pos, image=image)
                            block.add(self.solid_blocks)
                        # установка координат для всех подбираемых предметов
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
                        # установка координат выхода
                        if letter == 'E':
                            block = Level_end(*pos, image=image)
                            block.add(self.exits)
                        # установка координат противников
                        if letter == 'V':
                            block = Bearded(*pos, image=image)
                            block.add(self.enemies)
                        if letter == 'S':
                            block = Spike(*pos, image=image)
                            block.add(self.spikes)
                        block.add(self.objects)
        self.camera = Camera(self.player, self.objects)
        self.camera.update_borders()

    # обработка всех событий
    # TODO очистить ненужное
    def events(self):
        events = pg.event.get()
        for event in events:
            if event.type == pg.QUIT:
                self.running = False
                self.game_running = False
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_d:
                    self.right = True
                if event.key == pg.K_a:
                    self.left = True
                if event.key == pg.K_SPACE:
                    self.jump = True
                if event.key == pg.K_s:
                    self.fall = True
                if event.key == pg.K_q:
                    self.is_attacking = True
                if event.key == pg.K_r:
                    self.restart()
                if event.key == pg.K_TAB:
                    self.game_running = False
            if event.type == pg.KEYUP:
                if event.key == pg.K_d:
                    self.right = False
                if event.key == pg.K_a:
                    self.left = False
                if event.key == pg.K_SPACE:
                    self.jump = False
                if event.key == pg.K_s:
                    self.fall = False
                if event.key == pg.K_q:
                    self.is_attacking = False

    def update(self):
        # установка FPS
        ms = clock.tick(FPS)
        self.played += ms / 1000
        self.played = round(self.played, 2)

        self.camera.update()

        game_state = self.player.update(self.jump, self.fall, self.left, self.right, self.is_attacking, ms)
        self.help.update()
        self.coins.update()
        self.buffs.update()
        self.enemies.update()
        pg.display.set_caption(f'Player`s money: {self.player.money} HP: {self.player.hp} Played {self.played}')

        if not self.enemies:
            self.music = CALM_THEME
            self.is_playing = False

        if self.music == CALM_THEME and not self.is_playing and not self.has_changed:
            play_music(self.music)
            self.is_playing = True
            self.has_changed = True

        # старт нового уровня
        if game_state == 'end':
            self.current_level += 1
            if self.current_level > 4:
                self.game_running = False
                self.right = self.left = self.jump = self.fall = self.is_attacking = False
            else:
                self.start_next_level()
        if game_state == 'dead':
            self.current_level = 0
            self.start_next_level()

    def render(self):
        self.screen.blit(self.background, (0, 0))
        self.objects.draw(self.screen)
        pg.display.update()

    # фунция запуска игры
    def game_run(self):
        play_music(self.music)
        while self.game_running:
            self.events()
            self.update()
            self.render()

    # фунция запуска приложения
    def global_run(self):
        while self.running:
            self.menu.running = True
            down = self.start_menu()
            self.restart()
            if down == 'all down':
                break
            else:
                self.game_running = True
                self.game_run()
            if self.current_level > 4:
                state = self.end_window.run(self.played, self.player.money, self.player.hp)
                self.current_level = 0
                self.restart()
                if state == 'restart':
                    self.game_running = True
                else:
                    break


if __name__ == '__main__':
    game = Game()
    game.global_run()
    pg.quit()
