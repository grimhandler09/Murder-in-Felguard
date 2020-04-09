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
    action('CreatePlace(Gallows, Ruins)')
    action('SetPosition(John, Gallows)')
    action('Face(John, Gallows.Altar)')
    action('SetPosition(King Phillip, Gallows.Throne)')
    #action('Sit(King Phillip, Gallows.Throne)')
    action('SetPosition(Guard Gallant, Gallows.Altar)')
    action('Face(Guard Gallant, Gallows.Exit)')
    action('WalkToSpot(Guard Gallant, 583.1, 4.0, 7.3)')
    action('SetExpression(King Phillip, neutral)')
    populate_audience()
    action('SetPosition(' + global_game_states.accused + ', Gallows.Altar)')
    action('WalkToSpot(' + global_game_states.accused + ', 586.0, 5.3, 7.4)')