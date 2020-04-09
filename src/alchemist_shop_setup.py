from action import action

def alchemist_shop_setup():
	action('CreatePlace(Alch, AlchemyShop)')
	

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
	action('EnableIcon(Inspect, magnifyingglass, BluePotion1, Read Label, true)')
	action('EnableIcon(Inspect, magnifyingglass, BluePotion2, Read Label, true)')
	action('EnableIcon(Inspect, magnifyingglass, GreenPotion1, Read Label, true)')
	action('EnableIcon(Inspect, magnifyingglass, GreenPotion2, Read Label, true)')
	action('EnableIcon(Inspect, magnifyingglass, GreenPotion3, Read Label, true)')
	action('EnableIcon(Inspect, magnifyingglass, Poison, Read Label, true)')
	action('EnableIcon(Drink, drink, Poison, Drink Deadly Poison, false')
	action('EnableIcon(Inspect, magnifyingglass, PurplePotion1, Read Label, true)')
	action('EnableIcon(Inspect, magnifyingglass, RedPotion1, Read Label, true)')
	action('EnableIcon(Inspect, magnifyingglass, RedPotion2, Read Label, true)')
	action('EnableIcon(Inspect, magnifyingglass, Skull1, Inspect Skull, true')
	action('EnableIcon(Inspect, magnifyingglass, Skull2, Inspect Skull, true')
	action('EnableIcon(Inspect, bookshelf, Alch.RightBookcase, Browse, true)')
	action('EnableIcon(Inspect, bookshelf, Alch.LeftBookcase, Browse, true)')
	action('EnableIcon(Inspect, cauldron, Alch.Cauldron, Inspect, true)')

	action('EnableIcon(Talk, talk, Alchemist Henry, Talk to Alchemist Henry, true)')
	#action('EnableIcon(TakeLeft, hand, Poison, Take Giant Rat Poison, false)')
	action('EnableIcon(Leave, door, Alch.Door, Leave, true)')
	action('EnableIcon(Leave, door, Alch.Chest, Leave, true)')