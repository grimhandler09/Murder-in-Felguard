from begin_game import begin_game_setup
from scene_one_controller import scene_one_controller
from scene_two_setup import scene_two_setup
from scene_two_controller import scene_two_controller

# Respond to input.
def main():
    begin_game_setup()
    while(True):
        received = input()
        if(received == 'input Selected Start'):
            scene_one_controller()
            scene_two_setup()
            scene_two_controller()
        
    
main() #COMMENT OUT WHEN TESTING

'''
Replace the StartExperienceManager batch file with your manager ex:
python ../../../CS499/CS499Camelot/src/master_game_controller.py
'''