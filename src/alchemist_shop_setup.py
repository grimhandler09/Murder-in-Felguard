from action import action 

def alchemist_shop_setup():
	
	# Start Background music for alchemy shop
	action('StopSound()')
	action('PlaySound(Serenity)')
	
	action('Enter(John, Alch.Door, true)')
	action('SetCameraFocus(John)')
	action('SetCameraMode(follow)')
	action('EnableInput()')

