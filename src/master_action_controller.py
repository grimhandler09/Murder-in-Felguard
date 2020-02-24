from action import action

def talk_action(person):
    action('SetLeft(John)')
    action('SetRight(' + person + ')')
    if person == "Queen Margerie":
        command = 'SetDialog(What do you want? [Nothing | Nothing])'
    action(command)
    action('ShowDialog()')

#Send sit command with the place as the parameter
def sit_action(place):
    command = "Sit(John, " + place + ")"
    action(command)

def check_master_actions(received):
    if(received.startswith('input Sit')):
        received = received.split(' ')
        place = received[len(received) - 1]
        sit_action(place)
    elif(received.startswith('input Talk')):
        received = received.split(' ')
        person = received[len(received) - 1]
        talk_action(person)
    elif(received == "input Close Narration"):
        action("HideNarration()")
