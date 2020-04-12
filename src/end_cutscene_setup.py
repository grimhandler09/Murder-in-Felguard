'''
Author: Zachary Moore
Purpose: Performs setup for the end cutscene
'''
from action import action
import global_game_states

'''
Purpose: Performs setup for the end cutscene
'''
def end_cutscene_setup():
    # Set Focus on king at throne
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

    # Accused 
    action('SetPosition(' + global_game_states.accused + ', Gallows.Altar)')