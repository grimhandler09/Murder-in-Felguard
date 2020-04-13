'''
Authors: Zach Moore, Travis Conley, Adrian Wyllie, Mitchel Dennis
Purpose: Handles actions that should be playable if the player is located within the alchemist shop scene
'''

import time
from action import action
from master_action_controller import *
import global_game_states
from threading import Timer
from talk_controller import *
from add_clue import add_clue
from alchemist_shop_setup import alchemist_shop_setup

'''
Purpose: Assigns narration and dialog trees to inspectable items
Inputs: item - The item the player selects
Outputs: None
'''
def inspect_item(item):
	action('DisableInput()')
	action('WalkTo(John, ' + item + ')')
	action('Face(John, ' + item + ')')
	action('EnableInput()')

	#Potions
	if item == 'BluePotion1':
		#BluePotion1 = aqua regia
		midscene_narration('The label reads - Aqua Regia')
		action('PlaySound(Unlock, BluePotion1, false')
	elif item == 'BluePotion2':
		#BluePotion2 = aqua fortis
		midscene_narration('The label reads - Aqua Fortis')
		action('PlaySound(Unlock, BluePotion2, false')
	elif item == 'GreenPotion1':
		#GreenPotion1 = Strength Potion
		midscene_narration('The label reads - Strength Potion')
		action('PlaySound(Unlock, GreenPotion1, false')
	elif item == 'GreenPotion2':
		#GreenPotion2 = Speed Potion
		midscene_narration('The label reads - Speed Potion')
		action('PlaySound(Unlock, GreenPotion2, false')
	elif item == 'GreenPotion3':
		#GreenPotion3 = Night Vision Potion
		midscene_narration('The label reads - Night Vision Potion')
		action('PlaySound(Unlock, GreenPotion3, false')
	elif item == 'Poison':
		#Poison = Giant Rat Poison
		midscene_narration('The label is marked with a skull and crossbones')
		action('PlaySound(Unlock, Poison, false')
	elif item == 'PurplePotion1':
		#PurplePotion1 is Withering Potion
		midscene_narration('The label reads - Withering Potion')
		action('PlaySound(Unlock, PurplePotion1, false')
	elif item == 'RedPotion1':
		#RedPotion1 is Health Potion
		midscene_narration('The label reads - Health Potion')
		action('PlaySound(Unlock, RedPotion1, false')
	elif item == 'RedPotion2':
		#RedPotion2 is Food Potion
		midscene_narration('The label reads - Food Potion')
		action('PlaySound(Unlock, RedPotion2, false')

	#Skulls
	elif item == 'Skull1':
		midscene_narration('The skull is a cheap fake. \'Alchemist Henry\' is inscribed on the bottom.')
	elif item == 'Skull2':
		midscene_narration('From a distance it looks real, but up close it\'s obvious that it\'s made of paper')
	
	elif item == 'Alch.RightBookcase':
		#RightBookcase has potion descriptions
		set_left_right('John', 'null')
		action('ShowDialog()')
		action('PlaySound(Book, Alch.RightBookcase, false')
		player_response = 'input Selected AllPotionsList'
		while player_response != 'input Selected Done':
			if player_response == 'input Selected AllPotionsList':
				player_response = set_dialog('There is a book sticking out of the bookcase. Which part do you want to read? \\n[BluePotions | Blue Potions] \\n[GreenPotions | Green Potions] \\n[PurplePotions | Purple Potions] \\n[RedPotions | Red Potions] \\n[Done | Put it back]', ['BluePotions', 'GreenPotions', 'PurplePotions', 'RedPotions', 'Done'])
		#Blue Potions
			elif player_response == 'input Selected BluePotions':
				while player_response != 'input Selected AllPotionsList':
					player_response = set_dialog('We offer two blue potions: Aqua Regia and Aqua Fortis. \\n[Blue1 | Aqua Regia] \\n[Blue2 | Aqua Fortis] \\n[AllPotionsList | Back]', ['Blue1', 'Blue2', 'AllPotionsList'])
					if player_response == 'input Selected Blue1':
						player_response = set_dialog('Aqua Regia: Can disolve gold. Also known as nitrohydrochloric acid. \\n[Back | Back]', ['Back'])
					elif player_response == 'input Selected Blue2':
						player_response = set_dialog('Aqua Fortis: Also known as Fuming Nitric Acid. Creates toxic fumes. \\n[Back | Back]', ['Back'])
		#Green Potions
			elif player_response == 'input Selected GreenPotions':
				while player_response != 'input Selected AllPotionsList':
					player_response = set_dialog('We offer three green potions: Strength Potions, Speed Potions, and Night Vision Potions. \\n[Green1 | Strength Potions] \\n[Green2 | Speed Potions] \\n[Green3 | Night Vision Potions] \\n[AllPotionsList | Back]', ['Green1', 'Green2', 'Green3', 'AllPotionsList'])
					if player_response == 'input Selected Green1':
						player_response = set_dialog('Strength Potion: Lift a thousand pounds! \\n[Back | Back]', ['Back'])
					elif player_response == 'input Selected Green2':
						player_response = set_dialog('Speed Potion: Run faster than a horse! \\n[Back | Back]', ['Back'])
					elif player_response == 'input Selected Green3':
						player_response = set_dialog('Night Vision Potion: See at night like it\'s day! Warning: looking at bright lights may cause blindness. \\n[Back | Back]', ['Back'])
		#Purple Potions
			elif player_response == 'input Selected PurplePotions':
				while player_response != 'input Selected AllPotionsList':
					player_response = set_dialog('We offer two purple potions: Giant Rat Poison and Withering Potions. \\n[Purple1| Giant Rat Poison] \\n[Purple2| Withering Potion] \\n[AllPotionsList | Back]', ['Purple1','Purple2','AllPotionsList'])
					if player_response == 'input Selected Purple1':
						player_response = set_dialog('Giant Rat Poison keeps our sewers clean! Warning: Highly Toxic. \\n[Back | Back]', ['Back'])
						global_game_states.identified_poison = True
					elif player_response == 'input Selected Purple2':
						player_response = set_dialog('Withering Potion: Kills weeds fast! Safe in small or moderate amounts! \\n[Back | Back]', ['Back'])
		#Red Potions
			elif player_response == 'input Selected RedPotions':
				while player_response != 'input Selected AllPotionsList':
					player_response = set_dialog('We offer two red potions: Health Potions and Food Potions. \\n[Red1| Health Potion] \\n[Red2| Food Potion] \\n[AllPotionsList | Back]', ['Red1','Red2','AllPotionsList'])
					if player_response == 'input Selected Red1':
						player_response = set_dialog('Health Potion: it\'s the best health pot around! \\n[Back | Back]', ['Back'])
					elif player_response == 'input Selected Red2':
						player_response = set_dialog('Food Potion: Add to food to make it fantastic! \\n[Back | Back]', ['Back'])
		action('HideDialog()')
		action('PlaySound(Book, Alch.RightBookcase, false')
	
	elif item == 'Alch.LeftBookcase':
		#LeftBookcase = sales ledger
		action('PlaySound(Book, Alch.LeftBookcase, false')
		set_left_right('John', 'null')
		action('ShowDialog()')
		player_response = 'input Selected AllPotionsList'
		while player_response != 'input Selected Done':
			if player_response == 'input Selected AllPotionsList':
				player_response = set_dialog('There is a book sticking out of the bookcase. Which part do you want to read? \\n[First| First Page] \\n[Second| Second Page] \\n[Third| Third Page] \\n[Done | Put it back]', ['First', 'Second', 'Third', 'Done'])
			elif player_response == 'input Selected First':
				player_response = set_dialog('12x Speed Potion - Gossiping Gail. 1x Aqua Fortis - Priestess Esmerelda. \\n[AllPotionsList| Back]', ['AllPotionsList'])
			elif player_response == 'input Selected Second':
				player_response = set_dialog('2x Food Potion - Castle Chefs. 5x Withering Potion - Scout Joanna. 1x Night Vision Potion - Blind Bandit. \\n[AllPotionsList| Back]', ['AllPotionsList'])
			elif player_response == 'input Selected Third':
				player_response = set_dialog('1x Giant Rat Poison - Tiana. 3x Health Potion - Prison Guards. The rest is empty. \\n[AllPotionsList| Back]', ['AllPotionsList'])
				global_game_states.found_poison_purchase = True
				action('CreateItem(Sales Records, GreenBook)')
				add_clue('Tianna bought some rat poison', 'Sales Records')
		action('HideDialog()')
		action('PlaySound(Book, Alch.LeftBookcase, false')
	
	elif item == 'Alch.Cauldron':
		#Cauldron
		action('PlaySound(Brew, Alch.Cauldron, false)')
		midscene_narration('The cauldron is bubbling happily.')

'''
Purpose: Primary loop for the alchemist shop scene, controls which actions the player can take
Inputs: None
Outputs: None
'''
def alchemist_shop_controller():
	alchemist_shop_setup()
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
		else:
			check_master_actions(received)