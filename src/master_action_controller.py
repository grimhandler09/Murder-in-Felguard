'''
Authors: Zach Moore, Travis Conley, Adrian Wyllie, Mitchel Dennis
Purpose: Handles actions that should be playable regardless of player location
'''

from action import action
from talk_controller import *
import global_game_states
from add_clue import add_clue
import time

def scene_start():
    action('HideMenu()')
    action('SetCameraFocus(John)')
    action('SetCameraMode(follow)')
    action('EnableInput()')

def midscene_narration(text):
    action('SetNarration(\"' + text + '\")')
    action('ShowNarration()')
    received = input()
    while not (received == 'input Close Narration'):
        received = input()
    action('HideNarration()')

def display_clues_action():
    if not global_game_states.current_clues == []:
        midscene_narration('These are the clues gathered so far')
        all_clues = ''
        action('PlaySound(Write)')
        for item in global_game_states.current_clues:
            all_clues = all_clues + '' + item + '\\n'
        set_left_right('John', 'null')
        set_dialog(all_clues + '\\n[Next | Next]', ['Next'], True)
        action('HideDialog()')
    else:
        midscene_narration('Clues will be stored here when they are found.')

def talk_action(person):
    set_left_right('John', person)
    action('ShowDialog()')
    if not global_game_states.queen_death:
        castle_predeath(person)
    elif global_game_states.queen_death and global_game_states.current_scene == 'castle':
        castle_postdeath(person)
    elif global_game_states.current_scene == 'dungeon':
        dungeon_convo(person)
    elif global_game_states.current_scene == 'city':
        city_convo(person)
    elif global_game_states.current_scene == 'alchemist_shop':
        alchemist_shop_convo(person)
    elif global_game_states.current_scene == 'tavern':
        tavern_convo(person)
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
        action('HideList()')
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
       action('HideList()')
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

#Don't read this. Nothing is going on here. Mind your business
def drink_beverage_action(item):
    action('StopSound()')
    action('HideList()')
    action('PlaySound(Potion)')
    action('Drink(John)')
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
        midscene_narration('Accusation Score: 0/5.  The pressure of making a deadly accusation caused John to be parched, and not being the brightest individual, he drank the first thing he could. As it turns out, deadly poison is deadly. The actual perpetrators remain free, however, that is the last thing on John\'s mind. Clue Score: ')
        midscene_narration('Thanks for playing, try again and probably don\'t drink the poison!')
        action('ShowMenu()')

def check_master_actions(received):
    if received.startswith('input Sit'):
        received = received.split(' ')
        place = received[len(received) - 1]
        sit_action(place)
    elif received.startswith('input Talk'):
        person = received[11:]
        talk_action(person)
    elif received == 'input Close Narration':
        action('HideNarration()')
    elif received == 'input Close List':
        action('HideList()')
    elif received.startswith('input TakeRight'):
        item = received[16:]
        take_rightitem_action(item)
    elif received.startswith('input TakeLeft'):
        item = received[15:]
        take_leftitem_action(item)
    elif received.startswith('input StowRight'):
        item = received[16:]
        stow_rightitem_action(item)
    elif received.startswith('input StowLeft'):
        item = received[15:]
        stow_leftitem_action(item)
    elif received.startswith('input Drink'):
        item = received[12:]
        drink_beverage_action(item)
    elif received == "input Key Inventory":
        action('ClearList()')
        action('HideList()')
        for item in global_game_states.player_inventory:
            action('AddToList(' + item[0] + ', ' + item[1] + ')')
        action('ShowList(John)')
    elif received == 'input Key Interact':
        display_clues_action()
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
    elif received.startswith('input Accuse'):
        acc_character = received[13:]
        set_left_right('John', acc_character)
        received = set_dialog('Are you sure you want to accuse ' + acc_character + '? You can only do this once! [Yes | Yes] [No | No]', ['Yes', 'No'], True)
        if received == 'input Selected Yes':
            global_game_states.accused = acc_character
            action('FadeOut()')
        action('HideDialog()')
         
