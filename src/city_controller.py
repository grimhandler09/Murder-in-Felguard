from action import action
from master_action_controller import check_master_actions, scene_start, midscene_narration
from city_setup import city_setup
import global_game_states
from talk_controller import *
from alchemist_shop_setup import alchemist_shop_setup

#Enable John to accuse characters
def enable_accusation():
    for char in global_game_states.character_list:
        action('EnableIcon(Accuse, arrest, ' + char +', Accuse ' + char + ', false)')


# Determine where John enters the city from
def determine_entry():
    # Enter from dungeon (can only happen once)
    if global_game_states.prev_scene == 'dungeon':
        action('StopSound()')
        action('PlaySound(Town_Day)')
        action('Enter(John, City.WestEnd, true)')
    # Enter from Alchemist shop
    elif global_game_states.prev_scene == 'alchemist_shop':
        action('Exit(John, Alch.Door, true)')
        action('StopSound()')
        action('PlaySound(Town_Day)')
        action('Enter(John, City.BrownHouseDoor, true)')
    # Enter from tavern
    elif global_game_states.prev_scene == 'tavern':
        action('Exit(John, Tavern.Door, true)')
        action('StopSound()')
        action('PlaySound(Town_Day)')
        action('Enter(John, City.GreenHouseDoor, true)')

# Give city instructions
def opening_dialog():
    midscene_narration('John must explore the city to solve the Queen\'s Murder.')
    midscene_narration('You can now accuse every person you meet of killing Queen Margerie. Be careful, once you commit to accusing' +
    ' an individual, you can\'t go back!')

# Enter a building
def enter_building(door):
    action('PlaySound(OpenDoor)')
    
    # Enter the tavern
    if door == 'City.GreenHouseDoor':
        global_game_states.prev_scene = 'city'
        global_game_states.current_scene = 'tavern'
    
    # Enter the alchemist shop
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
    
    # Loop while player is in scene
    while global_game_states.current_scene == 'city' and global_game_states.accused == '':
        received = input()
        if received.startswith('input Enter'):
            door = received[12:]
            enter_building(door)
        else:
            check_master_actions(received)
            
            