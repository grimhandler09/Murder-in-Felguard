import pyautogui
import time
from action import action
from master_action_controller import check_master_actions
import global_game_states
from talk_controller import wait_for_response

def startup():
    action('SetCameraFocus(John)')
    action('SetCameraMode(follow)')
    action('HideMenu()')
    action('EnableInput()')

def scene_two_and_half_controller(city_position):
    if (city_position == 'Dungeon'):
        action('FadeIn()')
        action('SetPosition(John, City.WestEnd)')  
        startup()
    elif(city_position == 'Tavern'):
        action('Enter(John, City.GreenHouseDoor)')
        startup()
    elif(city_position == 'Alchemist'):
        action('Enter(John, City.BrownHouseDoor)')
    
    
    
    
