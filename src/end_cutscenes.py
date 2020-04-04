from action import action
import global_game_states
from master_action_controller import check_master_actions
from talk_controller import *

def present_evidence(accused):
    print()

def populate_audience(accused):
    position = 8.9
    for character in global_game_states.execution_characters:
        if not character == accused:
            action('SetPosition('+character+', Gallows.DirtPile)')
            action('WalkToSpot('+character+', 581.6, 3.9,' + str(position) +')')
            action('Face('+character+', Gallows.Altar)')
            position -= 1

def end_cutscene(accused):
    action('CreatePlace(Gallows, Ruins)')
    action('SetPosition(King Phillip, Gallows.Throne)')
    #action('Sit(King Phillip, Gallows.Throne)')
    action('SetPosition(John, Gallows.Throne)')
    action('WalkToSpot(John, 590.1, 5.5, 8.8)')
    action('Face(John, Gallows.Altar)')
    action('SetCameraFocus(John)')
    action('SetCameraMode(follow)')
    action('HideMenu()')
    action('EnableInput()')
    action('SetPosition(Guard Gallant, Gallows.Altar)')
    action('Face(Guard Gallant, Gallows.Exit)awa')
    action('WalkToSpot(Guard Gallant, 586.3, 5.3, 5.6)')
    action('SetPosition(Maester Purcell, 589.9, 5.4, 6.1)')
    action('Face(Maester Purcell, Gallows.Altar)')
    action('SetPosition(' + accused + ', Gallows.Altar)')
    populate_audience(accused)
    action('SetCameraFocus(Gallows.Altar)')
    set_left_right('King Phillip', 'null')
    set_dialog('We are gathered here today to face the person who has killed my dearest Margerie. [Next | Next]', ['Next'], True)
    set_dialog('My trusted advisor, John, has gathered the necessary evidence to bring ' + accused + ' to justice.')
    present_evidence(accused)
    set_dialog('It brings me no joy in sentencing you to death, but you have committed the greatest atrocity to this kingdom.')
    action('HideDialog()')
    action('SetCameraMode(focus)')
    action('SetCameraFocus(' + accused + ')')
    if accused == 'Maester Purcell':
        set_dialog('No...I don\'t even remember who Margerie is. [Next | Next]', ['Next'], True)
        set_dialog('Oh, darn this senile act. It\'s hard to act this stupid anyway.')
        set_dialog('Margerie was going to be the downfall of the kingdom. Her progressive ideas were tearing the land apart.')
        set_dialog('I was doing you all a favor. Get on with it')
        action('HideDialog()')
        action('Attack(Guard Gallant, Maester Purcell, true)')
        action('SetNarration(Accusation Score: 5/5. Nice job! Clue Score: )')
        
        action('HideNarration()')
    # elif accused == 'Tiana':
    
    # elif accused == 'Chamber Maid Scarlet':

    # elif accused == 'Alchemist':
    
    # else:
    #     action('SetPosition('+accused', Gallows.Altar)')
