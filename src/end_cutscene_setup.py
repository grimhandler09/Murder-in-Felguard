'''
Author: Zachary Moore
Purpose: Performs setup for the end cutscene
'''
from action import action
import global_game_states

def enable_use_clues():
    for clue in global_game_states.current_clues:
        action('DisableIcon(ClueRead, ' + clue[0])
        action('EnableIcon(UseClue, openscroll, '  + clue[0] + ', Use Clue, true)')

'''
Purpose: Performs setup for the end cutscene
'''
def end_cutscene_setup():
    action('StopSound()')
    action('PlaySound(Danger3)')
    action('DisableInput()')
    action('SetCameraMode(focus)')
    action('SetCameraFocus(King Phillip)')
    #action('SetPosition(John, Gallows)')
    #action('Face(John, Gallows.Altar)')
    action('SetPosition(King Phillip, Gallows.Throne)')
    #action('Sit(King Phillip, Gallows.Throne)')

    # Guard Gallant
    action('SetPosition(Guard Gallant, Gallows.Plant)')
    action('WalkToSpot(Guard Gallant, 1182.3, 10.3, 17.1)')
    action('SetExpression(King Phillip, Neutral)')

    enable_use_clues()
    # Accused 
    action('SetPosition(' + global_game_states.accused + ', Gallows.Altar)')
    action('SetExpression(' + global_game_states.accused + ', Sad)')