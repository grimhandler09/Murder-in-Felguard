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
		midscene_narration('The label reads - Aqua Regia')
	elif item == 'BluePotion2':
		#BluePotion2 = aqua fortis
		midscene_narration('The label reads - Aqua Fortis')
	elif item == 'GreenPotion1':
		#GreenPotion1 = Strength Potion
		midscene_narration('The label reads - Strength Potion')
	elif item == 'GreenPotion2':
		#GreenPotion2 = Speed Potion
		midscene_narration('The label reads - Speed Potion')
	elif item == 'GreenPotion3':
		#GreenPotion3 = Night Vision Potion
		midscene_narration('The label reads - Night Vision Potion')
	elif item == 'Poison':
		#Poison = Giant Rat Poison
		midscene_narration('The label is marked with a skull and crossbones')
	elif item == 'PurplePotion1':
		#PurplePotion1 is Withering Potion
		midscene_narration('The label reads - Withering Potion')
	elif item == 'RedPotion1':
		#RedPotion1 is Health Potion
		midscene_narration('The label reads - Health Potion')
	elif item == 'RedPotion2':
		#RedPotion2 is Food Potion
		midscene_narration('The label reads - Food Potion')
	elif item == 'Skull1':
		midscene_narration('The skull is a cheap fake. \'Alchemist Henry\' is inscribed on the bottom.')
	elif item == 'Skull2':
		midscene_narration('From a distance it looks real, but up close it\'s obvious that it\'s made of paper')
	elif item == 'Alch.RightBookcase':
		#RightBookcase has potion descriptions
		set_left_right('John', 'null')
		action('ShowDialog()')
		player_response = 'input Selected AllPotionsList'
		while player_response != 'input Selected Done':
			if player_response == 'input Selected AllPotionsList':
				player_response = set_dialog('There is a book sticking out of the bookcase. Which part do you want to read? [BluePotions | Blue Potions] [GreenPotions | Green Potions] [PurplePotions | Purple Potions] [RedPotions | Red Potions] [Done | Put it back]', ['BluePotions', 'GreenPotions', 'PurplePotions', 'RedPotions', 'Done'])
		#Blue Potions
			elif player_response == 'input Selected BluePotions':
				while player_response != 'input Selected AllPotionsList':
					player_response = set_dialog('We offer two blue potions: Aqua Regia and Aqua Fortis. [Blue1 | Aqua Regia] [Blue2 | Aqua Fortis] [AllPotionsList | Back]', ['Blue1', 'Blue2', 'AllPotionsList'])
					if player_response == 'input Selected Blue1':
						player_response = set_dialog('Aqua Regia: Can disolve gold. Also known as nitrohydrochloric acid [Back | Back]', ['Back'])
					elif player_response == 'input Selected Blue2':
						player_response = set_dialog('Aqua Fortis: Also known as Fuming Nitric Acid. Creates toxic fumes. [Back | Back]', ['Back'])
		#Green Potions
			elif player_response == 'input Selected GreenPotions':
				while player_response != 'input Selected AllPotionsList':
					player_response = set_dialog('We offer three green potions: Strength Potions, Speed Potions, and Night Vision Potions. [Green1 | Strength Potions] [Green2 | Speed Potions] [Green3 | Night Vision Potions] [AllPotionsList | Back]', ['Green1', 'Green2', 'Green3', 'AllPotionsList'])
					if player_response == 'input Selected Green1':
						player_response = set_dialog('Strength Potion: Lift a thousand pounds! [Back | Back]', ['Back'])
					elif player_response == 'input Selected Green2':
						player_response = set_dialog('Speed Potion: Run faster than a horse! [Back | Back]', ['Back'])
					elif player_response == 'input Selected Green3':
						player_response = set_dialog('Night Vision Potion: See at night like it\'s day! Warning: looking at bright lights may cause blindness. [Back | Back]', ['Back'])
		#Purple Potions
			elif player_response == 'input Selected PurplePotions':
				while player_response != 'input Selected AllPotionsList':
					player_response = set_dialog('We offer two purple potions: Giant Rat Poison and Withering Potions. [Purple1| Giant Rat Poison] [Purple2| Withering Potion] [AllPotionsList | Back]', ['Purple1','Purple2','AllPotionsList'])
					if player_response == 'input Selected Purple1':
						player_response = set_dialog('Giant Rat Poison keeps our sewers clean! Warning: Highly Toxic. [Back | Back]', ['Back'])
						global_game_states.identified_poison = True
					elif player_response == 'input Selected Purple2':
						player_response = set_dialog('Withering Potion: Kills weeds fast! Safe in small or moderate amounts! [Back | Back]', ['Back'])
		#Red Potions
			elif player_response == 'input Selected RedPotions':
				while player_response != 'input Selected AllPotionsList':
					player_response = set_dialog('We offer two red potions: Health Potions and Food Potions. [Red1| Health Potion] [Red2| Food Potion] [AllPotionsList | Back]', ['Red1','Red2','AllPotionsList'])
					if player_response == 'input Selected Red1':
						player_response = set_dialog('Health Potion: it\'s the best health pot around! [Back | Back]', ['Back'])
					elif player_response == 'input Selected Red2':
						player_response = set_dialog('Food Potion: Add to food to make it fantastic! [Back | Back]', ['Back'])
		action('HideDialog()')
	elif item == 'Alch.LeftBookcase':
		#LeftBookcase = sales ledger
		set_left_right('John', 'null')
		action('ShowDialog()')
		player_response = 'input Selected AllPotionsList'
		while player_response != 'input Selected Done':
			if player_response == 'input Selected AllPotionsList':
				player_response = set_dialog('There is a book sticking out of the bookcase. Which part do you want to read? [First| First Page] [Second| Second Page] [Third| Third Page] [Done | Put it back]', ['First', 'Second', 'Third', 'Done'])
			elif player_response == 'input Selected First':
				player_response = set_dialog('12x Speed Potion - Gossiping Gail. 1x Aqua Fortis - Priestess Esmerelda. [AllPotionsList| Back]', ['AllPotionsList'])
			elif player_response == 'input Selected Second':
				player_response = set_dialog('2x Food Potion - Castle Chefs. 5x Withering Potion - Scout Joanna. 1x Night Vision Potion - Blind Bandit. [AllPotionsList| Back]', ['AllPotionsList'])
			elif player_response == 'input Selected Third':
				player_response = set_dialog('1x Giant Rat Poison - Tiana. 3x Health Potion - Prison Guards. The rest is empty. [AllPotionsList| Back]', ['AllPotionsList'])
				global_game_states.found_poison_purchase = True
				add_clue('Tianna bought some rat poison')
		action('HideDialog()')
	elif item == 'Alch.Cauldron':
		#Cauldron
		midscene_narration('The cauldron is bubbling happily.')

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
			#action('Exit(John, ' + received[12:] + ', true)')
			global_game_states.current_scene = 'city'
			global_game_states.prev_scene = 'alchemist_shop'
			action('FadeOut()')
		else:
			check_master_actions(received)