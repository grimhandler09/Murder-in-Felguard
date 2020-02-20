#Interprets response from Camelot when sending command to it
def check_for_success(command):
    while(True):
        i = input()
        if(i == 'succeeded ' + command):
            return True
        elif(i == 'failed ' + command):
            return False
        elif(i.startswith('error')):
            return False

#Send sit command with the place as the parameter
def sit_action(place):
    command = "Sit(John, " + place + ")"
    print('start ' + command)
    check_for_success(command)

# Send a command to Camelot.
def action(command):
    print('start ' + command)
    return check_for_success(command)

#Setup beginning of the game
def begin_game_setup():
    # Create Queens Castle
    action('CreatePlace(QueensCastle, DiningRoom)')
    
    #Create Characters
    action('CreateCharacter(John, B)')
    action('SetClothing(John, Noble)')
    action('SetHairStyle(John, Long)')
    action('SetPosition(John, QueensCastle.BackRightChair)')
    action('CreateCharacter(Queen, A)')
    action('SetClothing(Queen, Queen)')
    action('SetHairStyle(Queen, Long)')
    action('SetPosition(Queen, QueensCastle.RightChair)')
    action('Sit(Queen, QueensCastle.RightChair)')
    
    #Create Items and position them
    action('CreateItem(QueensCup, Cup)')
    action('SetPosition(QueensCup, QueensCastle.DiningTable.Right)')
    action('CreateItem(JohnsCup, Cup)')
    action('SetPosition(JohnsCup, QueensCastle.DiningTable.BackRight)')
    action('ShowMenu()')

    #Enable Icons
    action('EnableIcon(Sit, Chair, QueensCastle.BackRightChair, Sit, true)')
# Respond to input.
def main():
    begin_game_setup()
    while(True):
        i = input()
        if(i == 'input Selected Start'):
            action('SetCameraFocus(John)')
            action('HideMenu()')
            action('EnableInput()')
        elif(i == 'input Open_Door BobsHouse.Door'):
            action('SetNarration(The door is locked!)')
            action('ShowNarration()')
        elif(i == 'input Close Narration'):
            action('HideNarration()')
        elif(i == 'input Sit QueensCastle.BackRightChair'):
            sit_action('QueensCastle.BackRightChair')
    
main() #COMMENT OUT WHEN TESTING

'''
Replace the StartExperienceManager batch file with your manager ex:
python ../../../CS499/CS499Camelot/src/example_manager.py
'''