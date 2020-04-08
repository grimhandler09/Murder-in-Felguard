from action import action

def tavern_setup():
    action('CreatePlace(Tavern, Tavern)')
    #Set at Night
    #action('SetNight()')
    #action('SetPosition(John, Tavern.Door)')
    #Witch Carlita
    action('SetPosition(Witch Carlita, Tavern.BackDoor)')
    #Noble Jeremy
    action('SetPosition(Noble Jeremy, Tavern.StoolFrontRight)')
    action('Sit(Noble Jeremy, Tavern.StoolFrontRight)')
    #Noble Cecilia
    action('SetPosition(Noble Cecilia, Tavern.StoolFrontLeft)')
    action('Sit(Noble Cecilia, Tavern.StoolFrontLeft)')
    #Merchant Bert
    action('SetPosition(Merchant Bert, Tavern.StoolBackLeft)')
    action('Sit(Merchant Bert, Tavern.StoolBackLeft)')
    #Chamber Maid Scarlet
    action('SetPosition(Chamber Maid Scarlet, Tavern.Fireplace)')
    action('Face(Chamber Maid Scarlet, Tavern.Fireplace)')
    #Castle Grand Maester Purcell
    action('SetPosition(Maester Purcell, Tavern.Table)')
    action('Face(Maester Purcell, Tavern.Table)')
    #Enable Icons
    action('EnableIcon(Sit, Chair, Tavern.StoolBackRight, Sit, true)')
    action('EnableIcon(Enter, Exit , Tavern.Door, Leave the Tavern, true)')
    
    action('EnableEffect(Tavern.Fireplace, Campfire)')