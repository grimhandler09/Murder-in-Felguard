import global_game_states

def add_clue(clue):
    if clue not in global_game_states.current_clues:
        global_game_states.current_clues.append(clue)
