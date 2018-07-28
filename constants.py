
"""File with all the constants, for map, characters and their stats

"""

# SCREEN AND MAP
MAP_WIDTH = 30
MAP_HEIGHT = 30
SCREEN_WIDTH = 672 #480 # 16 * 30        16 * 42 = 672
SCREEN_HEIGHT = 592 #480 # 16 * 30			16 * 37 = 592
TILE_SIZE = 16
FONT_SIZE = 16
# in tiles
SCREEN_SIZE_WIDTH = 42
SCREEN_SIZE_HEIGHT = 37

START_MESSAGE_BOX_X = 0
START_MESSAGE_BOX_Y = 30

# Area with equipment, status, noise etc.
START_INFORMATION_BOX_X = 30
START_INFORMATION_BOX_Y = 0
WIDTH_INFORMATION_BOX = 12
HEIGHT_INFORMATION_BOX = 20

INVENTORY_BOX_X = 30
INVENTORY_BOX_Y = 20

INVENTORY_ITEMS_START_X = 31
INVENTORY_ITEMS_START_Y = 21

INVENTORY_PLACES_WIDTH = 10
INVENTORY_PLACES_HEIGHT = 14

INVENTORY_WIDTH = 12
INVENTORY_HEIGHT = 17

EQUIPMENT_AREA_START_X = 33
EQUIPMENT_AREA_START_Y = 4
EQUIPMENT_AREA_WIDTH = 6
EQUIPMENT_AREA_HEIGHT = 6

HP_START_X = 31
HP_START_Y = 16


UI_HELMET_SLOT = (START_INFORMATION_BOX_X + (12 / 2)-1, START_INFORMATION_BOX_Y + 4) # HELMET
UI_RIGHT_HAND_SLOT = (START_INFORMATION_BOX_X + 3, START_INFORMATION_BOX_Y + 6) # RIGHT_HAND
UI_LEFT_HAND_SLOT = (START_INFORMATION_BOX_X + 7, START_INFORMATION_BOX_Y + 6) # LEFT_HAND
UI_LEFT_FOOT_SLOT = (START_INFORMATION_BOX_X + 4, START_INFORMATION_BOX_Y + 8) # LEFT_FOOT
UI_RIGHT_FOOT_SLOT = (START_INFORMATION_BOX_X + 6, START_INFORMATION_BOX_Y + 8) # RIGHT FOOT
UI_BREASTPLATE_SLOT = (START_INFORMATION_BOX_X + (12 / 2)-1, START_INFORMATION_BOX_Y + 6) # BREASTPLATE
UI_AMULET_SLOT = (START_INFORMATION_BOX_X + 7, START_INFORMATION_BOX_Y + 3) # AMULET
UI_ACCESSORY_SLOT = (START_INFORMATION_BOX_X + 8, START_INFORMATION_BOX_Y + 10) # ACCESSORY
UI_RIGHT_RING_SLOT = (START_INFORMATION_BOX_X + 7, START_INFORMATION_BOX_Y + 8) # RIGHT_RING
UI_LEFT_RING_SLOT = (START_INFORMATION_BOX_X + 3, START_INFORMATION_BOX_Y + 8)# LEFT_RING

# Enemies - map settings
MAX_ENEMIES = 15

# Indexes for images

IMAGES_INDEX_PLAYER = 0
IMAGES_INDEX_WALL = 1
IMAGES_INDEX_FLOOR = 2
IMAGES_INDEX_EMPTY_SPACE = 3
IMAGES_INDEX_WORM = 4
IMAGES_INDEX_ABHORRENT_CREATURE = 5

IMAGES_POTION_HP = 13
IMAGES_SCROLL_OF_DEATH = 14

# Monster stats
PLAYER_NAME = 'pysio'
PLAYER_START_HP = 20
WORM_MAX_HP = 3
ABHORRENT_CREATURE_MAX_HP = 100
# move here all the messages



# DESCRIPIONS

player_DESCRIPTION = "You were just a typical guy, living in house with your cats in a quiet village. You did not have any real ambitions, only dreams and hopes; many of which including that one girl. All has changed now and there is constant noise in your mind, images of The Mage, vivid descriptions of him talking to you not so long ago... 'I must be insane' you keep saying to yourself; but, still going forward."
