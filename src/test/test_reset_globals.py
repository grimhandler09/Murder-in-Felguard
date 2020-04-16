import reset_globals
import global_game_states

def test_reset_globals():
    reset_globals.reset_globals()
    # Castle
    assert global_game_states.queen_death == False
    assert global_game_states.castle_key == False
    assert global_game_states.castle_clues == []

    # Dungeon
    assert global_game_states.acquired_CellDoorKey == True
    assert global_game_states.dungeon_guard_lives == False
    assert global_game_states.dirtpile_inventory == [['Note From King', 'Note From King'], ['Cell Door Key', 'Cell Door Key']]
    assert global_game_states.dungeon_chest_inventory == [['Change of Clothes', 'Change of Clothes']]
    assert global_game_states.dungeon_clues == []

    # City
    assert global_game_states.first_city_entry == True
    assert global_game_states.blind_bandit_clue == False
    assert global_game_states.priestess_false_trail == False
    assert global_game_states.city_clues == []

    # Alchemy Shop
    assert global_game_states.first_alchemist_entry == True
    assert global_game_states.found_poison_purchase == False #Evidence for buyer of poison
    assert global_game_states.found_poison == False #Evidence for alchemist
    assert global_game_states.identified_poison == False #used as a step for found_potion
    assert global_game_states.alchemist_shop_clues == []

    # Tavern
    assert global_game_states.first_tavern_entry == True
    assert global_game_states.maester_purcell_senile == False
    assert global_game_states.cecilia_accusations == False
    assert global_game_states.chamber_maid_odd_behaviours == False
    assert global_game_states.tavern_clues == []

    # Ending
    assert global_game_states.execution_characters == ['Noble Jeremy', 'Noble Cecilia', 'Tiana']
    assert global_game_states.selected_clues == []

    # Global
    assert global_game_states.current_scene == 'castle'
    assert global_game_states.prev_scene == ''
    assert global_game_states.accused == ''
    assert global_game_states.player_inventory == [['Party Invitation', 'Party Invitation']]
    assert global_game_states.list_of_inventories == [global_game_states.player_inventory, global_game_states.dungeon_chest_inventory, global_game_states.dirtpile_inventory]
    assert global_game_states.current_clues == []
    assert global_game_states.character_list == ['Guard Gallant', 'King Phillip', 'Witch Carlita', 'Noble Jeremy', 'Noble Cecilia','Merchant Bert', 'Chamber Maid Scarlet', 'Tiana', 
        'Maester Purcell', 'Beggar Adeline', 'Beggar Miles', 'Alchemist Jeremy', 'Scout Joanna', 'Scout Tom', 'Drunk Devon', 
        'Priestess Esmerelda', 'Blind Bandit', 'Gossiping Gail', 'Guard', 'Alchemist Henry'
    ]
    assert global_game_states.wearing_disguise == False