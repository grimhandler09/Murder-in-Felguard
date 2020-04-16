import time
from action import action
from master_action_controller import check_master_actions, scene_start
from tavern_setup import tavern_setup
import global_game_states
from talk_controller import *

def tavern_controller():
    scene_start()

    # Start Background noises for tavern
    action('StopSound()')
    action('PlaySound(Tavern)')
    action('PlaySound(Fireplace, Tavern.Fireplace, true)')

    # Begin entry to tavern
    tavern_setup()
    action('SetPosition(John, Tavern.Door)')
    action('FadeIn()')
    
    # Endless loop until John leaves the tavern
    while global_game_states.current_scene == 'tavern' and global_game_states.accused == '':
        received = input()
        if received.startswith('input Enter'):
            global_game_states.current_scene = 'city'
            global_game_states.prev_scene = 'tavern'
        else:
            check_master_actions(received)
