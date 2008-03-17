import math

TILE_SZ = [100, 50]
TILE2TILE = 55.901699437
#tile2tile = math.sqrt(pow(TILE_SZ[0],2)+pow(TILE_SZ[1],2))
CHAR_SZ = [50, 50]
CHAR_POS = [0, 0, 0]
SCREEN_SZ = [800, 600]
SCREEN_OR = [SCREEN_SZ[0]/2, 20]
SCENE_SZ = [7, 7]
GAMEZONE_SZ = [800, 400]
HUD_SZ = [800, 200]
HUD_OR = [0, GAMEZONE_SZ[1]]

ANIMATIONS = 5
MAX_FRAMES = 5
ANIM_DELAY = 0.2
SPEED = 55.901699437

TILE_STONE = "tile_stone.png"
PLAYER_SPRITE1 = "black_mage.gif"
PLAYER_SPRITE2 = "black_mage_red.gif"
OBJ_BOOK_SPRITE1 = "book.png"
SIN30R = math.sin(math.radians(30))
COS30R = math.cos(math.radians(30))

HUD_COLOR_BASE = [177, 174, 200]
HUD_COLOR_BORDER1 = [104, 102, 119]
HUD_COLOR_BORDER2 = [138, 136, 160]
HUD_COLOR_BORDER3 = [202, 199, 231]
