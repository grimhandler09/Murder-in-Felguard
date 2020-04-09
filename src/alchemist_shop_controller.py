import time
from action import action
from master_action_controller import *
import global_game_states
from threading import Timer
from talk_controller import *
from add_clue import add_clue
from alchemist_shop_setup import alchemist_shop_setup

def inspect_item(item):
	action('WalkTo(John, ' + item + ')')
	action('Face(John, ' + item + ')')
	if item == 'BluePotion1':
		#BluePotion1 = aqua regia
		action('SetNarration(The label reads - Aqua Regia)')
		action('ShowNarration()')
	#elif item == 'BluePotion2':
		#BluePotion2 = aqua fortis
		action('SetNarration(The label reads - Aqua Fortis')
		action('ShowNarration()')
	elif item == 'GreenPotion1':
		#GreenPotion1 = Strength Potion
		action('SetNarration(The label reads - Strength Potion)')
		action('ShowNarration()')
	elif item == 'GreenPotion2':
		#GreenPotion2 = Speed Potion
		action('SetNarration(The label reads - Speed Potion)')
		action('ShowNarration()')
	elif item == 'GreenPotion3':
		#GreenPotion3 = Night Vision Potion
		action('SetNarration(The label reads - Night Vision Potion)')
		action('ShowNarration()')
	elif item == 'Poison':
		#Poison = Giant Rat Poison
		action('SetNarration(The label is marked with a skull and crossbones)')
		action('ShowNarration()')
	#elif item == 'PurplePotion1':
		#PurplePotion1 = Withering Potion
		action('SetNarration(The label reads - Withering Potion)')
		action('ShowNarration()')
	elif item == 'RedPotion1':
		#RedPotion1 = Health Potion
		action('SetNarration(The label reads - Health Potion)')
		action('ShowNarration()')
	elif item == 'RedPotion2':
		#RedPotion2 = Food Potion
		action('SetNarration(The label reads - Food Potion)')
		action('ShowNarration()')
	elif item == 'Skull1':
		action('SetNarration(The skull is a cheap fake. \'Alchemist Henry\' is inscribed on the bottom.')
		action('ShowNarration()')
	elif item == 'Skull2':
		action('SetNarration(From a distance it looks real, but up close it\'s obvious that it\'s made of paper mache)')
		action('ShowNarration()')
	elif item == 'Alch.RightBookcase':
		#RightBookcase = potion descriptions
		action('SetLeft(John)')
		action('SetRight(null)')
		action('ShowDialog()')
		pr = 'input Selected Menu'
		while pr != 'input Selected Next':
			if pr == 'input Selected Menu':
				pr = set_dialog('There is a book sticking out of the bookcase. Which part do you want to read? [First| Blue Potions] [Second| Green Potions] [Third| Purple Potions] [Fourth| Red Potions] [Next| Put it back]', ['First','Second','Third','Fourth','Next'])
		#Blue Potions
			elif pr == 'input Selected First':
				pr = set_dialog('We offer two blue potions: Aqua Regia and Aqua Fortis.[Blue1| Aqua Regia] [Blue2| Aqua Fortis] [Menu| Back]',['Blue1','Blue2','Menu'])
			elif pr == 'input Selected Blue1':
				pr = set_dialog('Aqua Regia: Can disolve gold. Also known as nitrohydrochloric acid \n[First| Back]',['First'])
			elif pr == 'input Selected Blue2':
				pr = set_dialog('Aqua Fortis: Also known as Fuming Nitric Acid. Creates toxic fumes. [First| Back]',['First'])
		#Green Potions
			elif pr == 'input Selected Second':
				pr = set_dialog('We offer three green potions: Strength Potions, Speed Potions, and Night Vision Potions. [Green1| Strength Potions] [Green2| Speed Potions] [Green3| Night Vision Potions] [Menu| Back]',['Green1','Green2','Green3','Menu'])
			elif pr == 'input Selected Green1':
				pr = set_dialog('Strength Potion: Lift a thousand pounds! [Second| Back]',['Second'])
			elif pr == 'input Selected Green2':
				pr = set_dialog('Speed Potion: Run faster than a horse! [Second| Back]',['Second'])
			elif pr == 'input Selected Green3':
				pr = set_dialog('Night Vision Potion: See at night like it\'s day! Warning: looking at bright lights amy cause blindness. [Second| Back]',['Second'])
		#Purple Potions
			elif pr == 'input Selected Third':
				pr = set_dialog('We offer two purple potions: Giant Rat Poison and Withering Potions. [Purple1| Giant Rat Poison] [Purple2| Withering Potion] [Menu| Back]',['Purple1','Purple2','Menu'])
			elif pr == 'input Selected Purple1':
				pr = set_dialog('Giant Rat Poison keeps our sewers clean! Warning: Highly Toxic. [Third| Back]',['Third'])
				global_game_states.identified_poison = True
			elif pr == 'input Selected Purple2':
				pr = set_dialog('Withering Potion: Kills weeds fast! Safe in small or moderate amounts! [Third| Back]',['Third'])
		#Red Potions
			elif pr == 'input Selected Fourth':
				pr = set_dialog('We offer two red potions: Health Potions and Food Potions. [Red1| Health Potion] [Red2| Food Potion] [Menu| Back]',['Red1','Red2','Menu'])
			elif pr == 'input Selected Red1':
				pr = set_dialog('Health Potion: it\'s the best health pot around! [Fourth| Back]',['Fourth'])
			elif pr == 'input Selected Red2':
				pr = set_dialog('Food Potion: Add to food to make it fantastic! [Fourth| Back]',['Fourth'])

	elif item == 'Alch.LeftBookcase':
		#LeftBookcase = sales ledger
		action('SetLeft(John)')
		action('SetRight(null)')
		action('ShowDialog()')
		pr = 'input Selected Menu'
		while pr != 'input Selected Next':
			if pr == 'input Selected Menu':
				pr = set_dialog('There is a book sticking out of the bookcase. Which part do you want to read? [First| First Page] [Second| Second Page] [Third| Third Page] [Next| Put it back]',['First','Second','Third','Next'])
			elif pr == 'input Selected First':
				pr = set_dialog('12x Speed Potion - Gossiping Gail. 1x Aqua Fortis - Priestess Esmerelda. [Menu| Back]',['Menu'])
			elif pr == 'input Selected Second':
				pr = set_dialog('2x Food Potion - Castle Chefs. 5x Withering Potion - Scout Joanna. 1x Night Vision Potion - Blind Bandit. [Menu| Back]',['Menu'])
			elif pr == 'input Selected Third':
				pr = set_dialog('1x Giant Rat Poison - Tiana. 3x Health Potion - Prison Guards. The rest is empty. [Menu| Back]',['Menu'])
				global_game_states.found_poison_purchase = True
				add_clue('Found Tianna bought poison')
	elif item == 'Alch.Cauldron':
		#Cauldron
		action('SetNarration(The cauldron is bubbling happily.)')
		action('ShowNarration()')

def alchemist_shop_controller():
	action('Enter(John, Alch.Door, true)')
	action('SetCameraFocus(John)')
	action('SetCameraMode(follow)')
	action('EnableInput()')
	while global_game_states.current_scene == 'alchemist_shop' and global_game_states.accused == '':
		received = input()
		if received.startswith('input Inspect'):
			received = received.split(' ')
			item = received[2]
			inspect_item(item)
		elif received.startswith('input Leave'):
			action('Exit(John, ' + received[12:] + ', true)')
			global_game_states.current_scene = 'city'
			global_game_states.prev_scene = 'alchemist_shop'
		else:
			check_master_actions(received)