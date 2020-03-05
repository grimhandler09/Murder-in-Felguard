import time
from action import action
from master_action_controller import check_master_actions
import global_game_states
from threading import Timer
from talk_controller import wait_for_response

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
    wait_for_response(['Next'])
    action('ClearDialog()')
    action('SetDialog(Enjoy your night Margerie. You\'ve earned it after ruling Felgard faithfully by my side for the last 20 years. [Next | Next])')
    wait_for_response(['Next'])
    action('ClearDialog()')
    action('SetDialog(In honor of the momentous occasion I got Carlita the Castle Witch to give you a very special present! [Next | Next])')
    wait_for_response(['Next'])
    action('HideDialog()')
    action('WalkToSpot(Witch Carlita, 303.1, 0.1, 5.2)')
    action('Cast(Witch Carlita, Queen Margerie)')
    action('EnableEffect(Queen Margerie, Heart)')
    time.sleep(2.5)
    action('SetLeft(King Phillip)')
    action('SetRight(Queen Margerie)')
    action('SetDialog(Let the party commence! [Next | Next])')
    action('ShowDialog()')
    wait_for_response(['Next'])
    action('HideDialog()')
    action('SetCameraFocus(John)')
    action('SetCameraMode(follow)')

def death_cutscene():
    action('DisableEffect(Queen Margerie)')
    action('DisableIcon(Talk, Queen Margerie)')
    action('SetCameraFocus(QueensCastle.DiningTable)')
    time.sleep(1)
    #action('Pickup(Queen Margerie, QueensCup)') #Pickup cup when fixed
    action('WalkTo(Queen Margerie, QueensCastle.RightChair)')
    action('WalkToSpot(Queen Margerie, 305.7, 0.1, 0.6)')
    action('Face(Queen Margerie, QueensCastle.DiningTable)')
    action('SetCameraFocus(Queen Margerie)')
    action('SetCameraMode(focus)')
    action('ClearDialog()')
    action('SetLeft(Queen Margerie)')
    action('SetRight(null)')
    action('SetDialog(Thank you all for coming to my birthday bash! [Next | Next])')
    action('ShowDialog()')
    wait_for_response(['Next'])
    action('ClearDialog()')
    action('SetDialog(It so wonderful to see you all here. I look forward to many more glorious years ruling the kingdom! Cheers! [Next | Next])')
    wait_for_response(['Next'])
    action('HideDialog()')
    action('Drink(Queen Margerie)')
    action('SetExpression(Queen Margerie, Disgusted)')
    action('Die(Queen Margerie)')
    action('SetCameraFocus(Chamber Maid Scarlet)')
    action('ClearDialog()')
    action('SetLeft(Chamber Maid Scarlet)')
    action('SetRight(null)')
    action('SetExpression(Chamber Maid Scarlet, Surprised)')
    action('SetDialog(Guards! It was the queen\'s aide! I saw him do it! [Next | Next])')
    action('ShowDialog()')
    wait_for_response(['Next'])
    action('HideDialog()')
    action('SetCameraMode(follow)')
    action('SetCameraFocus(John)')
    action('SetNarration(Quick! Gather evidence before the guards arrive!)')
    action('ShowNarration()')
    action('EnableInput()')
    action('WalkToSpot(King Phillip, 307.6, 0.1, -0.9)')
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
    arrest_time = Timer(15.0, arrest_cutscene())
    arrest_time.start()

def arrest_cutscene():
    action('HideDialog()')
    action('HideNarration()')
    action('CreateCharacter(Guard Tom, B)')
    action('CreateCharacter(Guard Lance, B)')
    action('CreateCharacter(Guard Jim, B)')
    action('SetClothing(Guard Tom, HeavyArmour)')
    action('SetClothing(Guard Lance, HeavyArmour)')
    action('SetClothing(Guard Jim, HeavyArmour)')
    action('CreateItem(TomSword, Sword)')
    action('CreateItem(LanceSword, Sword)')
    action('CreateItem(JimSword, Sword)')    
    action('SetPosition(TomSword, Guard Tom)')
    action('SetPosition(LanceSword, Guard Lance)')
    action('SetPosition(JimSword, Guard Jim)')
    action('SetCameraFocus(John)')
    #action('SetCameraFocus(QueensCastle.DiningTable)') #Change to door when the focus gets fixed
    action('Enter(Guard Tom, QueensCastle.Door)')
    action('Enter(Guard Tom, QueensCastle.Door)')
    action('Enter(Guard Tom, QueensCastle.Door)')
    action('SetDialog(Get him! [Next | Next])')
    action('SetRight(null)')
    action('SetLeft(Guard Lance)')
    action('ShowDialog()')
    wait_for_response(['Next'])
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
        elif received == 'input ReadInvitation Party Invitation':
            action('SetNarration(You are cordially invited to the Queen\'s Birthday Party. It will truly be one for the ages.)')
            action('ShowNarration()')
        else:
            if received.startswith('input Talk'):
                trigger_death += 1
            check_master_actions(received)
        
        if trigger_death > 2 and not global_game_states.queen_death:
                global_game_states.queen_death = True
                death_cutscene()
            