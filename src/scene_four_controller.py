import pyautogui
import time
from action import action
from master_action_controller import check_master_actions
import global_game_states
from talk_controller import *

def scene_four_controller():
    while(global_game_states.current_scene == 'scene_four'):
        received = input()
        if (received.startswith() == 'input Enter'):
            global_game_states.current_scene = 'scene_two_and_half'
        elif (received.startswith() == 'input Talk'):
            check_master_actions(received)