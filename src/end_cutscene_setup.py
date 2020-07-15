'''
Author: Zachary Moore
Purpose: Performs setup for the end cutscene
'''
from action import action
import global_game_states

def enable_use_clues():
    for clue in global_game_states.current_clues:
        action('EnableIcon(UseClue, openscroll, '  + clue[0] + ', Use Clue, false)')

'''
Purpose: Performs setup for the end cutscene
'''
def end_cutscene_setup():
    action('StopSound()')
    action('PlaySound(Danger3)')
    action('DisableInput()', False)
    action('SetCameraMode(focus)', False)
    action('SetCameraFocus(King Phillip)', False)
    action('SetPosition(King Phillip, Gallows.Throne)', False)

    # Guard Gallant
    action('SetPosition(Guard Gallant, Gallows.Plant)', False)
    #action('WalkToSpot(Guard Gallant, 1182.3, 10.3, 17.1)')
    action('SetExpression(King Phillip, Neutral)', False)

    enable_use_clues()
    # Accused 
    action('SetPosition(' + global_game_states.accused + ', Gallows.Altar)', False)
    action('SetExpression(' + global_game_states.accused + ', Sad)', False)