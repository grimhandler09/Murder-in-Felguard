from action import action

def scene_three_setup():
	action('CreatePlace(Alch, AlchemyShop)')
	action('SetPosition(John, Alch.Door)')

	#Alchemist Henry
	action('CreateCharacter(Alchemist Henry, D)')
	action('SetClothing(Alchemist Henry, Warlock)')
	action('SetHairStyle(Alchemist Henry, Short_Full)')
	action('SetPosition(Alchemist Henry, Alch.Bar.Behind)')

	#Enable Effects
	action('EnableEffect(Alch.Fireplace, Blackflame)')
	action('EnableEffect(Alch.Cauldron, Poison)')

	#Create Items
	action('CreateItem(BluePotion1, BluePotion)')
	action('CreateItem(BluePotion2, BluePotion)')
	action('CreateItem(GreenPotion1, GreenPotion)')
	action('CreateItem(GreenPotion2, GreenPotion)')
	action('CreateItem(GreenPotion3, GreenPotion)')
	action('CreateItem(Poison, PurplePotion)')
	action('CreateItem(Skull1, Skull)')
	action('CreateItem(Skull2, Skull)')
	action('CreateItem(PurplePotion1, PurplePotion)')
	action('CreateItem(RedPotion1, RedPotion)')
	action('CreateItem(RedPotion2, RedPotion)')

	#Position Items
	action('SetPosition(BluePotion1, Alch.Bar.Center)')
	action('SetPosition(Skull1, Alch.Bar.Right)')

	action('SetPosition(Poison, Alch.Table.Left)')
	action('SetPosition(GreenPotion1, Alch.Table.FrontLeft)')
	action('SetPosition(GreenPotion2, Alch.Table.BackRight)')
	action('SetPosition(PurplePotion1, Alch.Table.BackLeft)')

	action('SetPosition(BluePotion2, Alch.AlchemistTable.Left)')
	action('SetPosition(GreenPotion3, Alch.AlchemistTable.Right)')
	action('SetPosition(Skull2, Alch.AlchemistTable.Center)')

	action('SetPosition(RedPotion1, Alch.Bookshelf.Left)')
	action('SetPosition(RedPotion2, Alch.Bookshelf.Right)')

	#Enable Icons
	action('EnableIcon(Inspect, magnifyingglass, BluePotion1, true)')
	action('EnableIcon(Inspect, magnifyingglass, BluePotion2, true)')
	action('EnableIcon(Inspect, magnifyingglass, GreenPotion1, true)')
	action('EnableIcon(Inspect, magnifyingglass, GreenPotion2, true)')
	action('EnableIcon(Inspect, magnifyingglass, GreenPotion3, true)')
	action('EnableIcon(Inspect, magnifyingglass, Poison, true)')
	action('EnableIcon(Inspect, magnifyingglass, PurplePotion1, true)')
	action('EnableIcon(Inspect, magnifyingglass, RedPotion1, true)')
	action('EnableIcon(Inspect, magnifyingglass, RedPotion2, true)')
	action('EnableIcon(Inspect, magnifyingglass, Alch.RightBookcase, false)')
	action('EnableIcon(Inspect, magnifyingglass, Alch.LeftBookcase, false))')
	action('EnableIcon(Inspect, magnifyingglass, Alch.Cauldron, false))')

	action('EnableIcon(Talk, talk, Alchemist Henry, true)')
	#action('EnableIcon(Accuse, arrest, Alchemist Henry, false)')
	#action('EnableIcon(TakeLeft, hand, Poison, false)')
	action('EnableIcon(Leave, door, Alch.Door, true)') 