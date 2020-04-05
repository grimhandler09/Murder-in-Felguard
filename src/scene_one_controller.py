import time
from action import action
from master_action_controller import check_master_actions
import global_game_states
from threading import Timer
from talk_controller import *

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
    set_left_right('King Phillip', 'Queen Margerie')
    set_dialog('Happy Birthday Darling! I\'ve invited all of your closest friends and family to celebrate! [Next| Next]', ['Next'], True)
    set_dialog('Enjoy your night Margerie. You\'ve earned it after ruling Felgard faithfully by my side for the last 20 years. [Next | Next]')
    set_dialog('In honor of the momentous occasion I got Carlita the Castle Witch to give you a very special present! [Next | Next]')
    action('HideDialog()')
    action('WalkToSpot(Witch Carlita, 303.1, 0.1, 5.2)')
    action('Cast(Witch Carlita, Queen Margerie)')
    action('EnableEffect(Queen Margerie, Heart)')
    time.sleep(2.5)
    set_left_right('King Phillip', 'Queen Margerie')
    set_dialog('Let the party commence! [Next | Next]', ['Next'], True)
    action('HideDialog()')
    action('SetCameraFocus(John)')
    action('SetCameraMode(follow)')

def death_cutscene():
    action('DisableEffect(Queen Margerie)')
    action('DisableIcon(Talk, Queen Margerie)')
    action('SetCameraFocus(QueensCastle.DiningTable)')
    time.sleep(1)
    action('WalkToSpot(Queen Margerie, 305.7, 0.1, 0.6)')
    action('SetPosition(QueensCup, Queen Margerie)')
    action('Face(Queen Margerie, King Phillip)')
    action('SetCameraFocus(Queen Margerie)')
    action('SetCameraMode(focus)')
    set_left_right('Queen Margerie', 'null')
    set_dialog('Thank you all for coming to my birthday bash! [Next | Next]', ['Next'], True)
    set_dialog('It so wonderful to see you all here. I look forward to many more glorious years ruling the kingdom! Cheers! [Next | Next]', ['Next'])
    action('HideDialog()')
    action('Drink(Queen Margerie)')
    action('SetExpression(Queen Margerie, Disgusted)')
    action('Die(Queen Margerie)')
    action('SetCameraFocus(Chamber Maid Scarlet)')
    set_left_right('Chamber Maid Scarlet', 'null')
    action('SetExpression(Chamber Maid Scarlet, Surprised)')
    set_dialog('Guards! It was the queen\'s aide! I saw him do it! [Next | Next]', ['Next'], True)
    action('HideDialog()')
    action('SetCameraMode(follow)')
    action('SetCameraFocus(John)')
    action('SetNarration(Quick! Gather evidence before the guards arrive!)')
    action('ShowNarration()')
    action('EnableInput()')
    action('WalkToSpot(King Phillip, 307.6, 0.1, -0.9)')
    action('Face(King Phillip, Queen Margerie)')
    action('HideNarration()')
    action('SetExpression(King Phillip, Sad)')
    action('SetExpression(Maester Purcell, Sad)')
    action('SetExpression(Merchant Bert, Sad)')
    action('SetExpression(Noble Cecilia, Sad)')
    action('SetExpression(Noble Jeremy, Sad)')
    action('SetExpression(Witch Carlita, Sad)')
    action('SetExpression(Chamber Maid Scarlet, Sad)')
    action('Kneel(King Phillip)')
    action('WalkToSpot(Maester Purcell, 307.5, 0.1, 2.5)')
    action('Face(Master Purcell, Queen Margerie)')
    arrest_time = Timer(15.0, arrest_cutscene())
    arrest_time.start()

def arrest_cutscene():
    action('HideDialog()')
    action('HideNarration()')
    action('CreateCharacter(Guard Tom, B)')
    action('SetClothing(Guard Tom, HeavyArmour)')
    action('CreateItem(TomSword, Sword)')  
    action('SetPosition(TomSword, Guard Tom)')
    action('SetCameraFocus(QueensCastle.Door)')
    action('WalkTo(Guard Gallant, Queen Margerie)')
    action('Enter(Guard Tom, QueensCastle.Door)')
    action('SetCameraFocus(John)')
    action('SetCameraMode(follow)')
    set_left_right('Guard Tom', 'null')
    set_dialog('Get him! [Next | Next]', ['Next'], True)
    action('HideDialog()')
    global_game_states.end_scene_one = True
    



def scene_one_controller():
    #opening_cutscene()
    action('HideMenu()')
    action('SetCameraFocus(John)')
    action('EnableInput()')
    trigger_death = 0
    while(not global_game_states.end_scene_one):
        received = input()
        if received == 'input ReadLedger GuestLedger':
            action('SetNarration(Nobleman Jeremy - Holder of lands to the south. Childhood friend of Queen Margerie...Noblewoman Celcilia - Wife of Nobleman Jeremy)')
            action('ShowNarration()')
            trigger_death += 1
        elif received == 'input ReadInvitation Party_Invitation':
            action('SetNarration(You are cordially invited to the Queen\'s Birthday Party. It will truly be one for the ages.)')
            action('ShowNarration()')
        else:
            if received.startswith('input Talk'):
                trigger_death += 1
            check_master_actions(received)
        
        if trigger_death > 2 and not global_game_states.queen_death:
                global_game_states.queen_death = True
                death_cutscene()
            