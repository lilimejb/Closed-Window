# подключение библиотек
from player import Player
from utility import *
from enemy import *
from menu import Menu
from main_classes import Camera

clock = pg.time.Clock()


def play_music(music):
    pg.mixer.init()
    pg.mixer.music.load(music)
    pg.mixer.music.play(-1)


# Главный класс игры
class Game:
    def __init__(self):
        pg.init()

        self.running = True
        self.game_running = True

        self.menu = Menu()
        self.player = Player()
        self.camera = Camera()

        self.screen = pg.display.set_mode(WIN_SIZE)
        self.background = pg.image.load(BACKGROUND)
        self.background = pg.transform.scale(self.background, WIN_SIZE)

        self.right = False
        self.left = False
        self.jump = False
        self.fall = False
        self.is_attacking = False

        self.objects = pg.sprite.Group()
        self.coins = pg.sprite.Group()
        self.enemies = pg.sprite.Group()
        self.spikes = pg.sprite.Group()
        self.solid_blocks = pg.sprite.Group()
        self.help = pg.sprite.Group()
        self.exits = pg.sprite.Group()
        self.buffs = pg.sprite.Group()

        self.current_level = 0
        self.load_map()

        self.camera_usage = True

        for enemy in self.enemies:
            if enemy.name == 'bearded':
                enemy.solid_blocks = self.solid_blocks

        # TODO сделать список групп
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

    # функция для запуска меню
    def start_menu(self):
        down = self.menu.run()
        return down

    # функция создающая группы спрайтов и экзэмпляры классов
    # TODO сделать код чище и переписать логику появления игрока
    def load_sprites(self):
        self.objects = pg.sprite.Group()
        self.coins = pg.sprite.Group()
        self.enemies = pg.sprite.Group()
        self.spikes = pg.sprite.Group()
        self.solid_blocks = pg.sprite.Group()
        self.help = pg.sprite.Group()
        self.exits = pg.sprite.Group()
        self.buffs = pg.sprite.Group()
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
        self.player.hp = self.player.start_hp
        self.player.speed_max = self.player.speed_start
        self.player.jump_power = self.player.jump_power_start
        self.player.money = 0
        self.load_sprites()
        self.current_level = 0

    # функция загрузки следующего уровня
    def start_next_level(self):
        self.load_sprites()

    def load_map(self):
        map_path = LEVELS[self.current_level]
        # self.camera_usage = False

        with open(map_path, 'r', encoding='UTF-8') as file:
            for y, line in enumerate(file):
                for x, letter in enumerate(line):
                    # TODO сделать как сказал Лёша
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
                        # TODO перенести выход в Solid_blocks
                        if letter == 'E':
                            block = Level_end(*pos, image=image)
                            block.add(self.exits)
                        # установка координат противников
                        # TODO перенести противников в Solid_blocks
                        if letter == 'V':
                            block = Bearded(*pos, image=image)
                            block.add(self.enemies)
                        if letter == 'S':
                            block = Spike(*pos, image=image)
                            block.add(self.spikes)
                        block.add(self.objects)

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

        # if self.camera_usage:
        #     # изменяем ракурс камеры
        #     self.camera.update(self.player)
        #     # обновляем положение всех спрайтов
        #     for obj in self.objects:
        #         self.camera.apply(obj)

        game_state = self.player.update(self.jump, self.fall, self.left, self.right, self.is_attacking, ms)
        self.help.update()
        self.coins.update()
        self.buffs.update()
        self.enemies.update()
        pg.display.set_caption(f'Player`s money: {self.player.money} HP: {self.player.hp}')

        if not self.enemies:
            self.music = CALM_THEME
            self.is_playing = False

        if self.music == CALM_THEME and not self.is_playing and not self.has_changed:
            play_music(self.music)
            self.is_playing = True
            self.has_changed = True

        # старт нового уровня
        if game_state == 'end':
            self.current_level = (self.current_level + 1) % 5
            self.start_next_level()
        #
        # if game_state == 'game_over':
        #     self.game_running = False

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


if __name__ == '__main__':
    game = Game()
    game.global_run()
    pg.quit()
