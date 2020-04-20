from action import action
import global_game_states

def tavern_setup():

    if global_game_states.first_tavern_entry:

        # Witch Carlita
        action('SetPosition(Witch Carlita, Tavern.BackDoor)')
        action('SetExpression(Witch Carlita, neutral')
        
        # Noble Jeremy
        action('SetPosition(Noble Jeremy, Tavern)')
        action('WalkToSpot(Noble Jeremy, 1802.9, 0.1, -1.9)')
        action('Face(Noble Jeremy, Tavern.Table)')
        #action('Sit(Noble Jeremy, Tavern.StoolFrontRight)')
        
        # Noble Cecilia
        action('SetPosition(Noble Cecilia, Tavern)')
        action('WalkToSpot(Noble Cecilia, 1803.6, 0.1, -5.8)')
        action('Face(Noble Cecilia, Tavern.Table)')
        #action('Sit(Noble Cecilia, Tavern.StoolFrontLeft)')
        
        # Merchant Bert
        action('SetPosition(Merchant Bert, Tavern)')
        action('WalkToSpot(Merchant Bert, 1800.0, 0.1, -2.0)')
        action('Face(Merchant Bert, Tavern.Table)')
        #action('Sit(Merchant Bert, Tavern.StoolBackLeft)')
        
        # Chamber Maid Scarlet
        action('SetPosition(Chamber Maid Scarlet, Tavern.Fireplace)')
        action('Face(Chamber Maid Scarlet, Tavern.Fireplace)')
        
        # Castle Grand Maester Purcell
        action('SetPosition(Maester Purcell, Tavern.Table)')
        action('Face(Maester Purcell, Tavern.Table)')
        
        # Queen's Sister
        action('SetPosition(Tiana, Tavern.Bar)')
        action('Face(Tiana, Tavern.Fireplace)')
        
        #Bartender Bill
        action('SetExpression(Bartender Bill, happy)')
        
        # Enable Icons
        #action('EnableIcon(Sit, Chair, Tavern.StoolBackRight, Sit, true)')
        action('EnableIcon(Enter, Exit , Tavern.Door, Leave the Tavern, true)')
        action('EnableIcon(Talk, Talk , Witch Carlita, Talk to Witch Carlita, true)')

        global_game_states.first_tavern_entry = False
    
    #Branching Path
    if not global_game_states.wearing_disguise:
        action('SetExpression(Tiana, scared)')
        action('SetExpression(Maester Purcell, scared)')
        action('SetExpression(Chamber Maid Scarlet, scared)')
        action('SetExpression(Merchant Bert, scared)')
        action('SetExpression(Noble Cecilia, scared)')
        action('SetExpression(Noble Jeremy, scared)')
        action('SetExpression(Witch Carlita, scared)')
        
    else:
        action('SetExpression(Tiana, sad)')
        action('SetExpression(Maester Purcell, surprised)')
        action('SetExpression(Chamber Maid Scarlet, scared)')
        action('SetExpression(Noble Jeremy, happy)')
        action('SetExpression(Noble Cecilia, disgusted)')
        action('SetExpression(Merchant Bert, neutral)')
        action('SetExpression(Witch Carlita, angry)')