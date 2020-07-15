''' 
Authors: Zach Moore, Travis Conley, Adrian Wyllie, Mitchel Dennis
Purpose: Handle dialogue throughout the game
'''

# Import files 
from action import action
import global_game_states 
from add_clue import add_clue

'''
Purpose: Set left and right characters for dialogue
Inputs: Left and right person
Outputs: None
''' 
def set_left_right(left, right):
    action('SetLeft('+left+')')
    action('SetRight('+right+')')
    
'''
Purpose: Performs basic talk setup in a modular fashion
Inputs: Person being talked to
Outputs: None
'''
def talk_action(person):
    # Set left and right character
    set_left_right('John', person)
    action('ShowDialog()')

    # Determine which dialog sequence to check depending on the current scene
    if not global_game_states.queen_death:
        castle_predeath(person)
    elif global_game_states.queen_death and global_game_states.current_scene == 'castle':
        castle_postdeath(person)
    elif global_game_states.current_scene == 'dungeon':
        dungeon_convo(person)
    elif global_game_states.current_scene == 'city':
        city_convo(person)
    elif global_game_states.current_scene == 'alchemist_shop':
        alchemist_shop_convo(person)
    elif global_game_states.current_scene == 'tavern':
        tavern_convo(person)
    action('HideDialog()')

'''
Purpose: Performs repeated Camelot dialogue setup actions
Inputs: Dialogue to be said, the acceptable responses, and whether or not it is the first dialog interaction
Outputs: Selected dialogue response
'''
def set_dialog(dialog, responses=['Next'], show=False):
    # Set the new dialog
    action('ClearDialog()')
    action('SetDialog(\"'+dialog+'\")')

    # Show dialogue if first interaction
    if show:
        action('ShowDialog()')

    # Return selected response
    return wait_for_response(responses)

'''
Purpose: Only moves on from dialogue if the player selected an available response
Inputs: acceptable responses
Outputs: Selected dialogue response
'''
def wait_for_response(responses):
    response_list = []

    # Populate the list of acceptable responses
    for response in responses:
        response_list.append('input Selected ' + response)

    # Remove white space
    received = input().strip()

    # Wait for acceptable response
    while not received in response_list:
        received = input().strip()
    return received

'''
Purpose: Handles dialogue for castle scene, pre queen death
Inputs: person being talked to
Outputs: None
'''
def castle_predeath(person):
    if person == 'Maester Purcell':
        set_dialog('Oh, who do we have here? The Queen\'s assistant you say? Well, the Queen and I may not agree on everything' +
        ' but you seem like a fine young gentleman. \\n[Next| Thanks who are you again?]')
        set_dialog('I\'m not that important. I\'m just the Kingdom\'s Grand Maester. Mainly just an advisory role, but' +
        ' I plan on retiring at the end of the year...err...who are you again? \\n[Next| ...The Queen\'s Assistant]')
        set_dialog('Right the castle chef. *The maester gets a glassy look and stares off in the distance* \\n[Next| Goodbye]')
    elif person == 'Guard Gallant':
        set_dialog('Grrr... \\n[Next| I\'ll be on my way.]')
    elif person == 'Queen Margerie':
        set_dialog('Isn\'t my husband so sweet! He did all of this for me! \\n[Next| He sure is]')
    elif person == 'Witch Carlita':
        set_dialog('How can I help you? \\n[Next| Can you teach me how to cast spells?]')
        set_dialog("Unfortunately, that takes year of training. Maybe some other time \\n[Next| Darn]")
    elif person == 'Tiana':
        received = set_dialog('I don\'t know why King Phillip went through all this trouble for Margerie. She\'s hardly' + 
        ' worth it \\n[One| Why are you so upset?] \\n[Two| You should appreciate Margerie more]', ['One', 'Two'])
        if received == 'input Selected One':
            set_dialog('You would understand if you grew up with her \\n[Next| I\'m sure]')
        else:
            set_dialog('I\'m sure she\'ll she appreciate what she\'s got coming to her \\n[Next| ...okay]')
    elif person == 'King Phillip':
        set_dialog('Isn\'t Margerie lovely. I would be devastated if anything were to happen to her \\n[Next| You really out did yourself]')

