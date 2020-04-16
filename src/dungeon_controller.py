'''
Authors: Zach Moore, Travis Conley, Adrian Wyllie, Mitchel Dennis
Purpose: Handles actions that should be playable if the player is located within the dungeon scene
'''

import time
from action import action
from master_action_controller import check_master_actions, scene_start, midscene_narration, add_clue, remove_item, display_clues_action
import global_game_states
from talk_controller import *
from add_clue import add_clue

'''
Purpose: Allows the player controlled character, John, to walk up to and look at any object
Inputs: object_of_attention - the object that the player-controlled character will walk up to
Outputs: None
'''
def approach(object_of_attention):
    action('DisableInput()')
    action('WalkTo(John, ' + object_of_attention + ')')
    action('Face(John, ' + object_of_attention + ')')
    action('EnableInput()')

'''
Purpose: Opens the inventory associated with the object selected by the player
Inputs: the_list - the list of objects that exist within the container the player chooses
        container - the interactable object that has a list of items associated with it
Outputs: None
'''
def inventory(the_list, container):
    action('ClearList()')
    for item in the_list:
        action('AddToList(' + item[0] + ', ' + item[1] + ')')
    action('ShowList(' + container + ')')

'''
Purpose: To access any inventory that is associated with an object that can not be opened - e.g. dirt piles
Inputs: container - the non-furniture, stationary object that will act as an accessible inventory for the player
Outputs: None
'''
def look_inside_nonfurniture_action(container):
    approach(container)
    inventory(global_game_states.dirtpile_inventory, container)

'''
Purpose: To access any inventory that is associated with an object that can be opened - e.g. a chest
Inputs: container - the furniture, openable object the player selects to open
Outputs: None
'''
def look_inside_furniture_action(container):
    approach(container)
    action('OpenFurniture(John, ' + container + ')')
    inventory(global_game_states.dungeon_chest_inventory, container)

'''
Purpose: To facilitate the player's escape from the dungeon cell and to set up the rest of the dungeon scene after the player escapes the cell
Inputs: door - The prison cell door
Outputs: None
'''
def use_PrisonDoor_action(door):
    action('OpenFurniture(John, ' + door + ')')
    action('PlaySound(SecretDoor)')
    action('DisableIcon(UsePrisonDoor, ' + door + ')')
    action('EnableIcon(Leave, Door, Prison.Door, Leave, true)')
    action('EnableIcon(Look_Inside_Chest, hand, Prison.Chest, Look through chest, true)')
    action('EnableIcon(Read, research, Prison Ledger, Read, true)')
    action('EnableIcon(Read, research, Dire News, Read, true)')
    action('EnableIcon(Sit, Chair, Prison.Chair, Sit, true)')
    action('Face(Guard Lyra, John)')
    set_left_right('John', 'Guard Lyra')
    dungeon_convo('Guard Lyra')
    if not global_game_states.dungeon_guard_lives:
        action('SetExpression(Guard Lyra, scared)')
        approach('Guard Lyra')
        action('Attack(John, Guard Lyra, true)')
        action('Die(Guard Lyra)')
        action('EnableIcon(CheckBody, hand, Guard Lyra, Check, true)')

