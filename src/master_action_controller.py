from action import action
from talk_controller import *
import global_game_states
import pyautogui
from talk_controller import wait_for_response   


def talk_action(person):
    action('SetLeft(John)')
    action('SetRight(' + person + ')')
    action('ShowDialog()')
    if not global_game_states.queen_death:
        scene_one_predeath(person)
    elif global_game_states.queen_death and global_game_states.current_scene == 'scene_one':
        scene_one_postdeath(person)
    elif global_game_states.current_scene == 'scene_two':
        scene_two_convo(person)
    action('HideDialog()')

def take_leftitem_action(item):
    if [item, item] not in global_game_states.player_inventory:
        global_game_states.player_inventory.append([item, item])
        action('Pickup(John, ' + item +')')
    else:
        action('Unpocket(John, ' + item +')')
    action('DisableIcon(TakeLeft, ' + item + ')')
    action('EnableIcon(StowLeft, hand, ' + item + ', Take, true)')

def take_rightitem_action(item):
    if [item, item] not in global_game_states.player_inventory:
       global_game_states.player_inventory.append([item, item])
       #action('Pickup(John, ' + item +')')
       action('Draw(John, ' + item +')')
    else:
        action('Draw(John, ' + item +')')
    action('DisableIcon(TakeRight, ' + item + ')')
    action('EnableIcon(StowRight, hand, ' + item + ', Take, true)')

def stow_leftitem_action(item):
    action('Pocket(John, ' + item +')')
    action('DisableIcon(StowLeft, ' + item + ')')
    action('EnableIcon(TakeLeft, hand, ' + item + ', Take, true)')

def stow_rightitem_action(item):
    action('Sheathe(John, ' + item +')')
    action('DisableIcon(StowRight, ' + item + ')')
    action('EnableIcon(TakeRight, hand, ' + item + ', Take, true)')

def leave_action(exit_door):
    action('Exit(John, ' + exit_door + ', true)')

#Send sit command with the place as the parameter
def sit_action(place):
    command = "Sit(John, " + place + ")"
    action(command)

def check_master_actions(received):
    if received.startswith('input Sit'):
        received = received.split(' ')
        place = received[len(received) - 1]
        sit_action(place)
    elif received.startswith('input Talk'):
        person = received[11:]
        talk_action(person)
    elif received == "input Close Narration":
        action('HideNarration()')
        action('ClearNarration()')
    elif received == "input Close List":
        action("HideList()")
    elif received.startswith('input TakeRight'):
        received = received.split(' ')
        item = received[2]
        take_rightitem_action(item)
    elif received.startswith('input TakeLeft'):
        received = received.split(' ')
        item = received[2]
        take_leftitem_action(item)
    elif received.startswith('input StowRight'):
        received = received.split(' ')
        item = received[2]
        stow_rightitem_action(item)
    elif received.startswith('input StowLeft'):
        received = received.split(' ')
        item = received[2]
        stow_leftitem_action(item)
    elif received.startswith('input Leave'):
        received = received.split(' ')
        exit_door = received[2]
        leave_action(exit_door)
    elif received == "input Key Inventory":
        action('ClearList()')
        for item in global_game_states.player_inventory:
            action('AddToList(' + item[0] + ', ' + item[1] + ')')
        action('ShowList(John)')
    elif received == 'input Key Interact':
        command = pyautogui.prompt("Command")
        action(command)
        
