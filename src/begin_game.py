''' 
Authors: Zach Moore, Travis Conley, Adrian Wyllie, Mitchel Dennis
Purpose: Performs a lot of Camelot calls to setup a majority of the game.
'''
from action import action
from castle_setup import castle_setup

def all_game_setup():
    action('SetTitle(\"Murder in Felguard\")', False)
    action("SetCredits(\"Experience Manager by Zach Moore, Travis Conley, Adrian Wyllie, Mitchel Dennis\")", False)

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
    action('SetHairStyle(John, Long)', False)
    action('SetEyeColor(John, blue)', False)
    
    # Queen Margerie
    action('CreateCharacter(Queen Margerie, A)')
    action('SetClothing(Queen Margerie, Queen)', False)
    action('SetHairStyle(Queen Margerie, Long)', False)
    action('SetEyeColor(Queen Margerie, green)', False)
    
    # Guard Gallant
    action('CreateCharacter(Guard Gallant, F)')
    action('SetClothing(Guard Gallant, HeavyArmour)', False)
    action('CreateItem(GallantSword, Sword)', False)
    
    # King Phillip
    action('CreateCharacter(King Phillip, H)')
    action('SetClothing(King Phillip, King)', False)
    action('SetHairStyle(King Phillip, Short_Full)', False)
    
    # Witch Carlita
    action('CreateCharacter(Witch Carlita, C)')
    action('SetClothing(Witch Carlita, Witch)', False)
    action('SetHairStyle(Witch Carlita, Long)', False)
    action('SetHairColor(Witch Carlita, Gray)', False)
    action('Face(Witch Carlita, QueensCastle.BackRightChair)')
    action('CreateItem(CarlitaBook, BlueBook)', False)

    # Noble Jeremy
    action('CreateCharacter(Noble Jeremy, F)')
    action('SetClothing(Noble Jeremy, Noble)', False)
    action('SetHairStyle(Noble Jeremy, Spiky)', False)

    # Noble Cecilia
    action('CreateCharacter(Noble Cecilia, C)')
    action('SetClothing(Noble Cecilia, Noble)', False)
    action('SetHairStyle(Noble Cecilia, Short)', False)
    
    # Merchant Bert
    action('CreateCharacter(Merchant Bert, H)')
    action('SetClothing(Merchant Bert, Merchant)', False)
    action('SetHairColor(Merchant Bert, Blonde)', False)
    
    # Chamber Maid Scarlet
    action('CreateCharacter(Chamber Maid Scarlet, E)')
    action('SetClothing(Chamber Maid Scarlet, Peasant)', False)
    action('SetHairStyle(Chamber Maid Scarlet, Ponytail)', False)
    action('SetHairColor(Chamber Maid Scarlet, Brown)', False)
    
    # Tiana
    action('CreateCharacter(Tiana, A)')
    action('SetClothing(Tiana, Noble)', False)
    action('SetHairStyle(Tiana, Straight)', False)
    action('SetHairColor(Tiana, Brown)', False)
    
    # Castle Grand Maester Purcell
    action('CreateCharacter(Maester Purcell, H)')
    action('SetClothing(Maester Purcell, Priest)', False)
    action('SetHairStyle(Maester Purcell, Mage_Full)', False)
    action('SetHairColor(Maester Purcell, Gray)', False)

    ###############################################################
    # END CASTLE                                                  #
    ###############################################################

    ###############################################################
    # CITY                                                        #
    ###############################################################
    
    # Creating the possible clues within the city scene
    action('CreateItem(Desperate Times, Rags)', False)
    action('CreateItem(Beggar Miles Testimonial, PurplePotion)', False)
    action('CreateItem(Testimonial Gossip, EvilBook)', False)

    # Create City Characters
    # Beggar Adeline
    action('CreateCharacter(Beggar Adeline, G)')
    action('SetClothing(Beggar Adeline, Beggar)', False)
    action('SetHairStyle(Beggar Adeline, Long)', False)
    action('SetPosition(Beggar Adeline, City.Fountain)', False)
    action('SetExpression(Beggar Adeline, neutral)', False)
    action('SetSkinColor(Beggar Adeline, 4)', False)
    
    # Beggar Miles
    action('CreateCharacter(Beggar Miles, H)')
    action('SetClothing(Beggar Miles, Beggar)', False)
    action('SetHairStyle(Beggar Miles, Mage)', False)
    action('SetPosition(Beggar Miles, City.Bench)')
    action('Sit(Beggar Miles, City.Bench)', False)
    action('SetExpression(Beggar Miles, sad', False)
    action('SetSkinColor(Beggar Miles, 4)', False)
    
    # Alchemist Jeremy
    action('CreateCharacter(Alchemist Jeremy, F)')
    action('SetClothing(Alchemist Jeremy, Merchant)', False)
    action('SetHairStyle(Alchemist Jeremy, Spiky)', False)
    action('SetPosition(Alchemist Jeremy, City.BrownHouseDoor)')
    action('MoveAway(City.BrownHouseDoor)')
    action('WalkToSpot(Alchemist Jeremy, 925.3, 0.3, 5.0)', False)
    action('SetExpression(Alchemist Jeremy, happy)', False)
    action('SetSkinColor(Alchemist Jeremy, 7)', False)
    
    # Scout Joanna
    action('CreateCharacter(Scout Joanna, C)')
    action('SetClothing(Scout Joanna, LightArmour)', False)
    action('SetHairStyle(Scout Joanna, Ponytail)', False)
    action('SetPosition(Scout Joanna, City.NorthEnd)', False)
    action('CreateItem(JoannaTorch, Torch)')
    action('SetPosition(JoannaTorch, Scout Joanna)', False)
    action('SetSkinColor(Scout Joanna, 2)', False)
    
    # Scout Tom
    action('CreateCharacter(Scout Tom, D)')
    action('SetClothing(Scout Tom, LightArmour)', False)
    action('SetHairStyle(Scout Tom, Short)', False)
    action('SetPosition(Scout Tom, City.EastEnd)', False)
    action('CreateItem(TomTorch, Torch)')
    action('SetPosition(TomTorch, Scout Tom)', False)
    #action('WalkToSpot(Scout Tom, 916.0, 0.3, -12.6)')
    action('SetSkinColor(Scout Tom, 2)', False)
    
    # Drunk Devon
    action('CreateCharacter(Drunk Devon, F)')
    action('SetClothing(Drunk Devon, Peasant)', False)
    action('SetHairStyle(Drunk Devon, Musketeer)', False)
    action('SetPosition(Drunk Devon, City.GreenHouseDoor)')
    action('CreateItem(DevonsBottle, Bottle)')
    action('SetPosition(DevonsBottle, Drunk Devon)', False)
    action('MoveAway(City.GreenHouseDoor)')
    #action('WalkToSpot(Drunk Devon, 906.4, 0.3, -1.2)')
    action('SetExpression(Drunk Devon, happy)', False)
    action('SetSkinColor(Drunk Devon, 3)', False)
    
    # Priestess Esmerelda
    action('CreateItem(A Possible Smiting, SpellBook)', False)
    action('CreateCharacter(Priestess Esmerelda, E)')
    action('SetClothing(Priestess Esmerelda, Priest)', False)
    action('SetHairStyle(Priestess Esmerelda, Short)', False)
    action('SetPosition(Priestess Esmerelda, City.RedHouseDoor)')
    action('CreateItem(EsmereldaBook, RedBook)')
    action('SetPosition(EsmereldaBook, Priestess Esmerelda)', False)
    action('MoveAway(City.RedHouseDoor)')
    #action('WalkToSpot(Priestess Esmerelda, 928.9, 0.4, -1.7)')
    action('SetExpression(Priestess Esmerelda, angry)', False)
    
    # Blind Bandit
    action('CreateItem(A Contract Killing, Coin)', False)
    action('CreateCharacter(Blind Bandit, C)')
    action('SetClothing(Blind Bandit, Bandit)', False)
    action('SetHairStyle(Blind Bandit, Long)', False)
    action('SetPosition(Blind Bandit, City.Alley)', False)
    action('SetSkinColor(Blind Bandit, 5)', False)
    
    #Gossiping Gail
    action('CreateCharacter(Gossiping Gail, A)')
    action('SetClothing(Gossiping Gail, Peasant)', False)
    action('SetHairStyle(Gossiping Gail, Spiky)', False)
    #action('SetPosition(Gossiping Gail, City.BlueHouseDoor)')
    action('SetPosition(Gossiping Gail, City.Horse)', False)
    #action('WalkToSpot(Gossiping Gail, 924.8, 0.3, -10.2)')
    action('SetExpression(Gossiping Gail, happy)', False)
    
    #Enable Icons
    action('EnableIcon(Talk, Talk, Beggar Adeline, Talk to Beggar Adeline, true)', False)
    action('EnableIcon(Talk, Talk, Beggar Miles, Talk to Beggar Miles, true)', False)
    action('EnableIcon(Talk, Talk, Alchemist Jeremy, Talk to Alchemist Jeremy, true)', False)
    action('EnableIcon(Talk, Talk, Scout Joanna, Talk to Scout Joanna, true)', False)
    action('EnableIcon(Talk, Talk, Scout Tom, Talk to Scout Tom, true)', False)
    action('EnableIcon(Talk, Talk, Drunk Devon, Talk to Drunk Devon, true)', False)
    action('EnableIcon(Talk, Talk, Blind Bandit, Talk to Blind Bandit, true)', False)
    action('EnableIcon(Talk, Talk, Priestess Esmerelda, Talk to Priestess Esmerelda, true)', False)
    action('EnableIcon(Talk, Talk, Gossiping Gail, Talk to Gossiping Gail, true)', False)
    action('EnableIcon(Enter, Exit, City.BrownHouseDoor, Enter the Alchemist Shop, true)', False)
    action('EnableIcon(Enter, Exit , City.GreenHouseDoor, Enter the Tavern, true)', False)

    ###############################################################
    # END CITY                                                    #
    ###############################################################
    
    ###############################################################
    # DUNGEON                                                     #
    ###############################################################
    
    # Create Cell Door Guard Lyra
    action('CreateCharacter(Guard Lyra, C)')
    action('SetEyeColor(Guard Lyra, green)', False)
    action('SetClothing(Guard Lyra, LightArmour)', False)
    action('SetHairStyle(Guard Lyra, Short)', False)
    action('SetSkinColor(Guard Lyra, 2)', False)
    action('SetHairColor(Guard Lyra, red)', False)
    action('SetPosition(Guard Lyra, Prison.CellDoor)', False)
    action('SetExpression(Guard Lyra, disgusted)', False)
    #action('WalkToSpot(Guard Lyra, -608.6, 0.0, -2.7)')

    # Create items and position them
    action('CreateItem(Cell Door Key, BlueKey)', False)
    #action('SetPosition(Cell Door Key, QueensCastle.Door)')
    action('CreateItem(Dire News, PurpleBook)')
    action('SetPosition(Dire News, Prison.Bookshelf.Left)', False)
    action('CreateItem(Prison Ledger, OpenScroll)')
    action('SetPosition(Prison Ledger, Prison.Table.Left)', False)
    action('CreateItem(Note From King, OpenScroll)')
    #action('SetPosition(Note From King, Prison.DirtPile)')
    action('CreateItem(Change of Clothes, RedCloth)')
    
    # Creating the possible clues within the dungeon scene
    action('CreateItem(Starting Investigations, MagnifyingGlass)', False)
    action('CreateItem(A Testimonial by the Alchemist, PurplePotion)', False)

    # Enable Icons
    action('EnableIcon(Sit, Bed, Prison.Bed, Sit, true)', False)
    action('EnableIcon(Look_in_DirtPile, hand, Prison.DirtPile, Look through dirt, true)', False)
    action('EnableIcon(TakeLeft, hand, Cell Door Key, Take, true)', False)
    action('EnableIcon(Read, Research, Note From King, Read, true)', False)
    #action('EnableIcon(TakeLeft, hand, Party Invitation, Take, true)')
    action('EnableIcon(ChangeClothes, armour, Change of Clothes, Change Clothes, true)', False)

    ###############################################################
    # END DUNGEON                                                 #
    ###############################################################
    
    ###############################################################
    # ALCHEMIST SHOP                                              #
    ###############################################################
    
    # Creating the possible clues within the alchemist shop scene
    action('CreateItem(Found Poison, PurplePotion', False)
    action('CreateItem(Alchemist Testimonial, GreenPotion', False)

    # Alchemist Henry
    action('CreateCharacter(Alchemist Henry, D)')
    action('SetClothing(Alchemist Henry, Warlock)', False)
    action('SetHairStyle(Alchemist Henry, Short_Full)', False)
    action('SetEyeColor(Alchemist Henry, red)', False)
    action('SetPosition(Alchemist Henry, Alch.Bar.Behind)', False)

    # Enable Effects
    action('EnableEffect(Alch.Fireplace, Blackflame)', False)
    action('EnableEffect(Alch.Cauldron, Poison)', False)

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
    action('SetPosition(BluePotion1, Alch.Bar.Center)', False)
    action('SetPosition(Skull1, Alch.Bar.Right)', False)

    action('SetPosition(Poison, Alch.Table.Left)', False)
    action('SetPosition(GreenPotion1, Alch.Table.FrontLeft)', False)
    action('SetPosition(GreenPotion2, Alch.Table.BackRight)', False)
    action('SetPosition(PurplePotion1, Alch.Table.BackLeft)', False)

    action('SetPosition(BluePotion2, Alch.AlchemistTable.Left)', False)
    action('SetPosition(GreenPotion3, Alch.AlchemistTable.Right)', False)
    action('SetPosition(Skull2, Alch.AlchemistTable.Center)', False)

    action('SetPosition(RedPotion1, Alch.Bookshelf.Left)', False)
    action('SetPosition(RedPotion2, Alch.Bookshelf.Right)', False)

    # Enable Icons
    action('EnableIcon(Inspect, magnifyingglass, BluePotion1, Read Label, true)', False)
    action('EnableIcon(Inspect, magnifyingglass, BluePotion2, Read Label, true)', False)
    action('EnableIcon(Inspect, magnifyingglass, GreenPotion1, Read Label, true)', False)
    action('EnableIcon(Inspect, magnifyingglass, GreenPotion2, Read Label, true)', False)
    action('EnableIcon(Inspect, magnifyingglass, GreenPotion3, Read Label, true)', False)
    action('EnableIcon(Inspect, magnifyingglass, Poison, Read Label, true)', False)
    action('EnableIcon(Drink, drink, Poison, Drink Deadly Poison, false', False)
    action('EnableIcon(Inspect, magnifyingglass, PurplePotion1, Read Label, true)', False)
    action('EnableIcon(Inspect, magnifyingglass, RedPotion1, Read Label, true)', False)
    action('EnableIcon(Inspect, magnifyingglass, RedPotion2, Read Label, true)', False)
    action('EnableIcon(Inspect, magnifyingglass, Skull1, Inspect Skull, true', False)
    action('EnableIcon(Inspect, magnifyingglass, Skull2, Inspect Skull, true', False)
    action('EnableIcon(Inspect, bookshelf, Alch.RightBookcase, Browse, true)', False)
    action('EnableIcon(Inspect, bookshelf, Alch.LeftBookcase, Browse, true)', False)
    action('EnableIcon(Inspect, cauldron, Alch.Cauldron, Inspect, true)', False)
    action('EnableIcon(Talk, talk, Alchemist Henry, Talk to Alchemist Henry, true)', False)
    action('EnableIcon(Leave, door, Alch.Door, Leave, true)', False)
    #action('EnableIcon(TakeLeft, hand, Poison, Take Giant Rat Poison, false)')

    ###############################################################
    # END ALCHEMIST SHOP                                          #
    ###############################################################

    ###############################################################
    # STORAGE                                                     #
    ###############################################################

    action('CreateCharacter(Tester, D)')
    action('SetClothing(Tester, Noble)', False)
    action('SetPosition(Tester, CastleStorage.Shelf)')
    action('MoveAway(CastleStorage.Shelf)')
    #action('WalkToSpot(Tester, 2101.8, 0.1, -220.3)')
    action('Die(Tester)', False)
    action('CreateItem(AlchemistLetter, OpenScroll)')
    action('SetPosition(AlchemistLetter, CastleStorage.Barrel)', False)
    action('EnableIcon(ReadAlchemistLetter, Read, AlchemistLetter, Read Letter, true)', False)
    action('EnableIcon(OpenStorageChest, Chest, CastleStorage.Chest, Open Chest, true)', False)
    action('EnableIcon(InspectTester, Research, Tester, Inspect Body, true)', False)
    action('EnableIcon(ExitStorage, Door, CastleStorage.Door, Exit, true)', False)

    ###############################################################
    # END STORAGE                                                 #
    ###############################################################

    ###############################################################
    # TAVERN                                                      #
    ###############################################################
    
    
    # Creating the possible clues within the tavern scene
    action('CreateItem(Purcell Senile, OpenScroll)', False)
    action('CreateItem(Tiana Jealous, BlueBook)', False)
    action('CreateItem(Chamber Maid Distressed, PurpleBook)', False)
    action('CreateItem(Much Smarter than he Looks, Skull', False)
    action('CreateItem(Sinister Sister, EvilBook)', False)
    action('CreateItem(Chamber Maid Testimonial, PurplePotion)', False)

    # Creating the Tavern Bartender and enabling interactivity
    action('CreateCharacter(Bartender Bill, D)')
    action('SetClothing(Bartender Bill, Merchant)', False)
    action('SetPosition(Bartender Bill, Tavern.Bar.Behind)', False)
    action('SetEyeColor(Bartender Bill, blue)', False)
    action('SetSkinColor(Bartender Bill, 5)', False)
    action('SetHairColor(Bartender Bill, blonde)', False)
    action('EnableIcon(Talk, Talk, Bartender Bill, Talk to Bartender Bill, true)', False)
    action('EnableEffect(Tavern.Fireplace, CampFire)', False)
    
    ###############################################################
    # END TAVERN                                                  #
    ###############################################################    

# Setup beginning of the game
def begin_game_setup():    
    all_game_setup()
    castle_setup()
    
    # Show the menu
    action('ShowMenu()')
    

    


