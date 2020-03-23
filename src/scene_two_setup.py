from action import action
import time

def scene_two_setup():
    action('FadeOut()')
    #Create the Prison that John will be thrown into
    action('CreatePlace(Prison, Dungeon)')
    
    #Move Character(John) to the dungeon
    action('SetClothing(John, Peasant)')
    action('SetPosition(John, Prison.CellDoor.Inside)')

    #Create CellDoor Guard
    action('CreateCharacter(Guard, C)')
    action('SetClothing(Guard, LightArmour)')
    action('SetHairStyle(Guard, Short)')
    action('SetPosition(Guard, Prison.CellDoor)')

    #Create Items and position them
    action('CreateItem(PlayerSword, Sword)')
    action('SetPosition(PlayerSword, Prison.DirtPile)')
    action('CreateItem(CellDoorKey, BlueKey)')
    action('SetPosition(CellDoorKey, QueensCastle.Door)')
    action('AddToList(PlayerSword, Sword)')
    
    #Enable Icons
    action('EnableIcon(Sit, Bed, Prison.Bed, Sit, true)')
    #action('EnableIcon(Leave, Door, Prison.Door, Leave, true)')
    action('EnableIcon(Talk, Talk, Guard, Talk to the Guard, true)')
    action('EnableIcon(Look_in, hand, Prison.DirtPile, Look through dirt, true)')
    #action('EnableIcon(Look_up, hand, Prison.Chest, Look through chest, true)')
    #action('EnableIcon(Attack, sword, Guard, Strike, false)')
    action('EnableIcon(Use, door, Prison.CellDoor, Open, true)')
    action('EnableIcon(TakeLeft, hand, CellDoorKey, Take, true)')
    action('EnableIcon(TakeRight, hand, PlayerSword, Take, true)')

    #Populate containers of items
    #Prison.Chest = [['PlayerSword', 'Sword'], ['CellDoorKey', 'CellKey']]