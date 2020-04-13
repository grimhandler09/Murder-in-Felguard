'''
Authors: Travis Conley
Purpose: Functions that deal with pocketing and sheathing inventory plus their opposites
'''
import global_game_states
from action import action

'''
Purpose: Removes item from non player inventories
Inputs: item to be removed
Outputs: None
'''
def remove_item(item):
    # Check each inventory in the list of inventories
    for inventory in global_game_states.list_of_inventories:
        # Check each item in the given inventory
           for individual_item in inventory:
               #If the item is found and it is not currently in the player inventory
               if individual_item == [item, item] and not (inventory == global_game_states.player_inventory):
                   inventory.remove([item, item])

'''
Purpose: Allows John to take left handed items out of inventory
Inputs: item to be drawn in the left hand
Outputs: None
'''
def take_leftitem_action(item):
    # If the item was not already in inventory, pick it up and add it
    if [item, item] not in global_game_states.player_inventory:
        global_game_states.player_inventory.append([item, item])
        remove_item(item)
        action('HideList()')
        action('Pickup(John, ' + item +')')
    else:
        # If it was in inventory, take it out
        action('Unpocket(John, ' + item +')')

    # Switch enabled icons
    action('DisableIcon(TakeLeft, ' + item + ')')
    action('EnableIcon(StowLeft, hand, ' + item + ', Stow, true)')

'''
Purpose: Allows John to take right handed items out of inventory
Inputs: item to be drawn in the right hand
Outputs: None
'''
def take_rightitem_action(item):
    # If the item was not already in inventory, pick it up and add it
    if [item, item] not in global_game_states.player_inventory:
       global_game_states.player_inventory.append([item, item])
       remove_item(item)
       #action('Pickup(John, ' + item +')')
       action('HideList()')
       action('Draw(John, ' + item +')')
    else:
        # If it was in inventory, take it out
        action('Draw(John, ' + item +')')
    
    # Switch enabled icons
    action('DisableIcon(TakeRight, ' + item + ')')
    action('EnableIcon(StowRight, hand, ' + item + ', Stow, true)')


'''
Purpose: Allows John to put left handed items in inventory
Inputs: item to be put in inventory
Outputs: None
'''
def stow_leftitem_action(item):
    # Animation for pocketing 
    action('Pocket(John, ' + item +')')

    # Switch enabled Icons
    action('DisableIcon(StowLeft, ' + item + ')')
    action('EnableIcon(TakeLeft, hand, ' + item + ', Take, true)')

'''
Purpose: Allows John to put right handed items in inventory
Inputs: item to be put in inventory
Outputs: None
'''
def stow_rightitem_action(item):
    # Animation for sheathing
    action('Sheathe(John, ' + item +')')

    # Switch enabled Icons
    action('DisableIcon(StowRight, ' + item + ')')
    action('EnableIcon(TakeRight, hand, ' + item + ', Take, true)')