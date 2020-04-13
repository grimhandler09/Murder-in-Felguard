'''
Author: Zachary Moore
Purpose: Handles the players interactions with the castle scene
'''

# Imports 
import time
from action import action
from master_action_controller import check_master_actions, scene_start, add_clue, midscene_narration
import global_game_states
from talk_controller import *
from add_clue import add_clue

'''
Purpose: Plays the games beginning butscene
Inputs: None
Outputs: None
'''
def opening_cutscene():
    # Cutscene Setup
    action('SetCameraFocus(QueensCastle.DiningTable)')
    action('HideMenu()')
    action('EnableInput()')
    midscene_narration('Welcome to the Queen\'s birthday bash!')
    action('FadeIn()')

    # King's dialogue
    set_left_right('King Phillip', 'Queen Margerie')
    set_dialog('Happy Birthday Darling! I\'ve invited all of your closest friends and family to celebrate! [Next| Next]', ['Next'], True)
    set_dialog('Enjoy your night Margerie. You\'ve earned it after ruling Felgard faithfully by my side for the last 20 years. [Next| Next]')
    set_dialog('In honor of the momentous occasion I got Carlita the Castle Witch to give you a very special present! [Next| Next]')
    action('HideDialog()')
    
    # Witch casting spell
    action('WalkToSpot(Witch Carlita, 303.1, 0.1, 5.2)')
    action('Cast(Witch Carlita, Queen Margerie)')
    action('EnableEffect(Queen Margerie, Heart)')
    time.sleep(2.5)
    
    # Finishing Dialog
    set_left_right('King Phillip', 'Queen Margerie')
    set_dialog('Let the party commence! [Next| Next]', ['Next'], True)
    action('HideDialog()')
    action('SetCameraFocus(John)')
    action('SetCameraMode(follow)')

'''
Purpose: Plays the Queen's death cutscene
Inputs: None
Outputs: None
'''
def death_cutscene():
    # Scene Setup
    action('DisableEffect(Queen Margerie)')
    action('DisableIcon(Talk, Queen Margerie)')
    action('SetPosition(QueensCup, Queen Margerie)')
    action('SetCameraFocus(QueensCastle.DiningTable)')
    time.sleep(1)
    
    # Queen Standing up
    action('WalkToSpot(Queen Margerie, 305.7, 0.1, 0.6)')
    action('Face(Queen Margerie, King Phillip)')
    action('SetCameraFocus(Queen Margerie)')
    action('SetCameraMode(focus)')
    set_left_right('Queen Margerie', 'null')

    # Queen Dialog
    set_dialog('Thank you all for coming to my birthday bash! [Next| Next]', ['Next'], True)
    set_dialog('It\'s so wonderful to see you all here. I look forward to many more glorious years ruling the kingdom! Cheers! [Next| Next]')
    action('HideDialog()')

    # Drinking and Death
    action('Drink(Queen Margerie)')
    action('SetPosition(QueensCup, QueensCastle.DiningTable.Right)')
    set_dialog('Now let us... [Next| Next]', ['Next'], True)
    action('HideDialog()')
    action('SetExpression(Queen Margerie, Disgusted)')
    action('Die(Queen Margerie)')
    action('PlaySound(Scream)')

    # King rushes over
    action('SetCameraFocus(QueensCastle.DiningTable)')
    action('WalkToSpot(King Phillip, 307.6, 0.1, -0.9)')
    action('Face(King Phillip, Queen Margerie)')
    action('HideNarration()')

    # Facial expressions
    action('SetExpression(King Phillip, Sad)')
    action('SetExpression(Maester Purcell, Sad)')
    action('SetExpression(Merchant Bert, Sad)')
    action('SetExpression(Noble Cecilia, Sad)')
    action('SetExpression(Noble Jeremy, Sad)')
    action('SetExpression(Witch Carlita, Sad)')
    action('SetExpression(Chamber Maid Scarlet, Sad)')

    # New Talking Icons
    action('EnableIcon(Talk, Talk, Noble Jeremy, Talk to Jeremy, true)')
    action('EnableIcon(Talk, Talk, Noble Cecilia, Talk to Cecilia, true)')
    action('EnableIcon(Talk, Talk, Merchant Bert, Talk to Bert, true)')
    action('EnableIcon(Talk, Talk, Chamber Maid Scarlet, Talk to Scarlet, true)')
    action('EnableIcon(OpenCloset, Door, QueensCastle.BackDoor, Open Door, true)')
    action('DisableIcon(Talk, Witch Carlita)')
    action('DisableIcon(Talk, Guard Gallant)')

    # Guard walks over
    action('SetCameraFocus(QueensCastle.Door)')
    action('Kneel(King Phillip)')
    action('WalkToSpot(Guard Gallant, 305.8, 0.1, -2.3)')
    action('Face(Guard Gallant, Queen Margerie)')
    action('SetCameraMode(follow)')
    action('SetCameraFocus(John)')
    action('EnableInput()')
    action('Kneel(Guard Gallant)')

    # New Clues
    action('EnableIcon(InspectCup, Research, QueensCup, Inspect Cup, true)')
    action('EnableIcon(TriggerGuards, Door, QueensCastle.Door, Leave Castle, true)')
    add_clue('The Queen died after drinking from her cup', 'QueensCup')