'''
Purpose: Handles dialogue for castle scene, post queen death
Inputs: person being talked to
Outputs: None
'''
def castle_postdeath(person):
    if person == 'King Phillip':
        action('PlaySound(Cry2)')
        set_dialog('My Margerie...what has happened to you! Please find out what has happened. \\n[Next| I\'m so sorry Phillip, let me look around]')
    if person == 'Tiana':
        set_dialog('I mean I never preferred my sister, but I would never have wished this upon her. \\n[Next| Why exactly did you two not get along?]')
        set_dialog('Father always favored her since she was in line for the throne. But again, I would never kill her because of it. \\n[Next| I think the whole kingdom will feel the gravity of this loss]')
    if person == 'Maester Purcell':
        set_dialog('Margerie was never supposed to go before this old coot. Whoever did this has pure malice in their heart. \\n[Next| We will bring them to justice]')
    if person == 'Noble Jeremy' or person == 'Noble Cecilia' or person == 'Merchant Bert':
        set_dialog('Oh how horrible! \\n[Next| Did you see anything?]')
        set_dialog('I\'m sorry I didn\'t see anything. \\n[Next| Okay let me know if you think of anything]')
    if person == 'Chamber Maid Scarlet':
        set_dialog('How can I help? \\n[Next| You served the drink did you notice anything unusual?]')
        set_dialog('No, I poured the wine straight out of the bottle when I was setting up earlier. Everyone\'s cups were filled from the same bottle. \\n[Next| Where did you get the wine?]')
        set_dialog('Where we always get it, the local tavern. \\n[Next| Where was the taste tester?]')
        set_dialog('Errrm....I think he was off today because of the Queen\'s birthday \\n[Next| Thanks for your time]')

'''
Purpose: Handles dialogue for dungeon scene
Inputs: person being talked to
Outputs: None
'''
def dungeon_convo(person):
    if person == 'Guard Lyra':
        action('SetExpression(Guard Lyra, surprised)')
        received = set_dialog('Wait, how did you open the cell... \\n[Attack | I need to escape, for the King! (Attack)] \\n[Talk | Listen, the King told me to escape. (Persuade)]', ['Attack', 'Talk'], True)
        if received == 'input Selected Talk':
            action('SetExpression(Guard Lyra, angry)')
            received = set_dialog('You expect me to believe that? I\'m calling the other guards. \\n[Attack | I can\'t let you do that! (Attack)] \\n[Show | I have a letter from the King! (Persuade)]', ['Attack', 'Show'])
            if received == 'input Selected Show':
                action('SetExpression(Guard Lyra, neutral)')
                set_dialog('That has the King\'s official seal on it... Fine, I\'ll let you go, but get out of here before I change my mind. \\n[Next | Next]')
                global_game_states.dungeon_guard_lives = True
        action('HideDialog()')

