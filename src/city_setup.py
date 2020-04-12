from action import action
import global_game_states

def city_setup():
    
    # Set Day
    action('SetDay()')
    
    # Play Music
    action('PlaySound(Town_Day, City, true)')
    
    # Branching Path Alternative
    #if (not global_game_states.change_clothing):
        #action('SetExpression(Scout Tom, Disgusted)')
        #action('SetExpression(Scout Joanna, Disgusted)')