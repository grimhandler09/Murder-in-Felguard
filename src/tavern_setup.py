from action import action
import global_game_states

def tavern_setup():

    if global_game_states.first_tavern_entry:

        # Witch Carlita
        action('SetPosition(Witch Carlita, Tavern.BackDoor)', False)
        action('SetExpression(Witch Carlita, neutral)', False)
        
        # Noble Jeremy
        action('HideFurniture(Tavern.FrontRightStool)')
        action('SetPosition(Noble Jeremy, Tavern.Table.FrontRight)')
        #action('WalkToSpot(Noble Jeremy, 1802.9, 0.1, -1.9)')
        #action('Face(Noble Jeremy, Tavern.Table)')
        #action('Sit(Noble Jeremy, Tavern.FrontRightStool)')
        
        # Noble Cecilia
        action('HideFurniture(Tavern.FrontLeftStool)')
        action('SetPosition(Noble Cecilia, Tavern.Table.FrontLeft)')
        #action('WalkToSpot(Noble Cecilia, 1803.6, 0.1, -5.8)')
        #action('Face(Noble Cecilia, Tavern.Table)')
        #action('Sit(Noble Cecilia, Tavern.FrontLeftStool)')
        
        # Merchant Bert
        action('HideFurniture(Tavern.BackLeftStool)')
        action('SetPosition(Merchant Bert, Tavern.Table.BackLeft)')
        #action('WalkToSpot(Merchant Bert, 1800.0, 0.1, -2.0)')
        #action('Face(Merchant Bert, Tavern.Table)')
        #action('Sit(Merchant Bert, Tavern.BackLeftStool)')
        
        # Chamber Maid Scarlet
        action('SetPosition(Chamber Maid Scarlet, Tavern.Fireplace)')
        action('Face(Chamber Maid Scarlet, Tavern.Fireplace)')
        
        # Castle Grand Maester Purcell
        action('HideFurniture(Tavern.BackRightStool)')
        action('SetPosition(Maester Purcell, Tavern.Table.BackRight)')
        #action('Face(Maester Purcell, Tavern.Table)')
        #action('Sit(Maester Purcell, Tavern.BackRightStool)')
        
        # Queen's Sister
        action('SetPosition(Tiana, Tavern.Bar)')
        action('Face(Tiana, Tavern.Fireplace)')
        
        #Bartender Bill
        action('SetExpression(Bartender Bill, happy)', False)
        
        # Enable Icons
        #action('EnableIcon(Sit, Chair, Tavern.StoolBackRight, Sit, true)')
        action('EnableIcon(Enter, Exit , Tavern.Door, Leave the Tavern, true)', False)
        action('EnableIcon(Talk, Talk , Witch Carlita, Talk to Witch Carlita, true)', False)

        global_game_states.first_tavern_entry = False
    
    #Branching Path
    if not global_game_states.wearing_disguise:
        action('SetNarration(\"The noble are surprised to see you free\"')
        action('ShowNarration()')
        action('SetExpression(Tiana, surprised)', False)
        action('SetExpression(Maester Purcell, surprised)', False)
        action('SetExpression(Chamber Maid Scarlet, surprised)', False)
        action('SetExpression(Merchant Bert, surprised)', False)
        action('SetExpression(Noble Cecilia, surprised)', False)
        action('SetExpression(Noble Jeremy, surprised)', False)
        
    else:
        action('SetExpression(Tiana, sad)', False)
        action('SetExpression(Maester Purcell, surprised)', False)
        action('SetExpression(Chamber Maid Scarlet, scared)', False)
        action('SetExpression(Noble Jeremy, happy)', False)
        action('SetExpression(Noble Cecilia, disgusted)', False)
        action('SetExpression(Merchant Bert, neutral)', False)