from begin_game import begin_game_setup
from scene_one_controller import scene_one_controller
from scene_two_setup import scene_two_setup
from scene_two_controller import scene_two_controller
from CitySetup import CitySetup
from scene_two_and_half_controller import scene_two_and_half_controller
#from scene_three_controller import scene_three_controller
from scene_four_controller import scene_four_controller
import global_game_states

# Respond to input.
def main():
    begin_game_setup()
    while(True):
        received = input()
        if(received == 'input Selected Start'):
            scene_one_controller()
            global_game_states.current_scene = "scene_two"
            scene_two_setup()
            scene_two_controller()
            global_game_states.current_scene = "scene_two_and_half"
            CitySetup()
            while(global_game_states.accuse == False):
                if(global_game_states.current_scene == "scene_two_and_half"):
                    scene_two_and_half_controller(global_game_states.city_position)
                #elif (global_game_states.current_scene == "scene_three"):
                    #scene_three_controller()
                elif(global_game_states.current_scene == "scene_four"):
                    scene_four_controller()
    
main() #COMMENT OUT WHEN TESTING

'''
Replace the StartExperienceManager batch file with your manager ex:
python ../../../CS499/CS499Camelot/src/master_game_controller.py
'''