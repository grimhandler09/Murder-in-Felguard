import pyautogui

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

def talk_action(person):
    command = 'SetDialog(What do you want? [Nothing | Nothing])'
    action(command)
    action('ShowDialog()')

#Send sit command with the place as the parameter
def sit_action(place):
    command = "Sit(John, " + place + ")"
    action(command)

# Send a command to Camelot.
def action(command):
    print('start ' + command)
    return check_for_success(command)

#Setup beginning of the game
def begin_game_setup():
    # Create Queens Castle
    action('CreatePlace(QueensCastle, DiningRoom)')
    
    #Create Characters
    #Main Character(John)
    action('CreateCharacter(John, B)')
    action('SetClothing(John, Noble)')
    action('SetHairStyle(John, Long)')
    action('SetPosition(John, QueensCastle.BackRightChair)')
    #Queen
    action('CreateCharacter(Queen, A)')
    action('SetClothing(Queen, Queen)')
    action('SetHairStyle(Queen, Long)')
    action('SetPosition(Queen, QueensCastle.RightChair)')
    action('Sit(Queen, QueensCastle.RightChair)')
    #GuardGallant
    action('CreateCharacter(GuardGallant, F)')
    action('SetClothing(GuardGallant, HeavyArmour)')
    action('SetPosition(GuardGallant, QueensCastle.Door)')
    action('CreateItem(GallantSword, Sword)')
    action('SetPosition(GallantSword, GuardGallant)')
    
    #Create Items and position them
    action('CreateItem(QueensCup, Cup)')
    action('SetPosition(QueensCup, QueensCastle.DiningTable.Right)')
    action('CreateItem(JohnsCup, Cup)')
    action('SetPosition(JohnsCup, QueensCastle.DiningTable.BackRight)')
    action('CreateItem(PythonBox, BlueBook)')
    action('SetPosition(PythonBox, QueensCastle.Table)')
    action('ShowMenu()')

    #Enable Icons
    action('EnableIcon(Sit, Chair, QueensCastle.BackRightChair, Sit, true)')
    action('EnableIcon(Python, Drink, PythonBox, Command Camelot, true)')
    action('EnableIcon(Talk, Talk, Queen, Talk to the Queen, true)')
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
        elif(i == 'input Python PythonBox'):
            command = pyautogui.prompt("Command")
            action(command)
        elif(i == 'input Talk Queen'):
            talk_action('Queen')
    
main() #COMMENT OUT WHEN TESTING

'''
Replace the StartExperienceManager batch file with your manager ex:
python ../../../CS499/CS499Camelot/src/example_manager.py
'''