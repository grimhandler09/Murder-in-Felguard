import time
from action import action
from master_action_controller import check_master_actions, scene_start
from city_setup import city_setup
import global_game_states
from talk_controller import *

def enable_accusation():
    for char in global_game_states.character_list:
        action('EnableIcon(Accuse, arrest, ' + char +', Accuse ' + char + ', false)')

def determine_entry():
    if global_game_states.prev_scene == 'dungeon':
        action('Enter(John, City.WestEnd, true)')
    elif global_game_states.prev_scene == 'alchemist_shop':
        action('Enter(John, City.BrownHouseDoor, true)')
    elif global_game_states.prev_scene == 'tavern':
        action('Enter(John, City.GreenHouseDoor, true)')

def opening_dialog():
    time.sleep(1)
    action('SetNarration(John must explore the city to solve the Queen\'s Murder.)')
    action('ShowNarration()')
    input()
    action('SetNarration(\"You can now accuse every person you meet of killing Queen Margerie. Be careful, once you commit to accusing' +
    ' an individual, you can\'t go back!\")')
    action('ShowNarration()')

def enter_building(door):
    if door == 'City.GreenHouseDoor':
        global_game_states.prev_scene = 'city'
        global_game_states.current_scene = 'tavern'
    elif door == 'City.BrownHouseDoor':
        global_game_states.prev_scene = 'city'
        global_game_states.current_scene = 'alchemist_shop'
    action('Exit(John, ' + door + ', true)')

def city_controller():
    scene_start()
    if global_game_states.first_city_entry:
        city_setup()
        enable_accusation()
        opening_dialog()
        global_game_states.first_city_entry = False
    determine_entry()
    action('FadeIn()')
    while global_game_states.current_scene == 'city' and global_game_states.accused == '':
        received = input()
        if received.startswith('input Enter'):
            door = received[12:]
            enter_building(door)
        else:
            check_master_actions(received)
            
            