import os

# константы
TILE_SIZE = 64
WIN_SIZE = (16 * TILE_SIZE, 9 * TILE_SIZE)
FPS = 60
GRAVITY = .5

# путь к основным папкам
current_dir = os.path.dirname(__file__)
images = os.path.join(current_dir, 'images')
hero_sprites = os.path.join(images, 'hero_sprites')
blocks_sprites = os.path.join(images, 'blocks_sprites')
backgrounds = os.path.join(images, 'backgrounds')
level_items = os.path.join(images, 'level_items')
consumable = os.path.join(images, 'consumable')
heal = os.path.join(consumable, 'heal')
buffs = os.path.join(consumable, 'buffs')
coins = os.path.join(consumable, 'coins')
enemies = os.path.join(images, 'enemies')
levels = os.path.join('levels')

# путь к папкам с картинками игрока
idle = os.path.join(hero_sprites, 'Idle')
attack = os.path.join(hero_sprites, 'Attack')
death = os.path.join(hero_sprites, 'Death')
jump = os.path.join(hero_sprites, 'Jump')
run = os.path.join(hero_sprites, 'Run')
take_hit = os.path.join(hero_sprites, 'Take_hit')
fall = os.path.join(hero_sprites, 'Fall')

# ассеты музыки
BATTLE_THEME = os.path.join('battle_theme.mp3')
CALM_THEME = os.path.join('calm_theme.mp3')

# ассеты для игрока
# TODO сделать списочным выражением
PLAYER_ASSETS = {'idle': [os.path.join(idle, 'idle1.png'),
                          os.path.join(idle, 'idle2.png'),
                          os.path.join(idle, 'idle3.png'),
                          os.path.join(idle, 'idle4.png'),
                          os.path.join(idle, 'idle5.png'),
                          os.path.join(idle, 'idle6.png'),
                          os.path.join(idle, 'idle7.png'),
                          os.path.join(idle, 'idle8.png')],
                 'attack': [os.path.join(attack, 'attack1.png'),
                            os.path.join(attack, 'attack2.png'),
                            os.path.join(attack, 'attack3.png'),
                            os.path.join(attack, 'attack4.png'),
                            os.path.join(attack, 'attack5.png'),
                            os.path.join(attack, 'attack6.png')],
                 'death': [os.path.join(death, 'death1.png'),
                           os.path.join(death, 'death2.png'),
                           os.path.join(death, 'death3.png'),
                           os.path.join(death, 'death4.png'),
                           os.path.join(death, 'death5.png'),
                           os.path.join(death, 'death6.png')],
                 'jump': [os.path.join(jump, 'jump1.png'),
                          os.path.join(jump, 'jump2.png')],
                 'run': [os.path.join(run, 'run1.png'),
                         os.path.join(run, 'run2.png'),
                         os.path.join(run, 'run3.png'),
                         os.path.join(run, 'run4.png'),
                         os.path.join(run, 'run5.png'),
                         os.path.join(run, 'run6.png'),
                         os.path.join(run, 'run7.png'),
                         os.path.join(run, 'run8.png')],
                 'fall': [os.path.join(fall, 'fall1.png'),
                          os.path.join(fall, 'fall2.png')]}

# ассеты для блоков
# TODO сделать списочным выражением
BLOCK_ASSETS = {'ground': [os.path.join(blocks_sprites, 'ground.png')]}

# ассеты для задних фонов
BACKGROUND = os.path.join(backgrounds, 'background.bmp')
MENU_BACKGROUND = os.path.join(backgrounds, 'menu_background.bmp')

# ассеты для предметов на уровне
WELL = os.path.join(level_items, 'well.png')

# ассеты для еды
FOOD = [os.path.join(heal, 'Apple.png')]

# ассеты для монет
# TODO сделать списочным выражением
COINS = [os.path.join(coins, 'Coin_Blue.png')]

# ассеты для полезных/отрицательных эффектов
# TODO сделать списочным выражением
BUFFS = [os.path.join(buffs, 'Damage_boost.png'),
         os.path.join(buffs, 'Speed_down.png'),
         os.path.join(buffs, 'Speed_boost.png'),
         os.path.join(buffs, 'Jump_boost.png'),
         os.path.join(buffs, 'Jump_down.png')]

# путь к папкам с врагами
bearded = os.path.join(enemies, 'bearded')

# путь к папкам с картинками игрока
bearded_idle = os.path.join(bearded, 'bearded_idle')
bearded_walk = os.path.join(bearded, 'bearded_walk')

# ассеты для врагов
ENEMIES = {'spike': os.path.join(enemies, 'spike.png'),
           'bearded': {'idle': [os.path.join(bearded_idle, f'idle{n + 1}.png') for n in
                                range(len([f for f in os.listdir(bearded_idle)]))],
                       'run': [os.path.join(bearded_walk, f'walk{n + 1}.png') for n in
                               range(len([f for f in os.listdir(bearded_idle)]))]}}

# уровни
LEVELS = [os.path.join(levels, f'lvl{n + 1}') for n in range(len([f for f in os.listdir(levels)]))]

# блоки на карте
MAP_BLOCKS = {'B': BLOCK_ASSETS['ground'][0],
              'C': COINS[0],
              'S': ENEMIES['spike'],
              'F': FOOD[0],
              'E': WELL,
              'P': PLAYER_ASSETS['idle'][0],
              'L': BUFFS[1],
              'H': BUFFS[2],
              'J': BUFFS[3],
              'R': BUFFS[4],
              'V': ENEMIES['bearded']}

SOLID_BLOCKS = 'B'
CONSUMABLES = 'FCHJLR'