'''
Purpose: To determine which book is selected by the player and provide the appropriate narration and/or dialog required
Inputs: book - the book that the player selects
Outputs: None
'''
def read_book(book):
    set_left_right('John', 'null')
    NextDialogOption = ''
    
    # Dialog for Prison Ledger
    if book == 'Prison Ledger':
        approach(book)
        action('DisableInput()')
        action('PlaySound(Book)')
        while NextDialogOption != 'input Selected Exit':
            NextDialogOption = set_dialog('There are several entries that you could read to discover more clues about the Queen\'s death\\n' + 
            '[AlchemistInfo | Read about the Alchemist] \\n[ChamberMaid | Read about the Chamber Maid, personal servant to the Queen] \\n[GrandMa' +
            'esterInfo | Read about the Grand Maester] \\n[Exit | Stop reading]\\n', ['AlchemistInfo', 'ChamberMaid', 'GrandMaesterInfo', 'Exit'], True)
            if NextDialogOption == 'input Selected AlchemistInfo':
                NextDialogOption = set_dialog('The wine has been sent to the local alchemist for inspection.\\n [Next | Next]')
                add_clue('The Alchemist analyzed the poison used to kill the Queen', 'A Testimonial by the Alchemist')
            elif NextDialogOption == 'input Selected ChamberMaid':
                NextDialogOption = set_dialog('The Chamber Maid claims she saw the suspect put something in the Queen\'s drink.\\n[Next | Next]')
            elif NextDialogOption == 'input Selected GrandMaesterInfo':
                NextDialogOption = set_dialog('The Grand Maester claimed that the currently jailed suspect was falsely accused, but provided no evidence to the guards.\\n [Next | Next]')
                add_clue('The Grand Maester seems to believe something strange is going on', 'Starting Investigations')
        if global_game_states.dungeon_guard_lives:
            action('HideDialog()')
            action('Face(Guard Lyra, John)')
            action('Face(John, Guard Lyra)')
            set_left_right('John', 'Guard Lyra')
            action('SetExpression(Guard Lyra, angry)')
            set_dialog('If you\'re really trying to help the King, you might wanna actually leave before I throw you back in your cell. Just a thought.\\n[Next | Right, I\'ll be quick.]', ['Next'], True)
        action('EnableInput()')
        action('HideDialog()')
        #midscene_narration('Clues regarding the Queen\'s murder such as the one obtained here will be stored and can be accessed from anywhere in the game by pressing \'E\'.')
        
    if book == 'Note From King':
        action('PlaySound(Book)')
        NextDialogOption = set_dialog('I know in my heart that you are innocent, just as I know that my dear Queen Margerie was stolen from me by some dark force.' +
        ' Take this key, escape your cell, and do whatever it takes to uncover the identity of the true murderer. I command it.\\n-King Phillip \\n[Next | Next]', ['Next'], True)
        action('HideDialog()')
    if book == 'Dire News':
        action('PlaySound(Book)')
        midscene_narration('This missive describes the untimely and tragic death of the Queen. Penned by Royal Successor Tianna.')
    # action('SetCameraFocus(John)')
    # action('SetCameraMode(follow)')

'''
Purpose: To enable the dungeon door as an exit from the dungeon to the town
Inputs: exit_door - the door through which John will exit
Outputs: None
'''
def leave_action(exit_door):
    action('Exit(John, ' + exit_door + ', true)')
    global_game_states.current_scene = 'city'
    global_game_states.prev_scene = 'dungeon'
    
'''
Purpose: Change John from his peasant clothes into bandit clothes
Inputs: attire - the clothing object that John will change into
Outputs: None
'''
def change_clothes_action():
    action('HideList()')
    action('FadeOut')
    action('SetClothing(John, Bandit)')
    action('DisableIcon(Change of Clothes, Change Clothes)')
    action('DisableIcon(Look_Inside_Chest, Prison.Chest)')
    remove_item('Change of Clothes')
    global_game_states.wearing_disguise = True
    midscene_narration('John has changed into more discrete clothes.')
    action('FadeIn()')

'''
Purpose: Plays the opening narration, dialog, and camera changes for the dungeon scene.
Inputs: None
Outputs: None
'''
def opening_dialog_two():
    action('SetCameraFocus(John)')
    action('SetCameraMode(follow)')
    action('DisableInput()')
    action('Face(John, Prison.CellDoor)')
    midscene_narration('John has been arrested by the Queen\'s Guard.')
    action('FadeIn()')
    set_left_right('Guard Lyra', 'John')
    set_dialog('I hope you\'re happy. You just killed the most beloved Queen this kingdom has ever had. I can\'t even look at you.\\n' +
    ' [Next | What are you talking about] \\n[Next | I didn\'t do anything]', ['Next'], True)
    action('HideDialog()')
    action('EnableInput()')

'''
Purpose: Primary loop for the dungeon scene, controls which actions the player can take
Inputs: None
Outputs: None
'''
def dungeon_controller():
    scene_start()
    opening_dialog_two()
    while global_game_states.current_scene == 'dungeon':
        received = input()
        if received.startswith('input Look_in_DirtPile'):
            received = received.split(' ')
            container = received[2] 
            look_inside_nonfurniture_action(container)
        elif ((global_game_states.acquired_CellDoorKey) and (['Cell Door Key', 'Cell Door Key'] in global_game_states.player_inventory)):
            action('EnableIcon(UsePrisonDoor, door, Prison.CellDoor, Open, true)')
            global_game_states.acquired_CellDoorKey = False
        elif received.startswith('input Look_Inside_Chest'):
            received = received.split(' ')
            container = received[2]
            look_inside_furniture_action(container)
        elif received.startswith('input UsePrisonDoor'):
            received = received.split(' ')
            door = received[2]
            use_PrisonDoor_action(door)
        elif received.startswith('input Read '):
            book = received[11:]
            read_book(book)
        elif received.startswith('input Leave'):
            received = received.split(' ')
            exit_door = received[2]
            leave_action(exit_door)
        elif received.startswith('input CheckBody'):
            midscene_narration('Guard Lyra is unconscious but still breathing. She will live.')
        elif received.startswith('input ChangeClothes'):
            change_clothes_action()
        else:
            check_master_actions(received)