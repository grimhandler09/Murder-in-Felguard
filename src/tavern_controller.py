import time
from action import action
from master_action_controller import check_master_actions, scene_start
from tavern_setup import tavern_setup
import global_game_states
from talk_controller import *

def tavern_controller():
    scene_start()
    if global_game_states.first_tavern_entry:
        tavern_setup()
        global_game_states.first_tavern_entry = False
    while(global_game_states.current_scene == 'scene_four'):
        received = input()
        if (received.startswith() == 'input Enter'):
            global_game_states.current_scene = 'scene_two_and_half'
            global_game_states.prev_scene = 'scene_one'
        elif (received.startswith() == 'input Talk'):
            check_master_actions(received)