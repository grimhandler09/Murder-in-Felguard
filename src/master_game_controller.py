from begin_game import begin_game_setup
from scene_one_controller import scene_one_controller
from scene_two_setup import scene_two_setup
from scene_two_controller import scene_two_controller
import global_game_states
from end_cutscenes import end_cutscene

# Respond to input.
def main():
    begin_game_setup()
    while(True):
        received = input()
        if(received == 'input Selected Start'):
            #scene_one_controller()
            while(not global_game_states.end_game):
                global_game_states.end_game = True
                if global_game_states.current_scene == 'scene_two':
                    scene_two_setup()
                    scene_two_controller()
                elif global_game_states.current_scene == "scene_two_and_half":
                    print()
                elif global_game_states.current_scene == 'scene_three':
                    print()
                elif global_game_states.current_scene == 'scene_four':
                    print()
            end_cutscene('Maester Purcell')

                
        
    
main() #COMMENT OUT WHEN TESTING

'''
Replace the StartExperienceManager batch file with your manager ex:
python ../../../CS499/CS499Camelot/src/master_game_controller.py
'''