from action import action

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
        action('SetDialog(Oh who do we have here? The Queen\'s assistant you say? Well the Queen and I may not' +
        ' agree on everything but you seem like a fine young gentleman. [Next | Thanks who are you again?])')
        wait_for_response(['Next'])
        action('ClearDialog()')
        action('SetDialog(I\'m not that important. I\'m just the Kingdom\'s Grand Maester. Mainly just an advisory role but' +
        ' I plan on retiring at the end of the year...err...who are you again? [Next | ...The Queen\'s Assistant])')
        wait_for_response(['Next'])
        action('ClearDialog()')
        action('SetDialog(Right the castle chef. *The maester gets a glassy look and stares off in the distance* [Next | Goodbye])')
        wait_for_response(['Next'])
    elif person == 'Guard Gallant':
        action('SetDialog(Grrr... [Next | I\'ll be on my way.])')
        wait_for_response(['Next'])
    elif person == 'Queen Margerie':
        action('SetDialog(Isn\'t my husband so sweet! He did all of this for me! [Next | He sure is])')
        wait_for_response(['Next'])
    elif person == 'Witch Carlita':
        action('SetDialog(How can I help you? [Next | Can you teach me how to cast spells?])')
        wait_for_response(['Next'])
        action('ClearDialog()')
        action('SetDialog(Unfortunately that takes year of training. Maybe some other time [Next | Darn])')
        wait_for_response(['Next'])
    elif person == 'Tiana':
        action('SetDialog(I don\'t know why King Phillip went through all this trouble for Margerie. She\'s hardly' +
        ' worth it [One | Why are you so upset?] [Two | You should be more appreciate of Margerie])')
        received = wait_for_response(['One', 'Two'])
        action('ClearDialog()')
        if received == 'input Selected One':
            action('SetDialog(You would understand if you grew up with her[Next | I\'m sure])')
            wait_for_response(['Next'])
        else:
            action('SetDialog(I\'m sure she\'ll she appreciate what she\'s got coming to her [Next | ...okay])')
            wait_for_response(['Next'])
    elif person == 'King Phillip':
        action('SetDialog(Isn\'t Margerie lovely. I would be devastated if anything were to happen to her [Next | You really out did yourself])')
        wait_for_response(['Next'])

def scene_two_convo(person):
    if person == 'Guard':
        action('SetDialog(Don\'t you dare speak to me [Next | Fine])')
        wait_for_response(['Next'])
