from action import action

def tavern_setup():
    action('CreatePlace("Tavern", Tavern)')
    #Set at Night
    action('SetNight()')
    #Create Characters
    #Main Character(John)
    action('CreateCharacter(John, B)')
    action('SetClothing(John, Peasant)')
    action('SetHairStyle(John, Long)')
    action('SetPosition(John, Tavern.Door)')
    #Witch Carlita
    action('CreateCharacter(Witch Carlita, C)')
    action('SetClothing(Witch Carlita, Witch)')
    action('SetPosition(Witch Carlita, Tavern.BackDoor)')
    action('SetHairStyle(Witch Carlita, Long)')
    action('SetHairColor(Witch Carlita, Gray)')
    #Noble Jeremy
    action('CreateCharacter(Noble Jeremy, F)')
    action('SetClothing(Noble Jeremy, Noble)')
    action('SetPosition(Noble Jeremy, Tavern.StoolFrontRight)')
    action('Sit(Noble Jeremy, Tavern.StoolFrontRight)')
    action('SetHairStyle(Noble Jeremy, Spiky)')
    #Noble Cecilia
    action('CreateCharacter(Noble Cecilia, C)')
    action('SetClothing(Noble Cecilia, Noble)')
    action('SetPosition(Noble Cecilia, Tavern.StoolFrontLeft)')
    action('SetHairStyle(Noble Cecilia, Short)')
    action('Sit(Noble Cecilia, Tavern.StoolFrontLeft)')
    #Merchant Bert
    action('CreateCharacter(Merchant Bert, H)')
    action('SetClothing(Merchant Bert, Merchant)')
    action('SetPosition(Merchant Bert, Tavern.StoolBackLeft)')
    action('SetHairColor(Merchant Bert, Blonde)')
    action('Sit(Merchant Bert, Tavern.StoolBackLeft)')
    #Chamber Maid Scarlet
    action('CreateCharacter(Chamber Maid Scarlet, E)')
    action('SetClothing(Chamber Maid Scarlet, Peasant)')
    action('SetPosition(Chamber Maid Scarlet, Tavern.Fireplace)')
    action('SetHairStyle(Chamber Maid Scarlet, Ponytail)')
    action('SetHairColor(Chamber Maid Scarlet, Brown)')
    action('Face(Chamber Maid Scarlet, Tavern.Fireplace)')
    #Castle Grand Maester Purcell
    action('CreateCharacter(Maester Purcell, H)')
    action('SetClothing(Maester Purcell, Priest)')
    action('SetPosition(Maester Purcell, Tavern.Table)')
    action('SetHairStyle(Maester Purcell, Mage_Full)')
    action('SetHairColor(Maester Purcell, Gray)')
    action('Face(Maester Purcell, Tavern.Table)')
    
     #Enable Icons
    action('EnableIcon(Sit, Chair, Tavern.StoolBackRight, Sit, true)')
    action('EnableIcon(Talk, Talk, Maester Purcell, Talk to Maester Purcell, true)')
    action('EnableIcon(Talk, Talk, Witch Carlita, Talk to Witch Carlita, true)')
    action('EnableIcon(Talk, Talk, Noble Cecilia, Talk to Noble Cecilia, true)')
    action('EnableIcon(Talk, Talk, Merchant Bert, Talk to Merchant Bert, true)')
    action('EnableIcon(Talk, Talk, Chamber Maid Scarlet, Talk to Chamber Maid Scarlet, true)')
    action('EnableIcon(Talk, Talk, Noble Jeremy, Talk to Noble Jeremy, true)')
    action('EnableIcon(Enter, Exit , Tavern.Door, Leave the Tavern, true)')
    
    action('EnableEffect(Tavern.Fireplace, Campfire)')