'''
Purpose: Handles dialogue for city scene
Inputs: person being talked to
Outputs: None
'''
def city_convo(person):
    if person == 'Beggar Adeline':
        set_dialog('I\'m not sad about the Queen\'s death. She\'s been rolling in wealth while decent folks can\'t even find a job to support their families. \\n[Next | ... okay?]')
        set_dialog('In fact, I saw the chamber maid havin\' to take extra work from some older man just to make ends meet. The royal family\'s own servant, scrappin\' by. The nerve! \\n[Next | An older man you say?]')
        add_clue('Chamber Maid Scarlet was seen taking work from an older gentleman', 'Desperate Times')
        global_game_states.scarlet_working_extra_hard = True
    elif person == 'Beggar Miles':
        if not global_game_states.wearing_disguise:
            if global_game_states.found_poison:
                received = set_dialog('Did you get that purple bottle there from some rich fella, too? \\n[Inquire | What did you say?] \\n[Next | I don\'t have time for this]', ['Inquire', 'Next'])
                if received == 'input Selected Inquire':
                    received = set_dialog('Poor Chamber Maid Scarlet got one of those from Princess Tiana. Must\'ve driven her mad. I\'d get rid of that if I were you, Scarlet hasn\'t been the same since then. \\n[Inquire | Did you hear why Tiana gave it to her?] \\n[Next | I don\'t have time for this]', ['Inquire', 'Next'])
                    if received == 'input Selected Inquire':
                        received = set_dialog('Them castle folk don\'t think beggars have ears, but I did hear her mumble something about Grand Maester Purcell. Probably experimentin\' on the unfortunate. Maybe they\'re trying to help us, though. \\n[Next | That is way too optimistic to be true]')
                        add_clue('Princess Tiana and Grand Maester Purcell have been buying rat poison', 'Beggar Miles Testimonial')
            else:
                set_dialog('A fellow citizen, down on his luck. All I can offer is camaraderie. \\n[Next | Thanks, it\'s been a rough day]')
                set_dialog('It always is, but we keep on fighting. One day it\'ll get better, I\'m sure. \\n[Next | That\'s rather optimistic]')
                set_dialog('Sometimes that\'s all we got. \\n[Next | (Leave)]')
        else:
            set_dialog('Spare some change for an old man? \\n[Next | Sorry, I\'m broke]')
    elif person == 'Scout Joanna':
        set_dialog('You don\'t want to go this way. Once outside the town, you\'re on your own. \\n[Next | Thanks!]')
    elif person == 'Alchemist Jeremy':
        set_dialog('Step inside for all your alchemy needs. Whether it\'s a nice polish for your shoes or a draught for your pain, we\'ve got it here! \\n[Next | I\'ll keep that in mind]')
    elif person == 'Scout Tom':
        set_dialog('You don\'t want to go this way. Once outside the town, you\'re on your own. \\n[Next | Thanks!]')
    elif person == 'Drunk Devon':
        set_dialog('My name is Devon. This here is the Tavern, a good place to hear the comings and goings of the town. \\n[Next | Thanks!]')
    elif person == 'Priestess Esmerelda':
        set_dialog('The witches must burn! It is no surprise the Queen is dead given the monarchy\'s flagrant disrespect of the sacred texts and ancient traditions. \\n[Next | err... ok]')
        add_clue('The Priestess seems to have strong feelings about killing the Queen.', 'A Possible Smiting')
    elif person == 'Blind Bandit':
        if global_game_states.blind_bandit_offended == False:
            if global_game_states.wearing_disguise == True:
                set_dialog('I had heard a rumour last fortnight about a contract killing of the Queen, but I didn\'t believe it until now. \\n[Next | ... Interesting]')
                add_clue('The Blind Bandit mentioned there may be more than one person involved', 'A Contract Killing')
                global_game_states.blind_bandit_clue_aquired = True
            else:
                recieved = set_dialog('What are you doing dressed up in rags, begging for money or looking for work? \\n[Begging | Could you spare some change?] \\n[Work | Looking for work.] \\n[Investigate | Neither, I\'m actually investigating the Queen\'s death. Would you happen to know anything?]' , ['Begging', 'Work', 'Investigate'], True)
                if recieved == 'input Selected Begging':
                    set_dialog('Beggars. Always looking for coin, never willing to do the job. \\n[Next | Fine]')
                elif recieved == 'input Selected Work':
                    recieved = set_dialog('You think you got what it takes to be in my line of work? \\n[Yes | Just made it out of prison for murder] \\n[No | I won\'t break the law]', ['Yes', 'No'], False)
                    if recieved == 'input Selected Yes':
                        add_clue('The Blind Bandit mentioned there may be more than one person involved', 'A Contract Killing')
                        global_game_states.blind_bandit_clue_aquired = True
                        recieved = set_dialog('Wait... are you the one that took that assassination job? Look, I don\'t want anything to do with you, regicide ain\'t in my playbook. But I\'m not gonna leave you out to dry. Need a disguise? \\n[Yes | Thanks, I\'ll remember you] \\n[No | I don\'t need your help] \\n[More | Can\'t you do more?]', ['Yes', 'No', 'More'], False)
                        if recieved == 'input Selected Yes':
                            set_dialog('Don\'t even think about remembering me. I\'m just a nobody. Take these clothes. \\n[Next | (Change into a disguise)]')
                            action('FadeOut')
                            action('HideDialog()')
                            global_game_states.wearing_disguise = True
                            action('SetClothing(John, Bandit)')
                            action('FadeIn()')
                        elif recieved == 'input Selected No':
                            global_game_states.blind_bandit_offended = True
                            set_dialog('Fine, be that way. But we are done speaking, I ain\'t going down with you. \\n[Next | (Blind Bandit seems unwilling to speak further)]')
                        elif recieved == 'input Selected More':
                            global_game_states.blind_bandit_offended = True
                            set_dialog('I\'m already risking execution, and you ask for more? We\'re done, come back here and I\'ll take you out myself! \\n[Next | (Blind Bandit seems unwilling to speak further)]')
                    elif recieved == 'input Selected No':
                        set_dialog('Yeah, I didn\'t think so. Come back when you\'re serious. \\n[Next | Maybe]')
                elif recieved == 'input Selected Investigate':
                    global_game_states.blind_bandit_offended = True
                    set_dialog('I ain\'t done nothing wrong, you better walk away before things get ugly. \\n[Next | ok]')
        else:
            set_dialog('You better walk away right now. \\n[Next | I\'m going]')
        action('EnableInput()')
    elif person == 'Gossiping Gail':
        received = set_dialog('I know everything going on in this town. Go ahead, ask me. \\n[HumorHer | Ok, what\'s the news?] \\n[Next | I\'d rather not.]', ['HumorHer', 'Next'])
        if received == 'input Selected HumorHer':
            received = set_dialog('That Blind Bandit is a walking contradiction. She is not blind, and she is so much more sweet than she lets on. Hardly a criminal at all. \\n[HumorHer | Anything else?] \\n[Next | That\'s enough]', ['HumorHer', 'Next'])
            if received == 'input Selected HumorHer':
                received = set_dialog('Alchemist Henry has been looking for an easy break for years. Can\'t turn lead to gold, but he sure does turn time into thin air. \\n[HumorHer | Anything else?] \\n[Next | That\'s enough]', ['HumorHer', 'Next'])
                if received == 'input Selected HumorHer':
                    received = set_dialog('Drunk Devon has been sober for years, no clue why he doesn\'t just fix his name. Dunce Devon would be MUCH more appropriate (laughs). \\n[HumorHer | Anything else?] \\n[Next | That\'s enough]', ['HumorHer', 'Next'])
                    if received == 'input Selected HumorHer':
                        received = set_dialog('The beggars of this town can never seem to catch a break. No one takes pity on \'em anymore, and I think a few of them are starvin\'. I can\'t afford to part with any food though, my children need it. \\n[HumorHer | Anything else?] \\n[Next | That\'s enough]', ['HumorHer', 'Next'])
                        if received == 'input Selected HumorHer':
                            received = set_dialog('Princess Tiana could never find her way out of broom closet, she\'s as dumb as a sack of hammers. Doesn\'t make her any less nasty though. \\n[HumorHer | Anything else?] \\n[Next | That\'s enough]', ['HumorHer', 'Next'])
                            if received == 'input Selected HumorHer':
                                received = set_dialog('Princess Tiana has been forced to learn under Maester Purcell ever since her father caught her in some nasty business. I\'m sure that kind old man will fix the meanness within her. \\n[HumorHer | Anything else?] \\n[Next | That\'s enough]', ['HumorHer', 'Next'])
                                if received == 'input Selected HumorHer':
                                    received = set_dialog('Princess Tiana can\'t even leave the castle without Master Purcell\'s permission. Wonder how he keeps track of her now that his mind is goin\'. A tragic loss, that. \\n[HumorHer | Anything else?] \\n[Next | That\'s enough]', ['HumorHer', 'Next'])
                                    add_clue('Grand Maester Purcell has tutored a troubled Princess Tiana for decades', 'Testimonial Gossip')

