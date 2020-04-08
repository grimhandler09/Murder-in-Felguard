from begin_game import begin_game_setup
from castle_controller import castle_controller
from dungeon_setup import dungeon_setup
from dungeon_controller import dungeon_controller
from city_controller import city_controller
#from scene_three_controller import scene_three_controller
from tavern_controller import tavern_controller
#from end_cutscenes import end_cutscene
import global_game_states


# Respond to input.
def main():
    begin_game_setup()
    while True:
        received = input()
        if received == 'input Selected Start':
            castle_controller()
            while global_game_states.accused == '':
                if global_game_states.current_scene == 'scene_two':
                    dungeon_setup()
                    dungeon_controller()
                elif global_game_states.current_scene == "scene_two_and_half":
                    city_controller()
                elif global_game_states.current_scene == 'scene_three':
                    print()
                elif global_game_states.current_scene == 'scene_four':
                    tavern_controller()
            #end_cutscene()
    
main() #COMMENT OUT WHEN TESTING

'''
Replace the StartExperienceManager batch file with your manager ex:
python ../../../CS499/CS499Camelot/src/master_game_controller.py
'''