from action import action 

def alchemist_shop_setup():
	action('Enter(John, Alch.Door, true)')
	action('SetCameraFocus(John)')
	action('SetCameraMode(follow)')
	action('EnableInput()')