'''
Purpose: Handles dialogue for alchemist shop scene
Inputs: person being talked to
Outputs: None
'''
def alchemist_shop_convo(person):
    player_response = 'input Selected Menu'
    if person == 'Alchemist Henry':
        if global_game_states.blind_bandit_clue_aquired and (not global_game_states.alchemist_is_paranoid):
            player_response = set_dialog('Welcome! \\n[Menu | I had a few questions about the store...] \\n[Conspire | I may have overheard that a group of people conspired to kill the Queen] \\n[Next | Still looking around]', ['Menu', 'Conspire', 'Next'])
        if player_response == 'input Selected Menu':
            if global_game_states.found_poison_purchase == True:
                if global_game_states.found_poison == False:
                    if global_game_states.identified_poison == False:
                        player_response = set_dialog('Find anything you like? \\n[Purchase | Who is Tianna?] \\n[Next | Still looking around]', ['Purchase', 'Next'])
                    else:
                        player_response = set_dialog('Find anything you like? \\n[Purchase | Who is Tianna?] \\n[About | About that rat poison...] \\n[Next | Still looking around]', ['Purchase', 'About', 'Next'])
                else:
                    if global_game_states.identified_poison == False:
                        player_response = set_dialog('Need help with anything else? \\n[Purchase | Who is Tianna?] \\n[Free | Are you sure I can have this?] \\n[Next | No, thanks]', ['Purchase', 'Free', 'Next'])
                    else:
                        player_response = set_dialog('Need help with anything else? \\n[Purchase | Who is Tianna?] \\n[Free | Are you sure I can have this?] \\n[About | About that rat poison...] \\n[Next | No, thanks]', ['Purchase', 'Free', 'About', 'Next'])
            else:
                if global_game_states.found_poison == False:
                    if global_game_states.identified_poison == False:
                        player_response = set_dialog('Feel free to look around. \\n[Next | Thanks]')
                    else:
                        player_response = set_dialog('Find anything you like? \\n[About | About that rat poison...] \\n[Next | Still looking around]', ['About', 'Next'])
                else:
                    if global_game_states.identified_poison == False:
                        player_response = set_dialog('Need help with anything else? \\n[Free | Are you sure I can have this?] \\n[Next | No, thanks]', ['Free', 'Next'])
                    else:
                        player_response = set_dialog('Need help with anything else? \\n[Free | Are you sure I can have this?] \\n[About | About that rat poison...] \\n[Next| No, thanks]', ['About','Next'])
        elif player_response == 'input Selected Conspire':
            player_response = set_dialog('Did you? I-I-I wouldn\'t know anything about that. A travesty, yes. Her death was a travesty. \\n[DirectLie | I know you poisoned the Queen (lie)] \\n[DirectTruth | I know you poisoned the Queen] \\n[Indirect | I heard an alchemist brewed the Queen\'s last drink] \\n[Relent | I guess so]', ['DirectLie', 'DirectTruth', 'Indirect', 'Relent'])
            if player_response == 'input Selected DirectLie':
                set_dialog('Please, I didn\'t mean to! I only... I only sold the poison! I thought they were going to kill rats with it! You gotta believe me! \\n[Next | We\'ll see about that]')
                add_clue('The Alchemist confessed to selling poison to the murderers', 'Alchemist Testimonial')
                global_game_states.alchemist_is_paranoid = True
            elif player_response == 'input Selected DirectTruth':
                set_dialog('You know no such thing! I should call the guard on you, but you are lucky I feel generous today! \\n[Next | We\'ll see about that]')
                add_clue('The Alchemist became very defensive about the death of the Queen, but did not seem to want guards involved', 'Alchemist Testimonial')
                global_game_states.alchemist_is_paranoid = True
            elif player_response == 'input Selected Indirect':
                set_dialog('I see how it is. I will say only this. An alchemist brewing a Queen\'s drink would be very unlikely. However, someone the Queen trusted could gain access to the Queen\'s cup after it had been prepared and no one would think to check the contents. \\n[Next | We\'ll see about that]')
                add_clue('The Alchemist claimed innocence and blamed a mysterious trusted advisor of the Queen', 'Alchemist Testimonial')
                global_game_states.alchemist_is_paranoid = True
        if player_response == 'input Selected Purchase':
            player_response = set_dialog('Oh, Tianna? She\'s the Queen\'s sister. She recently bought some giant rat poison to help clear the sewers. \\n[Menu| Thanks]', ['Menu'])
        elif player_response == 'input Selected Free':
            player_response = set_dialog('If you\'re investigating for the king, take it! Quickly now! \\n[Menu| Okay...]', ['Menu'])
        elif player_response == 'input Selected About' and global_game_states.found_poison == False:
            player_response = set_dialog('Oh, the giant rat poison? I usually don\'t sell it to civilians. \\n[About2 | The king asked me]', ['About2'])
            if player_response == 'input Selected About2':
                player_response = set_dialog('You\'re investigating for the king? Take the display bottle. It\'s one of the purple ones, with a skull and crossbones. \\n[Menu | Thanks]', ['Menu'])
                action('EnableIcon(TakeLeft, hand, Poison, Take Giant Rat Poison, false)')
                add_clue('Giant rat poison was sold by Alchemist Henry', 'Found Poison')
                global_game_states.found_poison = True
        elif player_response == 'input Selected About' and global_game_states.found_poison == True:
            player_response = set_dialog('The giant rat poison? Didn\'t you already grab it? \\n[Menu | Yeah...]', ['Menu'])
        action('HideDialog()')

