''' 
Authors: Zach Moore, Travis Conley, Adrian Wyllie, Mitchel Dennis
Purpose: Performs a lot of Camelot calls to setup a majority of the game.
'''
from action import action
from castle_setup import castle_setup

def all_game_setup():
    action('SetTitle(\"Murder in Felguard\")')
    action("SetCredits(\"Experience Manager by Zach Moore, Travis Conley, Adrian Wyllie, Mitchel Dennis\")")

    # Create Game Locations
    action('CreatePlace(QueensCastle, DiningRoom)')
    action('CreatePlace(Prison, Dungeon)')
    action('CreatePlace(City, City)')
    action('CreatePlace(Gallows, Ruins)')
    action('CreatePlace(Alch, AlchemyShop)')
    action('CreatePlace(Tavern, Tavern)')
    action('CreatePlace(CastleStorage, Storage)')
    
    ###############################################################
    # Castle                                                      #
    ###############################################################
    
    # Create Characters

    # Main Character(John)
    action('CreateCharacter(John, B)')
    action('SetHairStyle(John, Long)')
    action('SetEyeColor(John, blue)')
    
    # Queen Margerie
    action('CreateCharacter(Queen Margerie, A)')
    action('SetClothing(Queen Margerie, Queen)')
    action('SetHairStyle(Queen Margerie, Long)')
    action('SetEyeColor(Queen Margerie, green)')
    
    # Guard Gallant
    action('CreateCharacter(Guard Gallant, F)')
    action('SetClothing(Guard Gallant, HeavyArmour)')
    action('CreateItem(GallantSword, Sword)')
    
    # King Phillip
    action('CreateCharacter(King Phillip, H)')
    action('SetClothing(King Phillip, King)')
    action('SetHairStyle(King Phillip, Short_Full)')
    
    # Witch Carlita
    action('CreateCharacter(Witch Carlita, C)')
    action('SetClothing(Witch Carlita, Witch)')
    action('SetHairStyle(Witch Carlita, Long)')
    action('SetHairColor(Witch Carlita, Gray)')
    action('Face(Witch Carlita, QueensCastle.BackRightChair)')
    action('CreateItem(CarlitaBook, BlueBook)')

    # Noble Jeremy
    action('CreateCharacter(Noble Jeremy, F)')
    action('SetClothing(Noble Jeremy, Noble)')
    action('SetHairStyle(Noble Jeremy, Spiky)')

    # Noble Cecilia
    action('CreateCharacter(Noble Cecilia, C)')
    action('SetClothing(Noble Cecilia, Noble)')
    action('SetHairStyle(Noble Cecilia, Short)')
    
    # Merchant Bert
    action('CreateCharacter(Merchant Bert, H)')
    action('SetClothing(Merchant Bert, Merchant)')
    action('SetHairColor(Merchant Bert, Blonde)')
    
    # Chamber Maid Scarlet
    action('CreateCharacter(Chamber Maid Scarlet, E)')
    action('SetClothing(Chamber Maid Scarlet, Peasant)')
    action('SetHairStyle(Chamber Maid Scarlet, Ponytail)')
    action('SetHairColor(Chamber Maid Scarlet, Brown)')
    
    # Tiana
    action('CreateCharacter(Tiana, A)')
    action('SetClothing(Tiana, Noble)')
    action('SetHairStyle(Tiana, Straight)')
    action('SetHairColor(Tiana, Brown)')
    
    # Castle Grand Maester Purcell
    action('CreateCharacter(Maester Purcell, H)')
    action('SetClothing(Maester Purcell, Priest)')
    action('SetHairStyle(Maester Purcell, Mage_Full)')
    action('SetHairColor(Maester Purcell, Gray)')

    ###############################################################
    # END CASTLE                                                  #
    ###############################################################

    ###############################################################
    # CITY                                                        #
    ###############################################################
    
    # Creating the possible clues within the city scene
    action('CreateItem(Desperate Times, Rags)')
    action('CreateItem(Beggar Miles Testimonial, PurplePotion)')
    action('CreateItem(Testimonial Gossip, EvilBook)')

    # Create City Characters
    # Beggar Adeline
    action('CreateCharacter(Beggar Adeline, G)')
    action('SetClothing(Beggar Adeline, Beggar)')
    action('SetHairStyle(Beggar Adeline, Long)')
    action('SetPosition(Beggar Adeline, City.Fountain)')
    action('SetExpression(Beggar Adeline, neutral)')
    action('SetSkinColor(Beggar Adeline, 4)')
    
    # Beggar Miles
    action('CreateCharacter(Beggar Miles, H)')
    action('SetClothing(Beggar Miles, Beggar)')
    action('SetHairStyle(Beggar Miles, Mage)')
    action('SetPosition(Beggar Miles, City.Bench)')
    action('Sit(Beggar Miles, City.Bench)')
    action('SetExpression(Beggar Miles, sad')
    action('SetSkinColor(Beggar Miles, 4)')
    
    # Alchemist Jeremy
    action('CreateCharacter(Alchemist Jeremy, F)')
    action('SetClothing(Alchemist Jeremy, Merchant)')
    action('SetHairStyle(Alchemist Jeremy, Spiky)')
    action('SetPosition(Alchemist Jeremy, City.BrownHouseDoor)')
    action('WalkToSpot(Alchemist Jeremy, 925.3, 0.3, 5.0)')
    action('SetExpression(Alchemist Jeremy, happy)')
    action('SetSkinColor(Alchemist Jeremy, 7)')
    
    # Scout Joanna
    action('CreateCharacter(Scout Joanna, C)')
    action('SetClothing(Scout Joanna, LightArmour)')
    action('SetHairStyle(Scout Joanna, Ponytail)')
    action('SetPosition(Scout Joanna, City.NorthEnd)')
    action('CreateItem(JoannaTorch, Torch)')
    action('SetPosition(JoannaTorch, Scout Joanna)')
    action('SetSkinColor(Scout Joanna, 2)')
    
    # Scout Tom
    action('CreateCharacter(Scout Tom, D)')
    action('SetClothing(Scout Tom, LightArmour)')
    action('SetHairStyle(Scout Tom, Short)')
    action('SetPosition(Scout Tom, City.WestEnd)')
    action('CreateItem(TomTorch, Torch)')
    action('SetPosition(TomTorch, Scout Joanna)')
    action('WalkToSpot(Scout Tom, 916.0, 0.3, -12.6)')
    action('SetSkinColor(Scout Tom, 2)')
    
    # Drunk Devon
    action('CreateCharacter(Drunk Devon, F)')
    action('SetClothing(Drunk Devon, Peasant)')
    action('SetHairStyle(Drunk Devon, Musketeer)')
    action('SetPosition(Drunk Devon, City.GreenHouseDoor)')
    action('CreateItem(DevonsBottle, Bottle)')
    action('SetPosition(DevonsBottle, Drunk Devon)')
    action('WalkToSpot(Drunk Devon, 906.4, 0.3, -1.2)')
    action('SetExpression(Drunk Devon, happy)')
    action('SetSkinColor(Drunk Devon, 3)')
    
    # Priestess Esmerelda
    action('CreateItem(A Possible Smiting, SpellBook)')
    action('CreateCharacter(Priestess Esmerelda, E)')
    action('SetClothing(Priestess Esmerelda, Priest)')
    action('SetHairStyle(Priestess Esmerelda, Short)')
    action('SetPosition(Priestess Esmerelda, City.RedHouseDoor)')
    action('CreateItem(EsmereldaBook, RedBook)')
    action('SetPosition(EsmereldaBook, Priestess Esmerelda)')
    action('WalkToSpot(Priestess Esmerelda, 928.9, 0.4, -1.7)')
    action('SetExpression(Priestess Esmerelda, angry)')
    
    # Blind Bandit
    action('CreateItem(A Contract Killing, Coin)')
    action('CreateCharacter(Blind Bandit, C)')
    action('SetClothing(Blind Bandit, Bandit)')
    action('SetHairStyle(Blind Bandit, Long)')
    action('SetPosition(Blind Bandit, City.Alley)')
    action('SetSkinColor(Blind Bandit, 5)')
    
    #Gossiping Gail
    action('CreateCharacter(Gossiping Gail, A)')
    action('SetClothing(Gossiping Gail, Peasant)')
    action('SetHairStyle(Gossiping Gail, Spiky)')
    action('SetPosition(Gossiping Gail, City.BlueHouseDoor)')
    action('WalkToSpot(Gossiping Gail, 924.8, 0.3, -10.2)')
    action('SetExpression(Gossiping Gail, happy)')
    
    #Enable Icons
    action('EnableIcon(Talk, Talk, Beggar Adeline, Talk to Beggar Adeline, true)')
    action('EnableIcon(Talk, Talk, Beggar Miles, Talk to Beggar Miles, true)')
    action('EnableIcon(Talk, Talk, Alchemist Jeremy, Talk to Alchemist Jeremy, true)')
    action('EnableIcon(Talk, Talk, Scout Joanna, Talk to Scout Joanna, true)')
    action('EnableIcon(Talk, Talk, Scout Tom, Talk to Scout Tom, true)')
    action('EnableIcon(Talk, Talk, Drunk Devon, Talk to Drunk Devon, true)')
    action('EnableIcon(Talk, Talk, Blind Bandit, Talk to Blind Bandit, true)')
    action('EnableIcon(Talk, Talk, Priestess Esmerelda, Talk to Priestess Esmerelda, true)')
    action('EnableIcon(Talk, Talk, Gossiping Gail, Talk to Gossiping Gail, true)')
    action('EnableIcon(Enter, Exit, City.BrownHouseDoor, Enter the Alchemist Shop, true)')
    action('EnableIcon(Enter, Exit , City.GreenHouseDoor, Enter the Tavern, true)')

    ###############################################################
    # END CITY                                                    #
    ###############################################################
    
    ###############################################################
    # DUNGEON                                                     #
    ###############################################################
    
    # Create Cell Door Guard Lyra
    action('CreateCharacter(Guard Lyra, C)')
    action('SetEyeColor(Guard Lyra, green)')
    action('SetClothing(Guard Lyra, LightArmour)')
    action('SetHairStyle(Guard Lyra, Short)')
    action('SetSkinColor(Guard Lyra, 2)')
    action('SetHairColor(Guard Lyra, red)')
    action('SetPosition(Guard Lyra, Prison.CellDoor)')
    action('SetExpression(Guard Lyra, disgusted)')
    #action('WalkToSpot(Guard Lyra, -608.6, 0.0, -2.7)')

    # Create items and position them
    action('CreateItem(Cell Door Key, BlueKey)')
    action('SetPosition(Cell Door Key, QueensCastle.Door)')
    action('CreateItem(Dire News, PurpleBook)')
    action('SetPosition(Dire News, Prison.Bookshelf.Left)')
    action('CreateItem(Prison Ledger, OpenScroll)')
    action('SetPosition(Prison Ledger, Prison.Table.Left)')
    action('CreateItem(Note From King, OpenScroll)')
    action('SetPosition(Note From King, Prison.DirtPile)')
    action('CreateItem(Change of Clothes, RedCloth)')
    
    # Creating the possible clues within the dungeon scene
    action('CreateItem(Starting Investigations, MagnifyingGlass)')
    action('CreateItem(A Testimonial by the Alchemist, PurplePotion)')

    # Enable Icons
    action('EnableIcon(Sit, Bed, Prison.Bed, Sit, true)')
    action('EnableIcon(Look_in_DirtPile, hand, Prison.DirtPile, Look through dirt, true)')
    action('EnableIcon(TakeLeft, hand, Cell Door Key, Take, true)')
    action('EnableIcon(Read, Research, Note From King, Read, true)')
    #action('EnableIcon(TakeLeft, hand, Party Invitation, Take, true)')
    action('EnableIcon(ChangeClothes, armour, Change of Clothes, Change Clothes, true)')

    ###############################################################
    # END DUNGEON                                                 #
    ###############################################################
    
    ###############################################################
    # ALCHEMIST SHOP                                              #
    ###############################################################
    
    # Creating the possible clues within the alchemist shop scene
    action('CreateItem(Found Poison, PurplePotion')
    action('CreateItem(Alchemist Testimonial, GreenPotion')

    # Alchemist Henry
    action('CreateCharacter(Alchemist Henry, D)')
    action('SetClothing(Alchemist Henry, Warlock)')
    action('SetHairStyle(Alchemist Henry, Short_Full)')
    action('SetEyeColor(Alchemist Henry, red)')
    action('SetPosition(Alchemist Henry, Alch.Bar.Behind)')

    # Enable Effects
    action('EnableEffect(Alch.Fireplace, Blackflame)')
    action('EnableEffect(Alch.Cauldron, Poison)')

    # Create Items
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

    # Position Items
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

    # Enable Icons
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
    action('EnableIcon(Leave, door, Alch.Door, Leave, true)')
    #action('EnableIcon(TakeLeft, hand, Poison, Take Giant Rat Poison, false)')

    ###############################################################
    # END ALCHEMIST SHOP                                          #
    ###############################################################

    ###############################################################
    # STORAGE                                                     #
    ###############################################################

    action('CreateCharacter(Tester, D)')
    action('SetClothing(Tester, Noble)')
    action('SetPosition(Tester, CastleStorage.Shelf)')
    action('WalkToSpot(Tester, 2101.8, 0.1, -2.1)')
    action('Die(Tester)')
    action('CreateItem(AlchemistLetter, OpenScroll)')
    action('SetPosition(AlchemistLetter, CastleStorage.Barrel)')
    action('EnableIcon(ReadAlchemistLetter, Read, AlchemistLetter, Read Letter, true)')
    action('EnableIcon(OpenStorageChest, Chest, CastleStorage.Chest, Open Chest, true)')
    action('EnableIcon(InspectTester, Research, Tester, Inspect Body, true)')
    action('EnableIcon(ExitStorage, Door, CastleStorage.Door, Exit, true)')

    ###############################################################
    # END STORAGE                                                 #
    ###############################################################

    ###############################################################
    # TAVERN                                                      #
    ###############################################################
    
    
    # Creating the possible clues within the tavern scene
    action('CreateItem(Purcell Senile, OpenScroll)')
    action('CreateItem(Tiana Jealous, BlueBook)')
    action('CreateItem(Chamber Maid Distressed, PurpleBook)')
    action('CreateItem(Much Smarter than he Looks, Skull')
    action('CreateItem(Sinister Sister, EvilBook)')
    action('CreateItem(Chamber Maid Testimonial, PurplePotion)')

    # Creating the Tavern Bartender and enabling interactivity
    action('CreateCharacter(Bartender Bill, D)')
    action('SetClothing(Bartender Bill, Merchant)')
    action('SetPosition(Bartender Bill, Tavern.Bar.Behind)')
    action('SetEyeColor(Bartender Bill, blue)')
    action('SetSkinColor(Bartender Bill, 5)')
    action('SetHairColor(Bartender Bill, blonde)')
    action('EnableIcon(Talk, Talk, Bartender Bill, Talk to Bartender Bill, true)')
    
    ###############################################################
    # END TAVERN                                                  #
    ###############################################################    

# Setup beginning of the game
def begin_game_setup():    
    all_game_setup()
    castle_setup()
    
    # Show the menu
    action('ShowMenu()')
    

    


