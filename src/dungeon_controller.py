import time
from action import action
from master_action_controller import check_master_actions, scene_start, midscene_narration, add_clue, remove_item
import global_game_states
from talk_controller import *
from add_clue import add_clue

def approach(object_of_attention):
    action('DisableInput()')
    action('WalkTo(John, ' + object_of_attention + ')')
    action('Face(John, ' + object_of_attention + ')')
    action('EnableInput()')

def inventory(the_list, container):
    action('ClearList()')
    for item in the_list:
        action('AddToList(' + item[0] + ', ' + item[1] + ')')
    action('ShowList(' + container + ')')

def look_inside_nonfurniture_action(container):
    approach(container)
    inventory(global_game_states.dirtpile_inventory, container)

def look_inside_furniture_action(container):
    approach(container)
    action('OpenFurniture(John, ' + container + ')')
    inventory(global_game_states.dungeon_chest_inventory, container)

def use_PrisonDoor_action(door):
    action('OpenFurniture(John, ' + door + ')')
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
        approach('Guard Lyra')
        action('Attack(John, Guard Lyra, true)')
        action('Die(Guard Lyra)')
        action('EnableIcon(CheckBody, hand, Guard Lyra, Check, true)')

def read_book(book):
    set_left_right('John', 'null')
    NextDialogOption = ''
    if book == 'Prison Ledger':
        approach(book)
        PrisonLedgerClues = 'Talking to the town Alchemist, Queen\'s Servant, or Grand Maester may yield additional evidence'
        add_clue(PrisonLedgerClues)
        while NextDialogOption != 'input Selected Exit':
            NextDialogOption = set_dialog('There are several entries that you could read to discover more clues about the Queen\'s Death ' + 
            '[AlchemistInfo | Read about the Alchemist] [Queen\'sServantInfo | Read about the Queen\'s personal servant] [GrandMa' +
            'esterInfo | Read about the Grand Maester] [Exit | Stop reading]', ['AlchemistInfo', 'Queen\'sServantInfo', 'GrandMaesterInfo', 'Exit'], True)
            if NextDialogOption == 'input Selected AlchemistInfo':
                NextDialogOption = set_dialog('The wine has been sent to the local alchemist for inspection. [Next | Next]')
            elif NextDialogOption == 'input Selected Queen\'sServantInfo':
                NextDialogOption = set_dialog('The Queen\'s servant claims she saw the suspect put something in the Queen\'s drink. [Next | Next]')
            elif NextDialogOption == 'input Selected GrandMaesterInfo':
                NextDialogOption = set_dialog('The Grand Maester claimed that the currently jailed suspect was falsely accused, but provided no evidence to the Guard Lyras. [Next | Next]')
        if global_game_states.dungeon_guard_lives:
            action('HideDialog()')
            action('Face(Guard Lyra, John)')
            action('Face(John, Guard Lyra)')
            set_left_right('John', 'Guard Lyra')
            set_dialog('If you\'re really trying to help the King, you might wanna actually leave before I throw you back in your cell. Just a thought. [Next | Next]', ['Next'], True)
        action('HideDialog()')
        time.sleep(0.25)
        midscene_narration('Clues regarding the Queen\'s murder such as the one obtained here will be stored and can be accessed from anywhere in the game by pressing \'E\'.')
    if book == 'Note From King':
        action('DisableInput()')
        NextDialogOption = set_dialog('I know in my heart that you are innocent, just as I know that my dear Queen Margerie was stolen from me by some dark force.' +
        ' Take this key, escape your cell, and do whatever it takes to uncover the identity of the true murderer. I command it. -King Phillip [Next | Next]', ['Next'], True)
        action('HideDialog()')
    if book == 'Dire News':
        midscene_narration('This missive describes the untimely and tragic death of the Queen. Penned by Royal Successor Tianna.')
    action('SetCameraFocus(John)')
    action('SetCameraMode(follow)')

def check_body_action(unconscious_body):
    midscene_narration('The Guard Lyra is unconscious but still breathing. She will live.')

def leave_action(exit_door):
    action('Exit(John, ' + exit_door + ', true)')
    global_game_states.current_scene = 'city'
    global_game_states.prev_scene = 'dungeon'
    

def change_clothes_action(attire):
    action('HideList()')
    action('FadeOut')
    action('SetClothing(John, Bandit)')
    action('DisableIcon(Change of Clothes, Change Clothes)')
    action('DisableIcon(Look_Inside_Chest, Prison.Chest)')
    remove_item('Change of Clothes')
    midscene_narration('John has changed into more discrete clothes.')
    action('FadeIn()')

def opening_dialog_two():
    midscene_narration('John has been arrested by the Queen\'s Guard.')
    action('SetCameraFocus(John)')
    action('SetCameraMode(follow)')
    action('FadeIn()')
    set_left_right('Guard Lyra', 'John')
    action('Face(John, Guard Lyra)')
    set_dialog('I hope you\'re happy. You just killed the most beloved queen this kingdom has ever had. I can\'t even look at you.' +
    ' [Next | What are you talking about] [Next | I didn\'t do anything]', ['Next'], True)
    action('HideDialog()')

def dungeon_controller():
    scene_start()
    opening_dialog_two()
    action('EnableInput()')
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
        elif received.startswith('input Read'):
            book = received[11:]
            read_book(book)
            time.sleep(0.25)
            action('EnableInput()')
        elif received.startswith('input Leave'):
            received = received.split(' ')
            exit_door = received[2]
            leave_action(exit_door)
        elif received.startswith('input CheckBody'):
            received = received.split(' ')
            unconscious_body = received[2]
            check_body_action(unconscious_body)
        elif received.startswith('input ChangeClothes'):
            attire = received[20:]
            change_clothes_action(attire)
        else:
            check_master_actions(received)