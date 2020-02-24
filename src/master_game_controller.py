from begin_game import begin_game_setup
from scene_one_controller import scene_one_controller

# Respond to input.
def main():
    begin_game_setup()
    while(True):
        received = input()
        if(received == 'input Selected Start'):
            scene_one_controller()
        
    
main() #COMMENT OUT WHEN TESTING

'''
Replace the StartExperienceManager batch file with your manager ex:
python ../../../CS499/CS499Camelot/src/example_manager.py
'''