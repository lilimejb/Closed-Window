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

# путь к папкам с картинками игрока
idle = os.path.join(hero_sprites, 'Idle')
attack = os.path.join(hero_sprites, 'Attack')
death = os.path.join(hero_sprites, 'Death')
jump = os.path.join(hero_sprites, 'Jump')
run = os.path.join(hero_sprites, 'Run')
take_hit = os.path.join(hero_sprites, 'Take_hit')
fall = os.path.join(hero_sprites, 'Fall')

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
                 'take_hit': [os.path.join(take_hit, 'take_hit1.png'),
                              os.path.join(take_hit, 'take_hit2.png'),
                              os.path.join(take_hit, 'take_hit3.png'),
                              os.path.join(take_hit, 'take_hit4.png')],
                 'fall': [os.path.join(fall, 'fall1.png'),
                          os.path.join(fall, 'fall2.png')]}

# ассеты для блоков
# TODO сделать списочным выражением
BLOCK_ASSETS = {'ground': [os.path.join(blocks_sprites, 'ground.png'),
                           os.path.join(blocks_sprites, 'ground-b.png'),
                           os.path.join(blocks_sprites, 'ground-corner.png'),
                           os.path.join(blocks_sprites, 'ground-right-corner.png'),
                           os.path.join(blocks_sprites, 'ground-shadow.png'),
                           os.path.join(blocks_sprites, 'ground-wall.png'),
                           os.path.join(blocks_sprites, 'ground-wall-b.png'),
                           os.path.join(blocks_sprites, 'ground-wood-legs.png')],
                'roof': [os.path.join(blocks_sprites, 'left-roof.png'),
                         os.path.join(blocks_sprites, 'right-roof.png'),
                         os.path.join(blocks_sprites, 'roof.png')],
                'corner': [os.path.join(blocks_sprites, 'left-corner.png'),
                           os.path.join(blocks_sprites, 'right-corner.png')],
                'slope': [os.path.join(blocks_sprites, 'slope.png'),
                          os.path.join(blocks_sprites, 'left-slope.png'),
                          os.path.join(blocks_sprites, 'right-slope.png')],
                'stairs': [os.path.join(blocks_sprites, 'stairs.png'),
                           os.path.join(blocks_sprites, 'stairs-left.png'),
                           os.path.join(blocks_sprites, 'stairs-right.png'),
                           os.path.join(blocks_sprites, 'stairs-mirror.png'),
                           os.path.join(blocks_sprites, 'stairs-mirror-left.png'),
                           os.path.join(blocks_sprites, 'stairs-mirror-right.png'),
                           os.path.join(blocks_sprites, 'stairs-wall.png'),
                           os.path.join(blocks_sprites, 'stairs-wall-left.png'),
                           os.path.join(blocks_sprites, 'stairs-wall-right.png'),
                           os.path.join(blocks_sprites, 'stairs-wall-mirror.png'),
                           os.path.join(blocks_sprites, 'stairs-wall-mirror-left.png'),
                           os.path.join(blocks_sprites, 'stairs-wall-mirror-right.png')],
                'top': [os.path.join(blocks_sprites, 'top-wood.png.png'),
                        os.path.join(blocks_sprites, 'top-left-wood.png'),
                        os.path.join(blocks_sprites, 'top-right-wood.png')],
                'walls': [os.path.join(blocks_sprites, 'wall.png'),
                          os.path.join(blocks_sprites, 'wall-b.png')],
                'windows': [os.path.join(blocks_sprites, 'window.png'),
                            os.path.join(blocks_sprites, 'window-bars.png')]}

# ассеты для задних фонов
BACKGROUND = os.path.join(backgrounds, 'background.bmp')
MENU_BACKGROUND = os.path.join(backgrounds, 'menu_background.bmp')

# ассеты для предметов на уровне
# TODO сделать списочным выражением
BARREL = os.path.join(level_items, 'barrel.png')
CRATE = os.path.join(level_items, 'crate.png')
CRATE_STACK = os.path.join(level_items, 'crate_stack.png')
HOUSES = [os.path.join(level_items, 'house-a.png'),
          os.path.join(level_items, 'house-b.png'),
          os.path.join(level_items, 'house-c.png')]
SIGN = os.path.join(level_items, 'sign.png')
STREET_LAMP = os.path.join(level_items, 'street_lamp.png')
WAGON = os.path.join(level_items, 'wagon.png')
WELL = os.path.join(level_items, 'well.png')

