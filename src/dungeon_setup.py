'''
Authors: Zach Moore, Travis Conley, Adrian Wyllie, Mitchel Dennis
Purpose: Handles setup actions for the dungeon scene
'''

from action import action
import global_game_states
import time

def dungeon_setup():

    action('FadeOut()')

    # Focus the camera back on John, away from the castle arrest cutscene
    action('SetCameraFocus(Prison.CellDoor)')
    action('SetCameraMode(follow)')
    
    # Adjust player inventory to empty it of any items aquired in the castle
    global_game_states.player_inventory = []

    # Move the player character John to the dungeon and change his clothes to reflect his incarceration
    action('SetClothing(John, Peasant)')
    action('SetPosition(John, Prison.CellDoor.Inside)')

    # Start Background music for dungeon
    action('PlaySound(Explorer)')
