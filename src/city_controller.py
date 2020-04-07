import time
from action import action
from master_action_controller import check_master_actions, scene_start
from city_setup import city_setup
import global_game_states
from talk_controller import *

def determine_entry():
    if global_game_states.prev_scene == 'scene_two':
        action('Enter(John, City.WestEnd, True)')
    elif global_game_states.prev_scene == 'scene_three':
        action('Enter(John, City.BrownHouseDoor, True)')
    elif global_game_states.prev_scene == 'scene_four':
        action('Enter(John, City.GreenHouseDoor, True)')

def opening_dialog():
    time.sleep(1)
    action('SetNarration(John must explore the city to solve the Queen\'s Murder.)')
    action('ShowNarration()')

def enter_building(door):
    if door == 'City.GreenHouseDoor':
        global_game_states.prev_scene = 'scene_two_and_half'
        global_game_states.current_scene = 'scene_four'
    elif door == 'City.BrownHouseDoor':
        global_game_states.prev_scene = 'scene_two_and_half'
        global_game_states.current_scene = 'scene_three'
    action('Exit(John, ' + door + ', True)')

def city_controller():
    scene_start()
    if global_game_states.first_city_entry:
        city_setup()
        opening_dialog()
        global_game_states.first_city_entry = False
    determine_entry()
    action('FadeIn')
    while global_game_states.current_scene == 'scene_two_and_half':
        received = input()
        if received.startswith('input Enter'):
            door = received[12:]
            enter_building(door)
        else:
            check_master_actions(received)
            
            