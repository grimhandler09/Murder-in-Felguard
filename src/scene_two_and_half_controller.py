import pyautogui
import time
from action import action
from master_action_controller import check_master_actions
import global_game_states
from talk_controller import *

def opening_dialog_two_and_half():
    time.sleep(1)
    action('SetNarration(John must explore the city to solve the Queen\'s Murder.)')
    action('ShowNarration()')
    input()
    action('HideNarration()')
    
def startup():
    action('SetCameraFocus(John)')
    action('SetCameraMode(follow)')
    action('HideMenu()')
    action('EnableInput()')
    opening_dialog_two_and_half()

def enter_building(door):
    if(door == 'input Enter City.GreenHouseDoor'):
        global_game_states.city_position = 'tavern'
        global_game_states.current_scene = 'scene_four'
        global_game_states.in_city = False
    elif(door == 'input Enter City.BrownHouseDoor'):
        global_game_states.city_position = 'alchemist'
        global_game_states.current_scene = 'scene_three'
        global_game_states.in_city = False

def scene_two_and_half_controller(city_position):
    global_game_states.current_scene = 'scene_two_and_half'
    if (global_game_states.city_position == 'dungeon'):
        action('Enter(John, City.WestEnd, True)')  
        startup()
    elif(global_game_states.city_position == 'tavern'):
        action('Enter(John, City.GreenHouseDoor, True')
        startup()
    elif(global_game_states.city_position == 'alchemist'):
        action('Enter(John, City.BrownHouseDoor, True)')
        startup()
    while(global_game_states.in_city):
        received = input()
        if (received.startswith() == 'input Enter'):
            enter_building(received)
        elif (received.statrswith() == 'input Talk'):
            check_master_actions(received)
            
            