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

    #Create Items and position them 'Change_of_Clothes'
    action('CreateItem(CellDoorKey, BlueKey)')
    action('SetPosition(CellDoorKey, QueensCastle.Door)')
    action('CreateItem(PrisonLedger, PurpleBook)')
    action('SetPosition(PrisonLedger, Prison.Bookshelf.Left)')
    action('CreateItem(DireNews, OpenScroll)')
    action('SetPosition(DireNews, Prison.Table.Left)')
    action('CreateItem(Note_From_King, OpenScroll)')
    action('SetPosition(Note_From_King, Prison.DirtPile)')
    action('AddToList(Note_From_King, OpenScroll)')
    action('CreateItem(Change_of_Clothes, RedCloth)')
    
    #Enable Icons
    action('EnableIcon(Sit, Bed, Prison.Bed, Sit, true)')
    action('EnableIcon(Look_in_DirtPile, hand, Prison.DirtPile, Look through dirt, true)')
    action('EnableIcon(TakeLeft, hand, CellDoorKey, Take, true)')
    action('EnableIcon(Read, Research, Note_From_King, Read, true)')
    action('EnableIcon(TakeLeft, hand, Party_Invitation, Take, true)')
    action('EnableIcon(ChangeClothes, armour, Change_of_Clothes, Change Clothes, true)')