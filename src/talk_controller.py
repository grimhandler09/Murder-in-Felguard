from action import action

def scene_one_predeath(person):
    if person == 'Maester Purcell':
        action('SetDialog(Oh who do we have here? The Queen\'s assistant you say? Well the Queen and I may not' +
        ' agree on everything but you seem like a fine young gentleman. [Next | Thanks who are you again?])')
        input()
        action('ClearDialog()')
        action('SetDialog(I\'m not that important. I\'m just the Kingdom\'s Grand Maester. Mainly just an advisory role but' +
        ' I plan on retiring at the end of the year...err...who are you again? [Next | ...The Queen\'s Assistant])')
        input()
        action('ClearDialog()')
        action('SetDialog(Right the castle chef. *The maester gets a glassy look and stares off in the distance* [Next | Goodbye])')
        input()
    elif person == 'Guard Gallant':
        action('SetDialog(Grrr... [Next | I\'ll be on my way.])')
        input()
    elif person == 'Queen Margerie':
        action('SetDialog(Isn\'t my husband so sweet! He did all of this for me! [Next | He sure is])')
        input()
    elif person == 'Witch Carlita':
        action('SetDialog(How can I help you? [Next | Can you teach me how to cast spells?])')
        input()
        action('ClearDialog()')
        action('SetDialog(Unfortunately that takes year of training. Maybe some other time [Next | Darn])')
        input()
    elif person == 'Tiana':
        action('SetDialog(I don\'t know why King Phillip went through all this trouble for Margerie. She\'s hardly' +
        ' worth it [One | Why are you so upset?] [Two | You should be more appreciate of Margerie])')
        received = input()
        action('ClearDialog()')
        if received == 'input Selected One':
            action('SetDialog(You would understand if you grew up with her[Next | I\'m sure])')
            input()
        else:
            action('SetDialog(I\'m sure she\'ll she appreciate what she\'s got coming to her [Next | ...okay])')
            input()
    elif person == 'King Phillip':
        action('SetDialog(Isn\'t Margerie lovely. I would be devastated if anything were to happen to her [Next | You really out did yourself])')
        input()