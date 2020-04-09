import global_game_states

def add_clue(clue):
    if clue not in global_game_states.current_clues:
        global_game_states.current_clues.append(clue)
        if global_game_states.current_scene == 'castle':
            global_game_states.castle_clues.append(clue)
        elif global_game_states.current_scene == 'dungeon':
            global_game_states.dungeon_clues.append(clue)
        elif global_game_states.current_scene == 'city':
            global_game_states.city_clues.append(clue)
        elif global_game_states.current_scene == 'alchemist_shop':
            global_game_states.alchemist_shop_clues.append(clue)
        elif global_game_states.current_scene == 'tavern':
            global_game_states.tavern_clues.append(clue)
