'''
Authors: Zach Moore, Travis Conley, Adrian Wyllie, Mitchel Dennis
Purpose: Handles actions that should be playable regardless of player location
'''
# Import files 
from action import action
from talk_controller import *
import global_game_states
from add_clue import add_clue
from inventory_management import *
import time

'''
Purpose: Performs generic start for most scenes
Inputs: None
Outputs: None
'''
def scene_start():
    action('HideMenu()')
    action('SetCameraFocus(John)')
    action('SetCameraMode(follow)')
    action('EnableInput()')

'''
Purpose: Handles narrations by making it modular for Camelot
Inputs: None
Outputs: None
'''
def midscene_narration(text):
    # Set and show
    action('SetNarration(\"' + text + '\")')
    action('ShowNarration()')

    # Only close with correct input
    received = input()
    while not (received == 'input Close Narration'):
        received = input()
    action('HideNarration()')

'''
Purpose: Displays the clues after pressing E
Inputs: None
Outputs: None
'''
def display_clues_action():
    # If the clue isn't empty
    if not global_game_states.current_clues == []:
        midscene_narration('These are the clues gathered so far')
        action('ClearList()')
        action('HideList()')
        # Add each clue to the Camelot list
        for clue in global_game_states.current_clues:
            action('AddToList(' + clue[0] + ', ' + clue[1] + ')')
        action('ShowList(John)')
    else:
        midscene_narration('Clues will be stored here when they are found.')


'''
Purpose: Handles seating in all chairs
Inputs: Place where John will sit
Outputs: None
'''
def sit_action(place):
    command = "Sit(John, " + place + ")"
    action(command)

'''
Purpose: Handles generic drinking action
Inputs: Item to be drank
Outputs: None
'''
def drink_beverage_action(item):
    action('StopSound()')
    action('HideList()')
    action('PlaySound(Potion)')
    action('Drink(John)')

    # Special case if poison is drank
    if item == 'Poison':
        midscene_narration('What a delicious beverage!')
        action('PlaySound(Danger1)')
        time.sleep(2)
        midscene_narration('John begins to feel a strange sensation just moments after ingesting the thick purple liquid...')
        action('SetCameraFocus(John)')
        action('SetCameraMode(focus)')
        action('Die(John)')
        action('SetCameraFocus(John)')
        action('SetCameraMode(follow)')
        midscene_narration('Accusation Score: 0/5.  The pressure of making a deadly accusation caused John to be parched, and not being the brightest individual, he drank the first thing he could. As it turns out, deadly poison is deadly. The actual perpetrators remain free, however, that is the last thing on John\'s mind.')
        midscene_narration('Thanks for playing, try again and probably don\'t drink the poison!')
        #action('Reset()')
        action('ShowMenu()')
        action('StopSound()')

'''
Purpose: Handles generic actions from other controllers
Inputs: input received from Camelot
Outputs: None
'''
def check_master_actions(received):
    # Sit action
    if received.startswith('input Sit'):
        received = received.split(' ')
        place = received[len(received) - 1]
        sit_action(place)
    
    # Talk action
    elif received.startswith('input Talk'):
        person = received[11:]
        talk_action(person)
    
    # Close Narration
    elif received == 'input Close Narration':
        action('HideNarration()')

    # Close List
    elif received == 'input Close List':
        action('HideList()')

    # Take right-handed item
    elif received.startswith('input TakeRight'):
        item = received[16:]
        take_rightitem_action(item)

    # Take left-handed item
    elif received.startswith('input TakeLeft'):
        item = received[15:]
        take_leftitem_action(item)

    # Stow right-handed item
    elif received.startswith('input StowRight'):
        item = received[16:]
        stow_rightitem_action(item)

    # Stow left-handed item
    elif received.startswith('input StowLeft'):
        item = received[15:]
        stow_leftitem_action(item)

    # Drink action
    elif received.startswith('input Drink'):
        item = received[12:]
        drink_beverage_action(item)

    # View inventory
    elif received == "input Key Inventory":
        action('ClearList()')
        action('HideList()')
        for item in global_game_states.player_inventory:
            action('AddToList(' + item[0] + ', ' + item[1] + ')')
        action('ShowList(John)')

    # Look at clues
    elif received == 'input Key Interact':
        display_clues_action()

    # Menu navigation options
    elif received == 'input Key Pause':
        action('ShowMenu()')
    elif received == 'input Selected Resume':
        action('HideMenu()')
        action('EnableInput()')
    elif received == 'input Selected Credits':
        action('ShowCredits()')
    elif received == 'input Close Credits':
        action('HideCredits()')
    elif received == 'input Selected Quit':
        action('Quit')

    # Accuse someone
    elif received.startswith('input Accuse'):
        # Get accused
        acc_character = received[13:]

        # Ensure they want to accuse
        set_left_right('John', acc_character)
        received = set_dialog('Are you sure you want to accuse ' + acc_character + '? You can only do this once! \\n[Yes | Yes] [No | No]', ['Yes', 'No'], True)
        if received == 'input Selected Yes':
            global_game_states.accused = acc_character
            action('FadeOut()')
        action('HideDialog()')
    
    elif received.startswith('input ClueRead'):
        clue_item = received[15:]
        for clue in global_game_states.current_clues:
            if clue_item == clue[0]:
                midscene_narration(clue[1])
         
