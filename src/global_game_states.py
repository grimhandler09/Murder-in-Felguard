#Castle
queen_death = False
scene_one_key = False
#scene_one_clues = []

#Dungeon
acquired_CellDoorKey = True
dungeon_guard_lives = False
dirtpile_inventory = [['Note_From_King', 'Note_From_King'], ['CellDoorKey', 'CellDoorKey']]
dungeon_chest_inventory = [['Change_of_Clothes', 'Change_of_Clothes']]
#scene_two_clues = []

#City
first_city_entry = True
#Alchemy Shop
found_poison_purchase = False #Evidence for buyer of poison
found_poison = False #Evidence for alchemist
identified_poison = False #used as a step for found_potion
#scene_three_clues = []

#Tavern
first_tavern_entry = True
#scene_four_clues = []

#Global
current_scene = 'scene_one'
prev_scene = ''
accused = ''
player_inventory = [['Party_Invitation', 'Party_Invitation']]
list_of_inventories = [player_inventory, dungeon_chest_inventory, dirtpile_inventory]
current_clues = []

