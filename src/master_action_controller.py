from action import action
from talk_controller import *
import global_game_states
from add_clue import add_clue

def scene_start():
    action('HideMenu()')
    action('SetCameraFocus(John)')
    action('SetCameraMode(follow)')
    action('EnableInput()')

def midscene_narration(text):
    action('SetNarration(' + text + ')')
    action('ShowNarration()')
    received = input()
    while not (received == 'input Close Narration'):
        received = input()
    action('HideNarration()')

def display_clues_action():
    if not global_game_states.current_clues == []:
        action('SetNarration(These are the clues gathered so far)')
        action('ShowNarration()')
        input()
        action('HideNarration()')
        for item in global_game_states.current_clues:
            all_clues = '' + item
        set_left_right('John', 'null')
        set_dialog(all_clues + ' [Next | Next]', ['Next'], True)
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
        castle_predeath(person)
    elif global_game_states.queen_death and global_game_states.current_scene == 'castle':
        castle_postdeath(person)
    elif global_game_states.current_scene == 'dungeon':
        dungeon_convo(person)
    elif global_game_states.current_scene == 'city':
        city_convo(person)
    elif global_game_states.current_scene == 'alchemist_shop':
        tavern_convo(person)
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
    elif received == "input Key Inventory":
        action('ClearList()')
        action('HideList()')
        for item in global_game_states.player_inventory:
            action('AddToList(' + item[0] + ', ' + item[1] + ')')
        action('ShowList(John)')
    elif received == 'input Key Interact':
        display_clues_action()
    elif received.startswith('input Accuse'):
        acc_character = received[13:]
        set_left_right('John', acc_character)
        received = set_dialog('Are you sure you want to accuse ' + acc_character + '? You can only do this once! [Yes | Yes] [No | No]', ['Yes', 'No'], True)
        if received == 'input Selected Yes':
            global_game_states.accused = acc_character
            action('FadeOut()')
        action('HideDialog()')
         
