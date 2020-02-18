# Send a command to Camelot.
def action(command):
	print('start ' + command)
	while(True):
		i = input()
		if(i == 'succeeded ' + command):
			return True
		elif(i == 'failed ' + command):
			return False
		elif(i.startswith('error')):
			return False



# Respond to input.
def main():
    # Set up a small house with a door.
    action('CreatePlace(BobsHouse, Cottage)')
    action('CreateCharacter(Bob, B)')
    action('SetClothing(Bob, Peasant)')
    action('SetPosition(Bob, BobsHouse.Door)')
    action('EnableIcon(Open_Door, Open, BobsHouse.Door, Leave the house, true)')
    action('ShowMenu()')
    
    while(True):
        i = input()
        if(i == 'input Selected Start'):
            action('SetCameraFocus(Bob)')
            action('HideMenu()')
            action('EnableInput()')
        elif(i == 'input Open_Door BobsHouse.Door'):
            action('SetNarration(The door is locked!)')
            action('ShowNarration()')
        elif(i == 'input Close Narration'):
            action('HideNarration()')
main()