import global_game_states

def reset_globals():
    # Castle
    global_game_states.queen_death = False
    global_game_states.castle_key = False
    global_game_states.castle_clues = []

    # Dungeon
    global_game_states.acquired_CellDoorKey = True
    global_game_states.dungeon_guard_lives = False
    global_game_states.dirtpile_inventory = [['Note From King', 'Note From King'], ['Cell Door Key', 'Cell Door Key']]
    global_game_states.dungeon_chest_inventory = [['Change of Clothes', 'Change of Clothes']]
    global_game_states.dungeon_clues = []

    # City
    global_game_states.first_city_entry = True
    global_game_states.blind_bandit_clue = False
    global_game_states.priestess_false_trail = False
    global_game_states.city_clues = []

    # Alchemy Shop
    global_game_states.first_alchemist_entry = True
    global_game_states.found_poison_purchase = False #Evidence for buyer of poison
    global_game_states.found_poison = False #Evidence for alchemist
    global_game_states.identified_poison = False #used as a step for found_potion
    global_game_states.alchemist_shop_clues = []

    # Tavern
    global_game_states.first_tavern_entry = True
    global_game_states.maester_purcell_senile = False
    global_game_states.cecilia_accusations = False
    global_game_states.chamber_maid_odd_behaviours = False
    global_game_states.tavern_clues = []

    # Ending
    global_game_states.execution_characters = ['Noble Jeremy', 'Noble Cecilia', 'Tiana']
    global_game_states.selected_clues = []

    # Global
    global_game_states.current_scene = 'castle'
    global_game_states.prev_scene = ''
    global_game_states.accused = ''
    global_game_states.player_inventory = [['Party Invitation', 'Party Invitation']]
    global_game_states.list_of_inventories = [global_game_states.player_inventory, global_game_states.dungeon_chest_inventory, global_game_states.dirtpile_inventory]
    global_game_states.current_clues = []
    global_game_states.character_list = ['Guard Gallant', 'King Phillip', 'Witch Carlita', 'Noble Jeremy', 'Noble Cecilia','Merchant Bert', 'Chamber Maid Scarlet', 'Tiana', 
        'Maester Purcell', 'Beggar Adeline', 'Beggar Miles', 'Alchemist Jeremy', 'Scout Joanna', 'Scout Tom', 'Drunk Devon', 
        'Priestess Esmerelda', 'Blind Bandit', 'Gossiping Gail', 'Guard', 'Alchemist Henry'
    ]