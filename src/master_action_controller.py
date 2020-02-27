from action import action
from talk_controller import *
from global_game_states import *
player_inventory = [['Party Invitation', 'Birthday Party Invitation']]

def talk_action(person):
    action('SetLeft(John)')
    action('SetRight(' + person + ')')
    action('ShowDialog()')
    if not get_queen_death():
        scene_one_predeath(person)
    action('HideDialog()')

#Send sit command with the place as the parameter
def sit_action(place):
    command = "Sit(John, " + place + ")"
    action(command)

def check_master_actions(received):
    if received.startswith('input Sit'):
        received = received.split(' ')
        place = received[len(received) - 1]
        sit_action(place)
    elif received.startswith('input Talk'):
        person = received[11:]
        talk_action(person)
    elif received == "input Close Narration":
        action('HideNarration()')
        action('ClearNarration()')
    elif received == "input Close List":
        action("HideList()")
    elif received == "input Key Inventory":
        action('ClearList()')
        for item in player_inventory:
            action('AddToList(' + item[0] + ', ' + item[1] + ')')
        action('ShowList(John)')
        
