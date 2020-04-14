'''
Authors: Zach Moore and Travis Conley
Purpose: Adds the input clue to the global game state of clues
'''
import global_game_states
from action import action

'''
Purpose: Adds the input clue to the global game state of clues
Inputs: Clue to be added
Outputs: None
'''
def add_clue(clue, clue_item):

    # If clue was already added, do not add again
    if [clue_item, clue] not in global_game_states.current_clues:

        # Append the clue to the clue list
        global_game_states.current_clues.append([clue_item,  clue])
        action('EnableIcon(ClueRead, Book, ' + clue_item + ', Read Clue, true)')
        # Depending on the current scene, add the clue to the appropriate clue scene list
        if global_game_states.current_scene == 'castle':
            global_game_states.castle_clues.append([clue_item, clue])
        elif global_game_states.current_scene == 'dungeon':
            global_game_states.dungeon_clues.append([clue_item, clue])
        elif global_game_states.current_scene == 'city':
            global_game_states.city_clues.append([clue_item, clue])
        elif global_game_states.current_scene == 'alchemist_shop':
            global_game_states.alchemist_shop_clues.append([clue_item, clue])
        elif global_game_states.current_scene == 'tavern':
            global_game_states.tavern_clues.append([clue_item, clue])
