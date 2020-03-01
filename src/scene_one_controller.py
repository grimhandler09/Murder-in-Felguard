import pyautogui
import time
from action import action
from master_action_controller import check_master_actions
from global_game_states import *

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
    action('SetCameraMode(follow)')

def death_cutscene():
    action('DisableEffect(Queen Margerie)')
    action('DisableIcon(Talk, Queen Margerie)')
    action('SetCameraFocus(QueensCastle.DiningTable)')
    time.sleep(1)
    #action('Pickup(Queen Margerie, QueensCup)')
    action('WalkTo(Queen Margerie, QueensCastle.RightChair)')
    action('WalkToSpot(Queen Margerie, 305.7, 0.1, 0.6)')
    action('Face(Queen Margerie, QueensCastle.DiningTable)')
    action('SetCameraFocus(Queen Margerie)')
    action('SetCameraMode(focus)')
    action('ClearDialog()')
    action('SetLeft(Queen Margerie)')
    action('SetDialog(Thank you all for coming to my birthday bash! [Next | Next])')
    action('ShowDialog()')
    input()
    action('ClearDialog()')
    action('SetLeft(Queen Margerie)')
    action('SetDialog(It so wonderful to see you all here. I look forward to many more glorious years ruling the kingdom! Cheers! [Next | Next])')
    input()
    action('HideDialog()')
    action('Drink(Queen Margerie)')
    action('Die(Queen Margerie)')
    action('SetCameraMode(follow)')
    action('SetCameraFocus(John)')
    action('WalkTo(King Phillip, Queen Margerie)')
    action('Kneel(King Phillip)')


def scene_one_controller():
    #opening_cutscene()
    action('HideMenu()')
    action('SetCameraFocus(John)')
    action('EnableInput()')
    trigger_death = 0
    played = False
    while(True):
        received = input()
        if received == 'input Python PythonBox':
            command = pyautogui.prompt("Command")
            action(command)
        elif received == 'input ReadLedger GuestLedger':
            action('SetNarration(Nobleman Jeremy - Holder of lands to the south. Childhood friend of Queen Margerie...Noblewoman Celcilia - Wife of Nobleman Jeremy)')
            action('ShowNarration()')
            trigger_death += 1
        elif received == 'input ReadInvitation Party Invitation':
            action('SetNarration(You are cordially invited to the Queen\'s Birthday Party. It will truly be one for the ages.)')
            action('ShowNarration()')
        elif received.startswith('input Talk'):
            trigger_death += 1
            check_master_actions(received)
        else:
            check_master_actions(received)
        
        if trigger_death > 2 and not played:
            set_queen_death(True)
            death_cutscene()
            played = True