import pyautogui
from begin_game import begin_game_setup
from action import action

def talk_action(person):
    action('SetLeft(John)')
    action('SetRight(' + person + ')')
    if person == "Queen":
        command = 'SetDialog(What do you want? [Nothing | Nothing])'
    action(command)
    action('ShowDialog()')

#Send sit command with the place as the parameter
def sit_action(place):
    command = "Sit(John, " + place + ")"
    action(command)

# Respond to input.
def main():
    begin_game_setup()
    while(True):
        received = input()
        if(received == 'input Selected Start'):
            action('FadeOut()')
            action('SetCameraFocus(QueensCastle.DiningTable)')
            action('HideMenu()')
            action('EnableInput()')
            action('SetNarration(Welcome to the Queen\'s birthday bash!)')
            action('ShowNarration()')
        elif(received.startswith('input Sit')):
            received = received.split(' ')
            place = received[len(received) - 1]
            sit_action(place)
        elif(received == 'input Python PythonBox'):
            command = pyautogui.prompt("Command")
            action(command)
        elif(received.startswith('input Talk')):
            received = received.split(' ')
            person = received[len(received) - 1]
            talk_action(person)
        elif(received == 'input Close Narration'):
            action('HideNarration()')
            action('FadeIn()')
            action('SetLeft(King)')
            action('SetRight(Queen)')
            action('SetDialog(Happy Birthday Darling! It is hard to believe that you\'re 45! [Nothing | Next])')
            action('ShowDialog()')
            received = input()
            action('ClearDialog()')
            action('SetDialog(In honor of the momentous occasion I got Glenda the Castle Witch to give you a very special present [Nothing | Next])')
            received = input()
            action('HideDialog()')
            action('WalkTo(CastleWitch, QueensCastle.RightWindow)')
            action('Cast(CastleWitch, Queen)')
            action('EnableEffect(Queen, Heart)')
            action('SetLeft(King)')
            action('SetRight(Queen)')
            action('SetDialog(Let the party commence! [Nothing | Next])')
            action('ShowDialog()')
        elif(received == 'input Selected Nothing'):
            action('HideDialog()')
            action('WalkTo(John, QueensCastle.RightWindow)')
            action('SetCameraFocus(John)')
    
main() #COMMENT OUT WHEN TESTING

'''
Replace the StartExperienceManager batch file with your manager ex:
python ../../../CS499/CS499Camelot/src/example_manager.py
'''