from action import action
import global_game_states 

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
        set_dialog('Oh, who do we have here? The Queen\'s assistant you say? Well, the Queen and I may not agree on everything' +
        ' but you seem like a fine young gentleman. [Next | Thanks who are you again?]')
        set_dialog('I\'m not that important. I\'m just the Kingdom\'s Grand Maester. Mainly just an advisory role, but' +
        ' I plan on retiring at the end of the year...err...who are you again? [Next | ...The Queen\'s Assistant]')
        set_dialog('Right the castle chef. *The maester gets a glassy look and stares off in the distance* [Next | Goodbye]')
    elif person == 'Guard Gallant':
        set_dialog('Grrr... [Next | I\'ll be on my way.]')
    elif person == 'Queen Margerie':
        set_dialog('Isn\'t my husband so sweet! He did all of this for me! [Next | He sure is]')
    elif person == 'Witch Carlita':
        set_dialog('How can I help you? [Next | Can you teach me how to cast spells?]')
        set_dialog("Unfortunately, that takes year of training. Maybe some other time [Next | Darn]")
    elif person == 'Tiana':
        received = set_dialog('I don\'t know why King Phillip went through all this trouble for Margerie. She\'s hardly' + 
        ' worth it [One | Why are you so upset?] [Two | You should appreciate Margerie more]', ['One', 'Two'])
        if received == 'input Selected One':
            set_dialog('You would understand if you grew up with her[Next | I\'m sure]')
        else:
            set_dialog('I\'m sure she\'ll she appreciate what she\'s got coming to her [Next | ...okay]')
    elif person == 'King Phillip':
        set_dialog('Isn\'t Margerie lovely. I would be devastated if anything were to happen to her [Next | You really out did yourself]')

def scene_one_postdeath(person):
    if person == 'King Phillip':
        set_dialog('My Margerie...what has happened to you! Please find out what has happened. [Next | I\'m so sorry Phillip, let me look around]')
    if person == 'Tiana':
        set_dialog('I mean I never preferred my sister, but I would never have wished this upon her. [Next | Why exactly did you two not get along?]')
        set_dialog('Father always favored her since she was in line for the throne. But again, I would never kill her because of it. [Next | I think the whole kingdom will feel the gravity of this loss]')
    if person == 'Maester Purcell':
        set_dialog('Margerie was never supposed to go before this old coot. Whoever did this has pure malice in their heart. [Next | We will bring them to justice]')
    if person == 'Noble Jeremy' or person == 'Noble Cecilia' or person == 'Merchant Bert':
        set_dialog('Oh how horrible! [Next | Did you see anything?]')
        set_dialog('I\'m sorry I didn\'t see anything. [Next | Okay let me know if you think of anything]')
    if person == 'Chamber Maid Scarlet':
        set_dialog('How can I help? [Next | You served the drink did you notice anything unusual?]')
        set_dialog('No, I poured the wine straight out of the bottle when I was setting up earlier. Everyone\'s cups were filled from the same bottle. [Next | Where did you get the wine?]')
        set_dialog('Where we always get it, the local tavern. [Next | Where was the taste tester?]')
        set_dialog('Errrm....I think he was off today because of the Queen\'s birthday [Next | Thanks for your time]')

    

def scene_two_convo(person):
    if person == 'Guard':
        set_dialog('Wait, how did you open the cell... [Next | I need to escape, for the King (Attack)]', ['Next'], True)
        action('HideDialog()')
        
def scene_two_and_half_convo(person):
    if person == 'Beggar Adeline':
        set_dialog('I\'m not sad about the Queen\'s death. She\'s been rolling in wealth while decent folks can\'t even find a job to support their families. [Next | ... okay?]')
    elif person == 'Beggar Miles':
        set_dialog('Spare some change for an old man? [Next | Sorry, I\'m broke]')
    elif person == 'Scout Joanna':
        set_dialog('You don\'t want to go this way. Once outside the town, you\'re on your own. [Next | Thanks!]')
    elif person == 'Alchemist Jeremy':
        set_dialog('Step inside for all your alchemy needs. Whether it\'s a nice polish for your shoes or a draught for your pain, we\'ve got it here! [Next | I\'ll keep that in mind]')
    elif person == 'Scout Tom':
        set_dialog('You don\'t want to go this way. Once outside the town, you\'re on your own. [Next | Thanks!]')
    elif person == 'Drunk Devon':
        set_dialog('My name is Devon. This here is the Tavern, a good place to hear the comings and goings of the town.')
    elif person == 'Princess Esmerelda':
        set_dialog('The witches must burn! It is no surprise the Queen is dead given the monarchy\'s flagrant disrespect of the sacred texts and ancient traditions. [Next | err... ok]')
    elif person == 'Blind Bandit':
        set_dialog('I heard a rumour last fortnight about a contract killing of the Queen, but I didn\'t believe it until now. [Next | ... Interesting]')
    elif person == 'Gossiping Gail':
        set_dialog('I know everything going on in this town. Go ahead ask me. [Next | I\'d rather not.')

