from action import action

#Setup beginning of the game
def begin_game_setup():
    # Create Queens Castle
    action('CreatePlace(QueensCastle, DiningRoom)')
    
    #Create Characters
    #Main Character(John)
    action('CreateCharacter(John, B)')
    action('SetClothing(John, Noble)')
    action('SetHairStyle(John, Long)')
    action('SetPosition(John, QueensCastle.BackRightChair)')
    action('Sit(John, QueensCastle.BackRightChair)')
    #Queen
    action('CreateCharacter(Queen, A)')
    action('SetClothing(Queen, Queen)')
    action('SetHairStyle(Queen, Long)')
    action('SetPosition(Queen, QueensCastle.RightChair)')
    action('Sit(Queen, QueensCastle.RightChair)')
    #GuardGallant
    action('CreateCharacter(GuardGallant, F)')
    action('SetClothing(GuardGallant, HeavyArmour)')
    action('SetPosition(GuardGallant, QueensCastle.Door)')
    action('CreateItem(GallantSword, Sword)')
    action('SetPosition(GallantSword, GuardGallant)')
    #King
    action('CreateCharacter(King, H)')
    action('SetClothing(King, King)')
    action('SetPosition(King, QueensCastle.LeftChair)')
    action('Sit(King, QueensCastle.LeftChair)')
    action('SetHairStyle(King, Short_Beard)')
    #CastleWitch
    action('CreateCharacter(CastleWitch, C)')
    action('SetClothing(CastleWitch, Witch)')
    action('SetPosition(CastleWitch, QueensCastle.LeftWindow)')
    action('SetHairStyle(CastleWitch, Long)')
    action('SetHairColor(CastleWitch, Gray)')
    action('Face(CastleWitch, QueensCastle.BackRightChair)')
    action('CreateItem(CastleWitchBook, BlueBook)')
    action('SetPosition(CastleWitchBook, CastleWitch)')
    #NobleJeremy
    action('CreateCharacter(NobleJeremy, F)')
    action('SetClothing(NobleJeremy, Noble)')
    action('SetPosition(NobleJeremy, QueensCastle.LeftWindow)')
    action('Sit(NobleJeremy, QueensCastle.FrontRightChair)')
    action('SetHairStyle(NobleJeremy, Spiky)')
    #NobleCecilia
    action('CreateCharacter(NobleCecilia, F)')
    action('SetClothing(NobleCecilia, Noble)')
    action('SetPosition(NobleCecilia, QueensCastle.LeftWindow)')
    action('SetHairStyle(NobleCecilia, Short)')
    action('Sit(NobleCecilia, QueensCastle.FrontLeftChair)')
    #MerchantBert
    action('CreateCharacter(MerchantBert, H)')
    action('SetClothing(MerchantBert, Merchant)')
    action('SetPosition(MerchantBert, QueensCastle.LeftWindow)')
    action('SetHairColor(MerchantBert, Blonde)')
    action('Sit(MerchantBert, QueensCastle.BackLeftChair)')
    #ChamberMaid
    action('CreateCharacter(ChamberMaid, E)')
    action('SetClothing(ChamberMaid, Peasant)')
    action('SetPosition(ChamberMaid, QueensCastle.BackDoor)')
    action('SetHairColor(ChamberMaid, Brown)')
    action('Face(ChamberMaid, QueensCastle.DiningTable)')
    #Create Items and position them
    action('CreateItem(QueensCup, GoldCup)')
    action('SetPosition(QueensCup, QueensCastle.DiningTable.Right)')
    action('CreateItem(JohnsCup, GoldCup)')
    action('SetPosition(JohnsCup, QueensCastle.DiningTable.BackRight)')
    action('CreateItem(BertsCup, GoldCup)')
    action('SetPosition(BertsCup, QueensCastle.DiningTable.BackLeft)')
    action('CreateItem(JeremysCup, GoldCup)')
    action('SetPosition(JeremysCup, QueensCastle.DiningTable.FrontRight)')
    action('CreateItem(KingsCup, GoldCup)')
    action('SetPosition(KingsCup, QueensCastle.DiningTable.Left)')
    action('CreateItem(CeciliasCup, GoldCup)')
    action('SetPosition(CeciliasCup, QueensCastle.DiningTable.FrontLeft)')
    action('CreateItem(PythonBox, BlueBook)')
    action('SetPosition(PythonBox, QueensCastle.Table)')
    
    #Enable Icons
    action('EnableIcon(Sit, Chair, QueensCastle.BackRightChair, Sit, true)')
    action('EnableIcon(Python, Drink, PythonBox, Command Camelot, true)')
    action('EnableIcon(Talk, Talk, Queen, Talk to the Queen, true)')

    # #EnableEffects
    action('EnableEffect(QueensCastle.Fireplace, Campfire)')

    
    action('ShowMenu()')