import pyautogui
import time
from action import action
from master_action_controller import check_master_actions
import global_game_states
from talk_controller import *


chest_inventory = [['Party Invitation', 'Birthday Party Invitation']]
dirtpile_inventory = [['PlayerSword', 'Sword'], ['CellDoorKey', 'CellKey']]

def stare_at(object_of_attention):
    command = 'Face(John, ' + object_of_attention + ')'
    action(command)
    #command = 'LookAt(John)'
    #action(command)

def inventory(the_list, container):
    action('ClearList()')
    for item in the_list:
        action('AddToList(' + item[0] + ', ' + item[1] + ')')
    action('ShowList(' + container + ')')

def look_inside_nonfurniture_action(container):
    command = 'WalkTo(John, ' + container + ')'
    action(command)
    stare_at(container)
    #action('Kneel(John)')
    inventory(dirtpile_inventory, container)


def look_inside_furniture_action(container):
    command = 'WalkTo(John, ' + container + ')'
    action(command)
    stare_at(container)
    command = 'OpenFurniture(John, ' + container + ')'
    action(command)
    inventory(chest_inventory, container)
    command = 'CloseFurniture(John, ' + container + ')'
    action(command)

def use_door_action(door):
    command = 'OpenFurniture(John, ' + door + ')'
    action(command)

def attack_char_action(target):
    command = 'WalkTo(John, ' + target + ')'
    action(command)
    stare_at(target)
    command = 'Attack(John, ' + target + ', false)'
    action(command)
    command = 'Die(' + target + ')'
    action(command)
    action('DisableIcon(Talk, ' + target + ')')
    action('DisableIcon(Attack, ' + target + ')')

def take_leftitem_action(item):
    command = 'Unpocket(John, ' + item +')'
    action(command)
    if ['CellDoorKey', 'CellKey'] not in global_game_states.player_inventory:
        global_game_states.player_inventory.append(['CellDoorKey', 'CellKey'])
    action('DisableIcon(Take, ' + item + ')')
    action('EnableIcon(Stow, hand, ' + item + ', Take, true)')

def take_rightitem_action(item):
    command = 'Draw(John, ' + item +')'
    action(command)
    if ['PlayerSword', 'Sword'] not in global_game_states.player_inventory:
       global_game_states.player_inventory.append(['PlayerSword', 'Sword'])
    action('DisableIcon(Take, ' + item + ')')
    action('EnableIcon(Stow, hand, ' + item + ', Take, true)')

def stow_leftitem_action(item):
    command = 'Pocket(John, ' + item +')'
    action(command)
    action('DisableIcon(Stow, ' + item + ')')
    action('EnableIcon(Take, hand, ' + item + ', Take, true)')

def stow_rightitem_action(item):
    command = 'Sheathe(John, ' + item +')'
    action(command)
    action('DisableIcon(Stow, ' + item + ')')
    action('EnableIcon(Take, hand, ' + item + ', Take, true)')

def leave_prison_action(exit_door):
    command = 'Exit(John, ' + exit_door + ', true)'
    action(command)

def opening_dialog_two():
    time.sleep(1)
    action('SetNarration(John has been arrested by the Queen\'s guards.)')
    action('ShowNarration()')
    input()
    action('HideNarration()')
    #action('FadeIn()')
    
    set_left_right('Guard', 'John')
    set_dialog('I hope you\'re happy. You just killed the most beloved queen this kingdom has ever had. I can\'t even look at you. [Next | What are you talking about] [Next | I didn\'t do anything]', ['Next'], True)
    action('HideDialog()')

def scene_two_controller():
    opening_dialog_two()
    action('SetCameraFocus(John)')
    action('SetCameraMode(follow)')
    action('EnableInput()')
    while(True):
        received = input()
        if received.startswith('input Look_in'):
            received = received.split(' ')
            container = received[2]
            look_inside_nonfurniture_action(container)
        elif received.startswith('input Look_up'):
            received = received.split(' ')
            container = received[2]
            look_inside_furniture_action(container)
        elif received.startswith('input Use'):
            received = received.split(' ')
            door = received[2]
            use_door_action(door)
        elif received.startswith('input Attack'):
            received = received.split(' ')
            target = received[2]
            attack_char_action(target)
        elif received.startswith('input Take'):
            received = received.split(' ')
            item = received[2]
            if item == 'PlayerSword':
                take_rightitem_action(item)
            else:
                take_leftitem_action(item)
        elif received.startswith('input Stow'):
            received = received.split(' ')
            item = received[2]
            if item == 'PlayerSword':
                stow_rightitem_action(item)
            else:
                stow_leftitem_action(item)
        elif received.startswith('input Leave'):
            received = received.split(' ')
            exit_door = received[2]
            leave_prison_action(exit_door)
        else:
            check_master_actions(received)