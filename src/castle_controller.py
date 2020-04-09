import time
from action import action
from master_action_controller import check_master_actions, scene_start, add_clue
import global_game_states
from talk_controller import *

def opening_cutscene():
    action('SetCameraFocus(QueensCastle.DiningTable)')
    action('HideMenu()')
    action('EnableInput()')
    action('SetNarration(Welcome to the Queen\'s birthday bash!)')
    action('ShowNarration()')
    input()
    action('HideNarration()')
    action('FadeIn()')
    set_left_right('King Phillip', 'Queen Margerie')
    set_dialog('Happy Birthday Darling! I\'ve invited all of your closest friends and family to celebrate! \n[Next| Next]', ['Next'], True)
    set_dialog('Enjoy your night Margerie. You\'ve earned it after ruling Felgard faithfully by my side for the last 20 years. \n[Next| Next]')
    set_dialog('In honor of the momentous occasion I got Carlita the Castle Witch to give you a very special present! \n[Next| Next]')
    action('HideDialog()')
    action('WalkToSpot(Witch Carlita, 303.1, 0.1, 5.2)')
    action('Cast(Witch Carlita, Queen Margerie)')
    action('EnableEffect(Queen Margerie, Heart)')
    time.sleep(2.5)
    set_left_right('King Phillip', 'Queen Margerie')
    set_dialog('Let the party commence! \n[Next| Next]', ['Next'], True)
    action('HideDialog()')
    action('SetCameraFocus(John)')
    action('SetCameraMode(follow)')

def death_cutscene():
    action('DisableEffect(Queen Margerie)')
    action('DisableIcon(Talk, Queen Margerie)')
    action('SetPosition(QueensCup, Queen Margerie)')
    action('SetCameraFocus(QueensCastle.DiningTable)')
    time.sleep(1)
    action('WalkToSpot(Queen Margerie, 305.7, 0.1, 0.6)')
    action('Face(Queen Margerie, King Phillip)')
    action('SetCameraFocus(Queen Margerie)')
    action('SetCameraMode(focus)')
    set_left_right('Queen Margerie', 'null')
    set_dialog('Thank you all for coming to my birthday bash! \n[Next| Next]', ['Next'], True)
    set_dialog('It\'s so wonderful to see you all here. I look forward to many more glorious years ruling the kingdom! Cheers! \n[Next| Next]')
    action('HideDialog()')
    action('Drink(Queen Margerie)')
    #action('Put(Queen Margerie, QueensCup)')
    action('SetPosition(QueensCup, QueensCastle.DiningTable.Right)')
    set_dialog('Now let us... \n[Next| Next]', ['Next'], True)
    action('HideDialog()')
    action('SetExpression(Queen Margerie, Disgusted)')
    action('Die(Queen Margerie)')
    action('SetCameraFocus(QueensCastle.DiningTable)')
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
    action('EnableIcon(Talk, Talk, Noble Jeremy, Talk to Jeremy, true)')
    action('EnableIcon(Talk, Talk, Noble Cecilia, Talk to Cecilia, true)')
    action('EnableIcon(Talk, Talk, Merchant Bert, Talk to Bert, true)')
    action('EnableIcon(Talk, Talk, Chamber Maid Scarlet, Talk to Scarlet, true)')
    action('EnableIcon(OpenCloset, Door, QueensCastle.BackDoor, Open Door, true)')
    action('DisableIcon(Talk, Witch Carlita)')
    action('DisableIcon(Talk, Guard Gallant)')
    action('SetCameraFocus(QueensCastle.Door)')
    action('Kneel(King Phillip)')
    action('WalkToSpot(Guard Gallant, 305.8, 0.1, -2.3)')
    action('Face(Guard Gallant, Queen Margerie)')
    action('SetCameraMode(follow)')
    action('SetCameraFocus(John)')
    action('EnableInput()')
    action('Kneel(Guard Gallant)')
    action('EnableIcon(InspectCup, Research, QueensCup, Inspect Cup, true)')
    action('EnableIcon(TriggerGuards, Door, QueensCastle.Door, Leave Castle, true)')
    add_clue('The Queen died after drinking from her cup')

def arrest_cutscene():
    action('HideDialog()')
    action('HideNarration()')
    action('CreateCharacter(Guard Tom, B)')
    action('SetClothing(Guard Tom, HeavyArmour)')
    action('CreateItem(TomSword, Sword)')  
    action('SetPosition(TomSword, Guard Tom)')
    action('SetCameraFocus(Chamber Maid Scarlet)')
    set_left_right('Chamber Maid Scarlet', 'null')
    action('SetExpression(Chamber Maid Scarlet, Surprised)')
    set_dialog('Guards! It was the queen\'s aide! He killed the Queen! \n[Next| Next]', ['Next'], True)
    action('HideDialog()')
    action('SetCameraFocus(QueensCastle.Door)')
    action('Enter(Guard Tom, QueensCastle.Door)')
    action('SetCameraFocus(John)')
    action('SetCameraMode(follow)')
    set_left_right('Guard Tom', 'null')
    set_dialog('Get him! \n[Next| Next]', ['Next'], True)
    action('HideDialog()')
    global_game_states.current_scene = 'dungeon'
    global_game_states.prev_scene = 'castle'
    add_clue('The chamber maid has accused of killing the queen')

