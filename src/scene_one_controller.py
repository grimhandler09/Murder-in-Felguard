import pyautogui
import time
from action import action
from master_action_controller import check_master_actions

def opening_cutscene():
    action('FadeOut()')
    action('SetCameraFocus(QueensCastle.DiningTable)')
    action('HideMenu()')
    action('EnableInput()')
    action('SetNarration(Welcome to the Queen\'s birthday bash!)')
    action('ShowNarration()')
    input()
    action('HideNarration()')
    action('FadeIn()')
    action('SetLeft(King Phillip)')
    action('SetRight(Queen Margerie)')
    action('SetDialog(Happy Birthday Darling! I\'ve invited all of your closest friends and family to celebrate! [Next | Next])')
    action('ShowDialog()')
    input()
    action('ClearDialog()')
    action('SetDialog(Enjoy your night Margerie. You\'ve earned it after ruling Felgard faithfully by my side for the last 20 years. [Next | Next])')
    input()
    action('ClearDialog()')
    action('SetDialog(In honor of the momentous occasion I got Carlita the Castle Witch to give you a very special present! [Next | Next])')
    input()
    action('HideDialog()')
    action('WalkToSpot(Witch Carlita, 303.1, 0.1, 5.2)')
    action('Cast(Witch Carlita, Queen Margerie)')
    action('EnableEffect(Queen Margerie, Heart)')
    time.sleep(2.5)
    action('SetLeft(King Phillip)')
    action('SetRight(Queen Margerie)')
    action('SetDialog(Let the party commence! [HideDialog | Next])')
    action('ShowDialog()')
    input()
    action('HideDialog()')
    action('SetCameraFocus(John)')


def scene_one_controller():
    #opening_cutscene()
    action('HideMenu()')
    action('SetCameraFocus(John)')
    action('EnableInput()')
    while(True):
        received = input()
        if(received == 'input Python PythonBox'):
            command = pyautogui.prompt("Command")
            action(command)
        elif(received == 'input ReadLedger GuestLedger'):
            action('SetNarration(Nobleman Jeremy - Holder of lands to the south. Childhood friend of Queen Margerie...Noblewoman Celcilia - Wife of Nobleman Jeremy)')
            action('ShowNarration()')
        else:
            check_master_actions(received)