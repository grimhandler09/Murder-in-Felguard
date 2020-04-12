from action import action
import global_game_states

def populate_audience():
    position = 8.9
    for character in global_game_states.execution_characters:
        if not character == global_game_states.accused:
            action('SetPosition(' + character + ', Gallows.DirtPile)')
            action('WalkToSpot(' + character +', 581.6, 3.9,' + str(position) +')')
            action('Face(' + character + ', Gallows.Altar)')
            position -= 1

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
    action('SetPosition(Guard Gallant, Gallows.Plant)')
    action('WalkToSpot(Guard Gallant, 1182.3, 10.3, 17.1)')
    action('SetExpression(King Phillip, Neutral)')
    #populate_audience()
    action('SetPosition(' + global_game_states.accused + ', Gallows.Altar)')