'''
Purpose: Plays the cutscene for the arrest of John
Inputs: None
Outputs: None
'''
def arrest_cutscene():
    # Cutscene setup
    action('StopSound()')
    action('PlaySound(Danger3, QueensCastle, true)')
    action('HideDialog()')
    action('HideNarration()')
    action('CreateCharacter(Guard Tom, B)')
    action('SetClothing(Guard Tom, HeavyArmour)')
    action('CreateItem(TomSword, Sword)')  
    action('SetPosition(TomSword, Guard Tom)')

    # Scarlet's dialog
    action('SetCameraFocus(Chamber Maid Scarlet)')
    set_left_right('Chamber Maid Scarlet', 'null')
    action('SetExpression(Chamber Maid Scarlet, Surprised)')
    set_dialog('Guards! It was the queen\'s aide! He killed the Queen! [Next| Next]', ['Next'], True)
    action('HideDialog()')

    # Guard Enters
    action('SetCameraFocus(QueensCastle.Door)')
    action('Enter(Guard Tom, QueensCastle.Door)')
    action('SetCameraFocus(John)')
    action('SetCameraMode(follow)')
    set_left_right('Guard Tom', 'null')
    set_dialog('Get him! [Next| Next]', ['Next'], True)
    action('HideDialog()')
    action('StopSound()')
    # Next scene setup
    global_game_states.current_scene = 'dungeon'
    global_game_states.prev_scene = 'castle'
    action('CreateItem(Chamber Maid Accusation, OpenScroll)')
    add_clue('The chamber maid has accused John of killing the queen', 'Chamber Maid Accusation')


'''
Purpose: Handles the interactions with things in the castle scene. Plays cutscenes when appropriate
Inputs: None
Outputs: None
'''
def castle_controller():
    # Generic scene start actions
    scene_start()

    # Play the opening cutscene
    opening_cutscene()

    # Gameplay controls
    midscene_narration('Welcome to Our Game! \\nImportant controls: \\n\\nI - Bring up player inventory \\nE - Bring up player clues')

    # Counter to keep track of dialog interactions before Queens death
    trigger_death = 0

    # Loop while the scene is still the castle
    while global_game_states.current_scene == 'castle':

        # Get input from Camelot
        received = input()

        # Check the action received from Camelot
        if received == 'input ReadLedger GuestLedger':
            # Contents of ledger
            action('PlaySound(Book)')
            midscene_narration('Nobleman Jeremy - Holder of lands to the south. Childhood friend of Queen Margerie\\nNoblewoman Celcilia -'
            + 'Wife of Nobleman Jeremy\\nMerchant Bert - The most prominent merchant in all of Felguard\\nGrand Maester Purcell - Felgard\'s '
            + 'longest serving maester\\nWitch Carlita - The castle mage')
            trigger_death += 1
        elif received == 'input ReadInvitation Party Invitation':
            # Reading invitation
            action('PlaySound(Book)')
            midscene_narration('You are cordially invited to the Queen\'s Birthday Party. It will truly be one for the ages.')
        elif received == 'input InspectCup QueensCup':
            # Clue for investigating cup
            midscene_narration('You notice the wine in the cup is a slightly different shade then the wine you had.')
            action('CreateItem(Wine Cup Color, GoldCup)')
            add_clue('The Queen\'s Cup of wine had an odd coloring to it', 'Wine Cup Color')
        elif received == 'input OpenCloset QueensCastle.BackDoor':
            # Enter storage if you have key, else tell player its locked
            if global_game_states.castle_key:
                action('Exit(John, QueensCastle.BackDoor, true)')
                action('Enter(John, CastleStorage.Door, true)')
            else:
                midscene_narration('The door is locked!')
        elif received == 'input CheckClosetKeyBag ClosetKeyBag':
            action('PlaySound(Pocket)')
            # Bag is empty if before Queen death, contains key if after
            if global_game_states.queen_death and not global_game_states.castle_key:
                action('Take(John, ClosetKey, ClosetKeyBag)')
                action('Pocket(John, ClosetKey)')
                midscene_narration('You find a key in the bag!')
                global_game_states.player_inventory.append(['ClosetKey', 'A mysterious key'])
                global_game_states.castle_key = True
            else:
                midscene_narration('The bag is empty')
        elif received == 'input InspectTester Tester':
            # Taste tester clue
            midscene_narration('You recognize the body of the Queen\'s taste tester')
            action('CreateItem(Taste Testers Death, OpenScroll)')
            add_clue('The Queen\'s taste tester was dead in the closet', 'Taste Testers Death')
        elif received == 'input OpenStorageChest CastleStorage.Chest':
            # Poison bottle clue
            midscene_narration('You find an empty potion bottle. The label is marked with a skull and crossbones')
            action('CreateItem(Empty Potion Bottle,PurplePotion)')
            add_clue('In castle storage, you found a suspicious looking potion bottle', 'Empty Potion Bottle')
        elif received == 'input ReadAlchemistLetter AlchemistLetter':
            # Alchemist Letter clue
            action('PlaySound(Book)')
            midscene_narration('The letter reads: To ensure a lethal dose, use about 10mL\\n-AH') 
            action('CreateItem(Letter from AH, OpenScroll)')   
            add_clue('A letter in the castle storage referenced a poison written by a mysterious AH', 'Letter from AH')
        elif received == 'input ExitStorage CastleStorage.Door':
            # Exit Storage and reenter castle. 
            action('Exit(John, CastleStorage.Door, true)')
            action('Enter(John, QueensCastle.BackDoor, true)')
            time.sleep(1.0)

            # Play arrest cutscene
            arrest_cutscene()
        elif received == 'input TriggerGuards QueensCastle.Door':
            # Play arrest cutscene if you try to leave
            arrest_cutscene() 
        else:
            # Add counter if talk action
            if received.startswith('input Talk'):
                trigger_death += 1
            
            # Check default master actions
            check_master_actions(received)
        
        # Trigger queen death if 3 interactions
        if trigger_death > 2 and not global_game_states.queen_death:
                global_game_states.queen_death = True
                death_cutscene()
            