def prepare_storage():
    action('CreatePlace(CastleStorage, Storage)')
    action('CreateCharacter(Tester, D)')
    action('SetClothing(Tester, Noble)')
    action('SetPosition(Tester, CastleStorage.Shelf)')
    action('WalkToSpot(Tester, 601.8, 0.1, -2.0)')
    action('Die(Tester)')
    action('CreateItem(AlchemistLetter, OpenScroll)')
    action('SetPosition(AlchemistLetter, CastleStorage.Barrel)')
    action('EnableIcon(ReadAlchemistLetter, Read, AlchemistLetter, Read Letter, true)')
    action('EnableIcon(OpenStorageChest, Chest, CastleStorage.Chest, Open Chest, true)')
    action('EnableIcon(InspectTester, Research, Tester, Inspect Body, true)')
    action('EnableIcon(ExitStorage, Door, CastleStorage.Door, Exit, true)')


def castle_controller():
    scene_start()
    opening_cutscene()
    action('SetNarration(Welcome to Our Game! Important controls: I - Bring up player inventory, E - Bring up player clues)')
    action('ShowNarration()')
    input()
    trigger_death = 0
    while(global_game_states.current_scene == 'castle'):
        received = input()
        if received == 'input ReadLedger GuestLedger':
            action("SetNarration(Nobleman Jeremy - Holder of lands to the south. Childhood friend of Queen Margerie...Noblewoman Celcilia - Wife of Nobleman Jeremy)")
            action('ShowNarration()')
            trigger_death += 1
        elif received == 'input ReadInvitation Party Invitation':
            action('SetNarration(You are cordially invited to the Queen\'s Birthday Party. It will truly be one for the ages.)')
            action('ShowNarration()')
        elif received == 'input InspectCup QueensCup':
            action('SetNarration(You notice the wine in the cup is a slightly different shade then the wine you had.)')
            action('ShowNarration()')
            add_clue('The Queen\'s Cup of wine had an odd coloring too it')
        elif received == 'input OpenCloset QueensCastle.BackDoor':
            if global_game_states.castle_key:
                action('Exit(John, QueensCastle.BackDoor, true)')
                prepare_storage()
                action('Enter(John, CastleStorage.Door, true)')
            else:
                action('SetNarration(The door is locked!)')
                action('ShowNarration()')
        elif received == 'input CheckClosetKeyBag ClosetKeyBag':
            if global_game_states.queen_death and not global_game_states.castle_key:
                action('Take(John, ClosetKey, ClosetKeyBag)')
                action('Pocket(John, ClosetKey)')
                action('SetNarration(You find a key in the bag!)')
                action('ShowNarration()')
                global_game_states.player_inventory.append(['ClosetKey', 'A mysterious key'])
                global_game_states.castle_key = True
            else:
                action('SetNarration(The bag is empty)')
                action('ShowNarration()')
        elif received == 'input InspectTester Tester':
            action('SetNarration(You recognize the body of the Queen\'s taste tester)')
            action('ShowNarration()')
            add_clue('The Queen\'s taste tester was dead in the closet')
        elif received == 'input OpenStorageChest CastleStorage.Chest':
            action('SetNarration(You find an empty potion bottle. The label is marked with a skull and crossbones)')
            action('ShowNarration()')
            add_clue('In castle storage, you found a suspicious looking potion bottle')
        elif received == 'input ReadAlchemistLetter AlchemistLetter':
            action('SetNarration(\"The letter reads: To ensure a lethal dose, use about 10mL-AH\")')
            action('ShowNarration()')      
            add_clue('A letter in the castle storage referenced a poison written by a mysterious AH')
        elif received == 'input ExitStorage CastleStorage.Door':
            action('Exit(John, CastleStorage.Door, true)')
            action('Enter(John, QueensCastle.BackDoor, true)')
            time.sleep(1.0)
            arrest_cutscene()
        elif received == 'input TriggerGuards QueensCastle.Door':
            arrest_cutscene() 
        else:
            if received.startswith('input Talk'):
                trigger_death += 1
            check_master_actions(received)
        
        if trigger_death > 2 and not global_game_states.queen_death:
                global_game_states.queen_death = True
                death_cutscene()
            