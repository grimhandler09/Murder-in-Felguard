from action import action
from talk_controller import *
import global_game_states
from talk_controller import wait_for_response   

def scene_start():
    action('SetCameraFocus(John)')  
    action('SetCameraMode(follow)')
    action('HideMenu()')
    action('EnableInput()')

def display_clues_action():
    if not global_game_states.current_clues == []:
        action('SetNarration(These are the clues gathered so far)')
        action('ShowNarration()')
        input()
        action('HideNarration()')
        for item in global_game_states.current_clues:
            all_clues = '' + item
        set_left_right('John', 'null')
        action('ShowDialog()')
        set_dialog(all_clues + ' [Next | Next]')
        action('HideDialog()')
    else:
        action('SetNarration(Clues will be stored here when they are found.)')
        action('ShowNarration()')
        input()
        action('HideNarration()')

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

def remove_item(item):
    for inventory in global_game_states.list_of_inventories:
           for individual_item in inventory:
               if individual_item == [item, item] and not (inventory == global_game_states.player_inventory):
                   inventory.remove([item, item])

def take_leftitem_action(item):
    if [item, item] not in global_game_states.player_inventory:
        global_game_states.player_inventory.append([item, item])
        remove_item(item)
        action('Pickup(John, ' + item +')')
    else:
        action('Unpocket(John, ' + item +')')
    action('DisableIcon(TakeLeft, ' + item + ')')
    action('EnableIcon(StowLeft, hand, ' + item + ', Stow, true)')

def take_rightitem_action(item):
    if [item, item] not in global_game_states.player_inventory:
       global_game_states.player_inventory.append([item, item])
       remove_item(item)
       #action('Pickup(John, ' + item +')')
       action('Draw(John, ' + item +')')
    else:
        action('Draw(John, ' + item +')')
    action('DisableIcon(TakeRight, ' + item + ')')
    action('EnableIcon(StowRight, hand, ' + item + ', Stow, true)')

def stow_leftitem_action(item):
    action('Pocket(John, ' + item +')')
    action('DisableIcon(StowLeft, ' + item + ')')
    action('EnableIcon(TakeLeft, hand, ' + item + ', Take, true)')

def stow_rightitem_action(item):
    action('Sheathe(John, ' + item +')')
    action('DisableIcon(StowRight, ' + item + ')')
    action('EnableIcon(TakeRight, hand, ' + item + ', Take, true)')

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
    elif received == "input Key Inventory":
        action('ClearList()')
        for item in global_game_states.player_inventory:
            action('AddToList(' + item[0] + ', ' + item[1] + ')')
        action('ShowList(John)')
    elif received == 'input Key Interact':
        display_clues_action()