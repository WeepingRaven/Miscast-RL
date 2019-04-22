
"""File with all the constants, for map, characters and their stats

"""

title = "I Cast, Ye Fall - RL"
version = "0.28 - Of Generated Levels"

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
EQUIPMENT_AREA_HEIGHT = 7

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
UI_LEFT_RING_SLOT = (START_INFORMATION_BOX_X + 3, START_INFORMATION_BOX_Y + 8) # LEFT_RING
UI_CLOAK_SLOT = (START_INFORMATION_BOX_X + (12 / 2)-1, START_INFORMATION_BOX_Y + 5) # CLOAK

# Enemies - map settings
MAX_ENEMIES = 2

# Indexes for images

IMAGES_INDEX_WALL = 1
IMAGES_INDEX_FLOOR = 2
IMAGES_INDEX_EMPTY_SPACE = 3

IMAGES_POTION_HP = 13
IMAGES_SCROLL_OF_DEATH = 14

#Player stats

PLAYER_NAME = 'Bupsio'
PLAYER_START_HP = 20

player = {
			'name': PLAYER_NAME,
			'hp': 20

	


		}

# Monster stats
#------------------------------------------
WORM_MAX_HP = 5
WORM_ATTACK = 1
WORM_DEFENCE = 0
WORM_NAME = 'worm'
WORM_SOUND_WALK = 'wiggle'
WORM_MOD_TO_HEARING = -100
WORM_MOD_TO_SEEING = -100
WORM_AI = 'simple_AI'
WORM_SPAWN_RANGE = (2, 2)
WORM_SPAWN_CHANCE = 60
WORM_IMAGE_INDEX = 4
WORM_MOD_TO_BE_SEEN = 0
WORM_MOD_TO_BE_HEARD = 0
#------------------------------------------
ABHORRENT_CREATURE_MAX_HP = 100 # start hp
ABHORRENT_CREATURE_ATTACK = 50
ABHORRENT_CREATURE_DEFENCE = 100
ABHORRENT_CREATURE_NAME = 'abhorrent creature'
ABHORRENT_CREATURE_SOUND_WALK = 'deep low humming'
ABHORRENT_CREATURE_MOD_TO_HEARING = 100
ABHORRENT_CREATURE_MOD_TO_SEEING = -100
ABHORRENT_CREATURE_AI = 'noise_AI'
ABHORRENT_CREATURE_SPAWN_RANGE = (2, 7)
ABHORRENT_CREATURE_SPAWN_CHANCE = 100
ABHORRENT_CREATURE_IMAGE_INDEX = 5
ABHORRENT_CREATURE_MOD_TO_BE_SEEN = 100
ABHORRENT_CREATURE_MOD_TO_BE_HEARD = 0
#------------------------------------------
GOBLIN_MAX_HP = 25
GOBLIN_ATTACK = 10
GOBLIN_DEFENCE = 0 # 10
GOBLIN_NAME = 'goblin'
GOBLIN_SOUND_WALK = 'mumbling and shuffling'
GOBLIN_MOD_TO_HEARING = 0
GOBLIN_MOD_TO_SEEING = 0
GOBLIN_AI = 'noise_AI'
GOBLIN_SPAWN_RANGE = (1, 5)
GOBLIN_SPAWN_CHANCE = 40
GOBLIN_IMAGE_INDEX = 25
GOBLIN_MOD_TO_BE_SEEN = 100
GOBLIN_MOD_TO_BE_HEARD = 0
#------------------------------------------

# move here all the messages

# DESCRIPIONS

player_DESCRIPTION = "What did I do to deserve this?" # Make it vary with mood and health.
abhorrent_creature_DESCRIPTION = "What is this?! Hope it doesn't hear me..."

# modificators:


mods = {
		
		# Keep this low, and add +10, +5 etc, besides mods to be seen
		# Decrease or increase percentage chance
		'mod_to_be_seen': 0,
		'mod_to_seeing': 0,
		'mod_to_be_heard': 0, # negative values decrease chance
		'mod_to_hearing': 0,
		
	   }
