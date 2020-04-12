import global_game_states

def reset_globals():
    # Castle
    global_game_states.queen_death = False
    global_game_states.queen_deathcastle_key = False
    global_game_states.queen_deathcastle_clues = []

    # Dungeon
    global_game_states.queen_deathacquired_CellDoorKey = True
    global_game_states.queen_deathdungeon_guard_lives = False
    global_game_states.queen_deathdirtpile_inventory = [['Note From King', 'Note From King'], ['Cell Door Key', 'Cell Door Key']]
    global_game_states.queen_deathdungeon_chest_inventory = [['Change of Clothes', 'Change of Clothes']]
    global_game_states.queen_deathdungeon_clues = []

    # City
    global_game_states.queen_deathfirst_city_entry = True
    global_game_states.queen_deathblind_bandit_clue = False
    global_game_states.queen_deathpriestess_false_trail = False
    global_game_states.queen_deathcity_clues = []

    # Alchemy Shop
    global_game_states.queen_deathfirst_alchemist_entry = True
    global_game_states.queen_deathfound_poison_purchase = False #Evidence for buyer of poison
    global_game_states.queen_deathfound_poison = False #Evidence for alchemist
    global_game_states.queen_deathidentified_poison = False #used as a step for found_potion
    global_game_states.queen_deathalchemist_shop_clues = []

    # Tavern
    global_game_states.queen_deathfirst_tavern_entry = True
    global_game_states.queen_deathmaester_purcell_senile = False
    global_game_states.queen_deathcecilia_accusations = False
    global_game_states.queen_deathchamber_maid_odd_behaviours = False
    global_game_states.queen_deathtavern_clues = []

    # Ending
    global_game_states.queen_deathexecution_characters = ['Noble Jeremy', 'Noble Cecilia', 'Tiana']

    # Global
    global_game_states.queen_deathcurrent_scene = 'castle'
    global_game_states.queen_deathprev_scene = ''
    global_game_states.queen_deathaccused = ''
    global_game_states.queen_deathplayer_inventory = [['Party Invitation', 'Party Invitation']]
    global_game_states.queen_deathlist_of_inventories = [player_inventory, dungeon_chest_inventory, dirtpile_inventory]
    global_game_states.queen_deathcurrent_clues = []
    global_game_states.queen_deathcharacter_list = ['Guard Gallant', 'King Phillip', 'Witch Carlita', 'Noble Jeremy', 'Noble Cecilia','Merchant Bert', 'Chamber Maid Scarlet', 'Tiana', 
        'Maester Purcell', 'Beggar Adeline', 'Beggar Miles', 'Alchemist Jeremy', 'Scout Joanna', 'Scout Tom', 'Drunk Devon', 
        'Priestess Esmerelda', 'Blind Bandit', 'Gossiping Gail', 'Guard', 'Alchemist Henry'
    ]