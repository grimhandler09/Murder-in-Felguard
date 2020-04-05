from action import action

def set_left_right(left, right):
    action('SetLeft('+left+')')
    action('SetRight('+right+')')

def set_dialog(dialog, responses=['Next'], show=False):
    action('ClearDialog()')
    action('SetDialog(\"'+dialog+'\")')
    if show:
        action('ShowDialog()')
    return wait_for_response(responses)

def wait_for_response(responses):
    response_list = []
    for response in responses:
        response_list.append('input Selected ' + response)
    received = input().strip()
    while not received in response_list:
        received = input().strip()
    return received

def scene_one_predeath(person):
    if person == 'Maester Purcell':
        set_dialog('Oh who do we have here? The Queen\'s assistant you say? Well the Queen and I may not agree on everything' +
        ' but you seem like a fine young gentleman. [Next | Thanks who are you again?]')
        set_dialog('I\'m not that important. I\'m just the Kingdom\'s Grand Maester. Mainly just an advisory role but' +
        ' I plan on retiring at the end of the year...err...who are you again? [Next | ...The Queen\'s Assistant]')
        set_dialog('Right the castle chef. *The maester gets a glassy look and stares off in the distance* [Next | Goodbye]')
    elif person == 'Guard Gallant':
        set_dialog('Grrr... [Next | I\'ll be on my way.]')
    elif person == 'Queen Margerie':
        set_dialog('Isn\'t my husband so sweet! He did all of this for me! [Next | He sure is]')
    elif person == 'Witch Carlita':
        set_dialog('How can I help you? [Next | Can you teach me how to cast spells?]')
        set_dialog('Unfortunately that takes year of training. Maybe some other time [Next | Darn]')
    elif person == 'Tiana':
        received = set_dialog('I don\'t know why King Phillip went through all this trouble for Margerie. She\'s hardly' + 
        ' worth it [One | Why are you so upset?] [Two | You should be more appreciate of Margerie]', ['One', 'Two'])
        if received == 'input Selected One':
            set_dialog('You would understand if you grew up with her[Next | I\'m sure]')
        else:
            set_dialog('I\'m sure she\'ll she appreciate what she\'s got coming to her [Next | ...okay]')
    elif person == 'King Phillip':
        set_dialog('Isn\'t Margerie lovely. I would be devastated if anything were to happen to her [Next | You really out did yourself]')

def scene_two_convo(person):
    if person == 'Guard':
        set_dialog('Wait, how did you open the cell... [Next | I need to escape, for the King (Attack)]', ['Next'], True)
        action('HideDialog()')
