import pyautogui
import time
from action import action
from master_action_controller import check_master_actions
import global_game_states
from global_game_states import dirtpile_inventory
from global_game_states import chest_inventory
from talk_controller import wait_for_response

#chest_inventory = [['Party Invitation', 'Birthday Party Invitation']]
#dirtpile_inventory = [['PlayerSword', 'Sword'], ['CellDoorKey', 'CellKey']]

def stare_at(object_of_attention):
    action('Face(John, ' + object_of_attention + ')')

def inventory(the_list, container):
    action('ClearList()')
    for item in the_list:
        action('AddToList(' + item[0] + ', ' + item[1] + ')')
    action('ShowList(' + container + ')')

def look_inside_nonfurniture_action(container):
    action('WalkTo(John, ' + container + ')')
    action('Face(John, ' + container + ')')
    #action('Kneel(John)')
    inventory(dirtpile_inventory, container)


def look_inside_furniture_action(container):
    action('WalkTo(John, ' + container + ')')
    stare_at(container)
    action('OpenFurniture(John, ' + container + ')')
    inventory(chest_inventory, container)
    action('CloseFurniture(John, ' + container + ')')

def use_door_action(door):
    action('OpenFurniture(John, ' + door + ')')
    action('DisableIcon(Use, ' + door + ')')
    action('EnableIcon(Leave, Door, Prison.Door, Leave, true)')
    action('EnableIcon(Look_up, hand, Prison.Chest, Look through chest, true)')
    action('EnableIcon(Attack, sword, Guard, Strike, false)')

def attack_char_action(target):
    action('WalkTo(John, ' + target + ')')
    action('Face(John, ' + target + ')')
    action('Attack(John, ' + target + ', false)')
    action('Die(' + target + ')')
    action('DisableIcon(Talk, ' + target + ')')
    action('DisableIcon(Attack, ' + target + ')')

def opening_dialog_two():
    action('SetCameraFocus(Prison.CellDoor)')
    time.sleep(1)
    action('SetNarration(John has been arrested by the Queen\'s guards.)')
    action('ShowNarration()')
    input()
    action('HideNarration()')
    action('FadeIn()')
    action('SetLeft(Guard)')
    action('SetRight(John)')
    action('SetDialog(I hope you\'re happy. You just killed the most beloved queen this kingdom has ever had. I can\'t even look at you. [Next | What are you talking about] [Next | I didn\'t do anything])')
    action('ShowDialog()')
    wait_for_response(['Next'])
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
        else:
            check_master_actions(received)