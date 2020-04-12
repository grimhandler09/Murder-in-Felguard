'''
Authors: Zach Moore, Travis Conley, Adrian Wyllie, Mitchel Dennis
Purpose: The master game controller handles the flow of the player from scene to scene. It integrates many setup files
        and controllers so that the game can be played
'''

# File imports
from action import action
from begin_game import begin_game_setup
from castle_controller import castle_controller
from castle_setup import castle_setup
from dungeon_setup import dungeon_setup
from dungeon_controller import dungeon_controller
from city_controller import city_controller
from alchemist_shop_setup import alchemist_shop_setup
from alchemist_shop_controller import alchemist_shop_controller
from tavern_setup import tavern_setup
from tavern_controller import tavern_controller
import global_game_states
from end_cutscenes import end_cutscene

'''
Purpose: Handles game flow. Integrates rest of program by calling the appropriate scenes when necessary
Inputs: None
Outputs: None
'''
def main():

    # Begin setup of the game
    begin_game_setup()
    castle_setup()
    
    # Show the menu
    action('ShowMenu()')
    # Loop prevents the experience manager from closing and crashing the game
    while True:

        # Get input from Camelot
        received = input()

        # Start the game if the start button is selected
        if received == 'input Selected Start':    

            # Let the player navigate between scenes until someone is accused  
            while global_game_states.accused == '':

                #Navigate to the appropriate scene based on the global game state, then caller the correct setup and controller
                if global_game_states.current_scene == 'castle':
                    castle_controller()
                elif global_game_states.current_scene == 'dungeon':
                    dungeon_setup()
                    dungeon_controller()
                elif global_game_states.current_scene == 'city':
                    city_controller()
                elif global_game_states.current_scene == 'alchemist_shop':
                    alchemist_shop_controller()
                elif global_game_states.current_scene == 'tavern':
                    tavern_controller()

            # Call the end cutscene to end the game
            end_cutscene()
#main() #COMMENT OUT WHEN TESTING

#Replace the StartExperienceManager batch file with your manager ex:
#python ../../../CS499/CS499Camelot/src/master_game_controller.py