# ассеты для еды
# TODO сделать списочным выражением
FOOD = [os.path.join(heal, 'Apple.png'),
        os.path.join(heal, 'AppleWorm.png'),
        os.path.join(heal, 'Avocado.png'),
        os.path.join(heal, 'Bacon.png'),
        os.path.join(heal, 'Beer.png'),
        os.path.join(heal, 'Boar.png'),
        os.path.join(heal, 'Bread.png'),
        os.path.join(heal, 'Brownie.png'),
        os.path.join(heal, 'Bug.png'),
        os.path.join(heal, 'Cheese.png'),
        os.path.join(heal, 'Cherry.png'),
        os.path.join(heal, 'Chicken.png'),
        os.path.join(heal, 'ChickenLeg.png'),
        os.path.join(heal, 'Cookie.png'),
        os.path.join(heal, 'DragonFruit.png'),
        os.path.join(heal, 'Eggplant.png'),
        os.path.join(heal, 'Eggs.png'),
        os.path.join(heal, 'Fish.png'),
        os.path.join(heal, 'FishFillet.png'),
        os.path.join(heal, 'FishSteak.png'),
        os.path.join(heal, 'Grub.png'),
        os.path.join(heal, 'Grub.png'),
        os.path.join(heal, 'Honey.png'),
        os.path.join(heal, 'Honeycomb.png'),
        os.path.join(heal, 'Jam.png'),
        os.path.join(heal, 'Jerky.png'),
        os.path.join(heal, 'Lemon.png'),
        os.path.join(heal, 'Marmalade.png'),
        os.path.join(heal, 'MelonCantaloupe.png'),
        os.path.join(heal, 'MelonHoneydew.png'),
        os.path.join(heal, 'MelonWater.png'),
        os.path.join(heal, 'Moonshine.png'),
        os.path.join(heal, 'Olive.png'),
        os.path.join(heal, 'Onion.png'),
        os.path.join(heal, 'PepperRed.png'),
        os.path.join(heal, 'Pickle.png'),
        os.path.join(heal, 'PickledEggs.png'),
        os.path.join(heal, 'PieApple.png'),
        os.path.join(heal, 'PieLemon.png'),
        os.path.join(heal, 'PiePumpkin.png'),
        os.path.join(heal, 'Pineapple.png'),
        os.path.join(heal, 'Potato.png'),
        os.path.join(heal, 'PotatoRed.png'),
        os.path.join(heal, 'Pretzel.png'),
        os.path.join(heal, 'Ribs.png'),
        os.path.join(heal, 'Rol.png'),
        os.path.join(heal, 'Saki.png'),
        os.path.join(heal, 'PepperGreen.png'),
        os.path.join(heal, 'Peach.png'),
        os.path.join(heal, 'Pepperoni.png'),
        os.path.join(heal, 'Sardines.png'),
        os.path.join(heal, 'Sashimi.png'),
        os.path.join(heal, 'Sausages.png'),
        os.path.join(heal, 'Shrimp.png'),
        os.path.join(heal, 'Steak.png'),
        os.path.join(heal, 'Stein.png'),
        os.path.join(heal, 'Strawberry.png'),
        os.path.join(heal, 'Sushi.png'),
        os.path.join(heal, 'Tart.png'),
        os.path.join(heal, 'Tomato.png'),
        os.path.join(heal, 'Turnip.png'),
        os.path.join(heal, 'Waffles.png'),
        os.path.join(heal, 'Whiskey.png'),
        os.path.join(heal, 'Wine.png')]

# ассеты для монет
# TODO сделать списочным выражением
COINS = [os.path.join(coins, 'Coin_Blue.png'),
         os.path.join(coins, 'Coin_Gold.png'),
         os.path.join(coins, 'Coin_Green.png'),
         os.path.join(coins, 'Coin_Purple.png'),
         os.path.join(coins, 'Coin_Red.png')]

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

# ассеты для врагов
# TODO сделать списочным выражением
ENEMIES = {'spike': os.path.join(enemies, 'spike.png'),
           'bearded_idle': [os.path.join(bearded_idle, 'idle1.png'),
                            os.path.join(bearded_idle, 'idle2.png'),
                            os.path.join(bearded_idle, 'idle3.png'),
                            os.path.join(bearded_idle, 'idle4.png'),
                            os.path.join(bearded_idle, 'idle5.png')]}

# уровни
# TODO сделать списочным выражением
LEVELS = ['lvl1', 'lvl2']

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
              'V': ENEMIES['bearded_idle'][0]}

SOLID_BLOCKS = 'B'
CONSUMABLES = 'FCHJLR'
