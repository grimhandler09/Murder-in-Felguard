import pyautogui
import time
from action import action
from master_action_controller import check_master_actions
from master_action_controller import add_clue
import global_game_states
from talk_controller import *

def approach(object_of_attention):
    action('WalkTo(John, ' + object_of_attention + ')')
    action('Face(John, ' + object_of_attention + ')')

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
    inventory(global_game_states.chest_inventory, container)
    action('CloseFurniture(John, ' + container + ')')

def use_PrisonDoor_action(door):
    action('OpenFurniture(John, ' + door + ')')
    action('DisableIcon(UsePrisonDoor, ' + door + ')')
    action('EnableIcon(Leave, Door, Prison.Door, Leave, true)')
    action('EnableIcon(Look_up, hand, Prison.Chest, Look through chest, true)')
    action('EnableIcon(Read, research, PrisonLedger, Read, true)')
    action('Face(Guard, John)')
    set_left_right('John', 'Guard')
    scene_two_convo('Guard')
    approach('Guard')
    action('Attack(John, Guard, true)')
    action('Die(Guard)')

def read_book(book):
    set_left_right('John', 'null')
    received = ''
    if book == 'PrisonLedger':
        PrisonLedgerClues = 'Talking to the town Alchemist, Queen\'s Servant, or Grand Maester may yield additional evidence'
        add_clue(PrisonLedgerClues)
        approach(book)
        action('ShowDialog()')
        while received != 'input Selected Exit':
            received = set_dialog('There are several entries that you could read to discover more clues about the Queen\'s Death ' + 
            '[AlchemistInfo | Read about the Alchemist] [Queen\'sServantInfo | Read about the Queen\'s personal servant] [GrandMa' +
            'esterInfo | Read about the Grand Maester] [Exit | Stop reading]', ['AlchemistInfo', 'Queen\'sServantInfo', 'GrandMaesterInfo', 'Exit'])
            if received == 'input Selected AlchemistInfo':
                received = set_dialog('The wine has been sent to the local alchemist for inspection. [Next | Next]')
            elif received == 'input Selected Queen\'sServantInfo':
                received = set_dialog('The Queen\'s servant claims she saw the suspect put something in the Queen\'s drink. [Next | Next]')
            elif received == 'input Selected GrandMaesterInfo':
                received = set_dialog('The Grand Maester claimed that the currently jailed suspect was falsely accused, but provided no evidence to the guards. [Next | Next]')
        action('HideDialog()')
    if book == 'Note_From_King':
        action('ShowDialog()')
        received = set_dialog('I know in my heart that you are innocent, just as I know that my dear Queen Margerie was stolen from me by some dark force.' +
        ' Take this key, escape your cell, and do whatever it takes to uncover the identity of the true murderer. I command it. -King Phillip [Next | Next]')
    action('HideDialog()')

def leave_action(exit_door):
    action('Exit(John, ' + exit_door + ', true)')
    global_game_states.current_scene = 'scene_three'#two_and_half'
    global_game_states.previous_scene = 'scene_two'

def opening_dialog_two():
    action('DisableInput()')
    action('SetCameraFocus(John)')
    action('SetCameraMode(follow)')
    action('SetNarration(John has been arrested by the Queen\'s guards.)')
    action('ShowNarration()')
    input()
    action('HideNarration()')
    action('FadeIn()')
    set_left_right('Guard', 'John')
    set_dialog('I hope you\'re happy. You just killed the most beloved queen this kingdom has ever had. I can\'t even look at you.' +
    ' [Next | What are you talking about] [Next | I didn\'t do anything]', ['Next'], True)

    action('HideDialog()')

def scene_two_controller():
    opening_dialog_two()
    action('EnableInput()')
    while(global_game_states.current_scene == 'scene_two'):
        received = input()
        if received.startswith('input Look_in'):
            received = received.split(' ')
            container = received[2]
            look_inside_nonfurniture_action(container)
        elif ((global_game_states.acquired_CellDoorKey) and (['CellDoorKey', 'CellDoorKey'] in global_game_states.player_inventory)):
            action('EnableIcon(UsePrisonDoor, door, Prison.CellDoor, Open, true)')
            global_game_states.acquired_CellDoorKey = False
        elif received.startswith('input Look_up'):
            received = received.split(' ')
            container = received[2]
            look_inside_furniture_action(container)
        elif received.startswith('input UsePrisonDoor'):
            received = received.split(' ')
            door = received[2]
            use_PrisonDoor_action(door)
        elif received.startswith('input Read'):
            received = received.split(' ')
            book = received[2]
            read_book(book)
        elif received.startswith('input Leave'):
            received = received.split(' ')
            exit_door = received[2]
            leave_action(exit_door)
        else:
            check_master_actions(received)