'''
Purpose: Handles dialogue for tavern scene
Inputs: person being talked to
Outputs: None
'''
def tavern_convo(person):
    if global_game_states.wearing_disguise:
        if person == 'Maester Purcell':
            received = set_dialog('Oh! Where am I? Oh that\'s right, the tavern. I really should be going. Who are you again? *The maester gets a glassy look and stares off in the distance* \\n[Next | erm... ok?]')
            if global_game_states.maester_purcell_senile and global_game_states.scarlet_working_extra_hard:
                while received != 'input Selected Leave':
                    received = set_dialog('*The maester continues staring off towards nothing* \\n[Stare | *Stare directly at the maester*] \\n[Leave | Whatever]', ['Stare', 'Leave'])
                    if received == 'input Selected Stare':
                        received = set_dialog('*Yet more staring occurs* \\n[Stare | *Continue to stare directly at the maester*] \\n[Leave | Whatever]', ['Stare', 'Leave'])
                        if received == 'input Selected Stare':
                            global_game_states.staring_contest_with_purcell += 1
                            if global_game_states.staring_contest_with_purcell > 4:
                                received = set_dialog('Oh, what do you want? Can\'t you see I am very intentionally ignoring you, fool? I have important work to do in the absence of that pretender Queen. Can\'t an old man enjoy a retirement well earned? \\n[Leave | You don\'t seem that senile...]', ['Leave'])
                                add_clue('Grand Maester Purcell spoke very poorly of the Queen, and very fondly of a job he recently performed', 'Much Smarter than he Looks')
            global_game_states.staring_contest_with_purcell = 0
        elif person == 'Witch Carlita':
            set_dialog('That Maester Purcell sure acts like a fool, but he\'s sharp as a tack. Don\'t let him fool you \\n[Leave | Hmmm that\'s interesting]', ['Leave'])
            add_clue('Witch Carlita mentioned that Maester Purcell is not as senile as he acts.', 'Purcell Senile')
            global_game_states.maester_purcell_senile = True
        elif person == 'Noble Jeremy':
            set_dialog('This murder is the most interesting thing to happen in years. Remember back when the Queen\'s Uncle got his leg eaten by that bear? Now that was a story. \\n[Next| ...Fascinating.]')
        elif person == 'Noble Cecilia':
            received = set_dialog('Tiana has always been jealous of her sister. \\n[Continue | What does that have to do with anything?] \\n[Leave | Ok]', ['Continue', 'Leave'])
            if received == 'input Selected Continue':
                set_dialog('I\'m just saying Tiana has always wanted the crown ever since she was a child \\n[Next | Thanks]')
                add_clue('Noblewoman Cecilia mentioned that Tiana has always envied the crown', 'Tiana Jealous')
                global_game_states.cecilia_accusations = True
        elif person == 'Merchant Bert':
            set_dialog('I sold the Alchemist a whole cart-load of ingredients last week, some of them were poisons. If you want to look for clues, I\'d start with the Alchemist shop \\n[Next| Thanks, I\'ll do that.]')
        elif person == 'Chamber Maid Scarlet':
            if global_game_states.found_poison and global_game_states.chamber_maid_odd_behaviours:
                received = set_dialog('*Scarlet sits silently trembling, fumbling for words* \\n[Poison | Do you know what this is? (Show Poison)] \\n[Next | ...]', ['Poison', 'Next'])
                if received == 'input Selected Poison':
                    set_dialog('No... No, No! I only did what I was told! Tianna... Queen Tianna... She would never lie! \\n[Next | ...]')
                    add_clue('Chamber Maid Scarlet panicked at the mention of giant rat poison, and mumbled the name Tianna', 'Chamber Maid Testimonial')
            else:
                set_dialog('*Scarlet sits silently trembling, fumbling for words* \\n[Next | ...]')
                add_clue('Scarlet the chamber maid was acting odd and unable to speak in the tavern', 'Chamber Maid Distressed')
                global_game_states.chamber_maid_odd_behaviours = True
        elif person == 'Tiana':
            if global_game_states.cecilia_accusations:
                received = set_dialog('I told you to stop bothering me, or else I\'ll call the guards! I am the Queen now! \\n[Accusatory | A dead sister has some perks, doesn\'t it?] \\n[Sly | I loved it when my older sibiling... passed. I inherited all the land] \\n[Leave | Alright, my bad]', ['Accusatory', 'Sly', 'Leave'])
                if received == 'input Selected Accusatory':
                    set_dialog('I should have you killed for such insolence! Guards! Where are my guards? ...If my guards show up I\'ll have you jailed. Get lost. \\n[Next | I should be going]')
                elif received == 'input Selected Sly':
                    set_dialog('Yes, the world has a way of working out for those who deserve it, doesn\'t it? My sister never earned the crown, but I have. \\n[Next | Indeed]')
                    add_clue('Tianna appears to be proud of the Queen\'s death', 'Sinister Sister')
            else:
                set_dialog('Why do you speak to me?! Can\'t you see I\'m distraught?! \\n[Next | ...]')
        elif person == 'Bartender Bill':
            received = set_dialog('My name is Bill the Bartender. what can I get you? \\n[Investigate | I\'m looking into the Queen\'s murder] \\n[Reveal | It\'s me Bill. Your old friend John. (Reveal Identity)]', ['Investigate','Reveal'])
            if received == 'input Selected Investigate':
                set_dialog('Well feel free to talk to the people here. Alcohol has a way of loosening people\'s lips. \\n[Next | You\'re not wrong]')
            elif received == 'input Selected Reveal':
                set_dialog('John! Well now this puts me in a tricky spot. You\'ve always been a good friend to me. I can help you get out of the kingdom if you\'d like \\n[Decline | No, I can prove my innocence] \\n[Accept | I\'ll take your offer.', ['Decline','Accept'])
    else:
        if person == 'Bartender Bill':
            set_dialog('John! What are you doing here! We gotta get you out of those prison clothes. Go see the Blind Bandit out back, I\'ll bet she can help you before the guards get here. \\n[Decline | No, I don\'t need to hide] \\n[Accept | I\'ll go talk to the Blind Bandit', ['Decline','Accept'])
        else:
            set_dialog('The murderer is here! Somebody call for the guards. HELP!!! \\n[Flee | No! Wait! (I should really find a disguise)]', ['Flee'])