from action import action
import global_game_states
import time

def dungeon_setup():

    action('FadeOut()')

    #Create the Prison that John will be thrown into
    action('CreatePlace(Prison, Dungeon)')
    action('SetCameraFocus(Prison.CellDoor)')
    action('SetCameraMode(follow)')
    
    #Adjust player inventory
    global_game_states.player_inventory = []

    #Move Character(John) to the dungeon
    action('SetClothing(John, Peasant)')
    action('SetPosition(John, Prison.CellDoor.Inside)')

    #Create CellDoor Guard
    action('CreateCharacter(Guard, C)')
    action('SetClothing(Guard, LightArmour)')
    action('SetHairStyle(Guard, Short)')
    action('SetPosition(Guard, Prison.CellDoor)')
    action('WalkToSpot(Guard, -608.6, 0.0, -2.7)')

    #Create Items and position them 'Change_of_Clothes'
    action('CreateItem(Cell Door Key, BlueKey)')
    action('SetPosition(Cell Door Key, QueensCastle.Door)')
    action('CreateItem(Prison Ledger, PurpleBook)')
    action('SetPosition(Prison Ledger, Prison.Bookshelf.Left)')
    action('CreateItem(Dire News, OpenScroll)')
    action('SetPosition(Dire News, Prison.Table.Left)')
    action('CreateItem(Note From King, OpenScroll)')
    action('SetPosition(Note From King, Prison.DirtPile)')
    action('AddToList(Note From King, OpenScroll)')
    action('CreateItem(Change of Clothes, RedCloth)')
    
    #Enable Icons
    action('EnableIcon(Sit, Bed, Prison.Bed, Sit, true)')
    action('EnableIcon(Look_in_DirtPile, hand, Prison.DirtPile, Look through dirt, true)')
    action('EnableIcon(TakeLeft, hand, Cell Door Key, Take, true)')
    action('EnableIcon(Read, Research, Note From King, Read, true)')
    action('EnableIcon(TakeLeft, hand, Party Invitation, Take, true)')
    action('EnableIcon(ChangeClothes, armour, Change of Clothes, Change Clothes, true)')