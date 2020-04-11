from action import action
import global_game_states
import time

def dungeon_setup():

    action('FadeOut()')

    # Create the Prison that John will be thrown into

    action('SetCameraFocus(Prison.CellDoor)')
    action('SetCameraMode(follow)')
    
    # Adjust player inventory
    global_game_states.player_inventory = []

    # Move Character(John) to the dungeon
    action('SetClothing(John, Peasant)')
    action('SetPosition(John, Prison.CellDoor.Inside)')

    # Adjust List
    action('AddToList(Note From King, OpenScroll)')