def scene_three_convo(person):
    pr = 'input Selected Menu'
    while(pr != 'input Selected Done' and person == 'Alchemist Henry'):
        if pr == 'input Selected Menu' and global_game_states.found_poison_purchase == False and global_game_states.found_poison == False and global_game_states.identified_poison == False:
            pr = set_dialog('Welcome! Feel free to look around. [Done | Thanks]')
        elif pr == 'input Selected Menu' and global_game_states.found_poison_purchase == True and global_game_states.found_poison == False and global_game_states.identified_poison == False:
            pr = set_dialog('Find anything you like? [Purchase | Who is Tianna?] [Done | Still looking around]')
        elif pr == 'input Selected Menu' and global_game_states.found_poison_purchase == False and global_game_states.found_poison == True and global_game_states.identified_poison == False:
            pr = set_dialog('Need help with anything else? [Free | Are you sure I can have this?] [Done | No, thanks]')
        elif pr == 'input Selected Menu' and global_game_states.found_poison_purchase == True and global_game_states.found_poison == True and global_game_states.identified_poison == False:
            pr = set_dialog('Need help with anything else? [Purchase | Who is Tianna?] [Free | Are you sure I can have this?] [Done | No, thanks]')
        elif pr == 'input Selected Menu' and global_game_states.found_poison_purchase == False and global_game_states.found_poison == False and global_game_states.identified_poison == True:
            pr = set_dialog('Find anything you like? [About | Actually...] [Done | Still looking around]')
        elif pr == 'input Selected Menu' and global_game_states.found_poison_purchase == True and global_game_states.found_poison == False and global_game_states.identified_poison == True:
            pr = set_dialog('Find anything you like? [Purchase | Who is Tianna?] [About | Actually...] [Done | Still looking around]')
        elif pr == 'input Selected Menu' and global_game_states.found_poison_purchase == False and global_game_states.found_poison == True and global_game_states.identified_poison == True:
            pr = set_dialog('Need help with anything else? [Free | Are you sure I can have this?] [About | Actually...] [Done | No, thanks]')
        elif pr == 'input Selected Menu' and global_game_states.found_poison_purchase == True and global_game_states.found_poison == True and global_game_states.identified_poison == True:
            pr = set_dialog('Need help with anything else? [Purchase | Who is Tianna?] [Free | Are you sure I can have this?] [About | Actually...] [Done | No, thanks]')
        elif pr == 'input Selected Purchase':
            pr = set_dialog('Oh, Tianna? She\'s the Queen\'s sister. She recently bought some giant rat poison to help clear the sewers. [Menu | Thanks]')
        elif pr == 'input Selected Free':
            pr = set_dialog('If you\'re investigating for the king, take it! Quick, before I change my mind! [Menu | Okay...]')
        elif pr == 'input Selected About' and global_game_states.found_poison == False:
            pr = set_dialog('Oh, the giant rat poison? I usually don\'t sell it to civilians. [About2 | The king asked me]')
        elif pr == 'input Selected About' and global_game_states.found_poison == True:
            pr = set_dialog('The giant rat poison? Didn\'t you already grab it? [Menu | Yeah...]')
        elif pr == 'input Selected About2':
            pr = set_dialog('You\'re investigating for the king? Take the display bottle. It\'s the one with a skull and crossbones. [Menu | Thanks]')
            action('EnableIcon(TakeLeft, hand, Poison, false)')
            if 'Found Poison' not in global_game_states.current_clues:
                global_game_states.current_clues.append('Found Poison')
            #add_clue('Found Poison')
            global_game_states.found_poison = True
        
def scene_four_convo(person):
    if person == 'Maester Purcell':
        set_dialog('Oh! Where am I? Oh that\'s right, the tavern. I really should be going. Who are you again? *The maester gets a glassy look and stares off in the distance* [Next | erm... ok?]')
    elif person == 'Witch Carlita':
        set_dialog('That Maester Purcell sure acts like a fool, but he\'s sharp as a tack. Don\'t let him fool you [Next | Thanks for the heads up]')
    elif person == 'Noble Jeremy':
        set_dialog('This murder is the most interesting thing to happen in years. Remember back when the Queen\'s Uncle got his leg eaten by that shark? Now that was a story. [Next | ...Fascinating.]')
    elif person == 'Noble Cecilia':
        set_dialog('Tiana has always been jealous of her sister, I just can\'t imagine she would poison her. [Next | ...]')
    elif person == 'Merchant Bert':
        set_dialog('I sold the Alchemist a whole cart-load of ingredients last week, some of them were poisons. If you want to look for clues, I\'d start with the Alchemist shop [Next | Thanks, I\'ll take a look around.]')
    elif person == 'Chamber Maid Scarlet':
        set_dialog('*Scarlet sits silently trembling, fumbling for words* [Next | Next]') 
