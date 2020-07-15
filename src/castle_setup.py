from action import action

def castle_setup():
    #Set at Night
    action('SetNight()', False)

    # Sound Affect
    # Start Background sound for castle
    action('PlaySound(Fireplace, QueensCastle.Fireplace, true)', False)
    action('PlaySound(LivelyMusic, QueensCastle, true)', False)
    action('PlaySound(Danger3, CastleStorage, true)', False)

    # Setup and position John
    action('SetClothing(John, Noble)', False)
    action('SetPosition(John, QueensCastle.BackRightChair)')
    action('Sit(John, QueensCastle.BackRightChair)', False)

    # Queen Margerie Setup
    action('SetExpression(Queen Margerie, Happy)', False)
    action('SetPosition(Queen Margerie, QueensCastle.RightChair)')
    action('Sit(Queen Margerie, QueensCastle.RightChair)', False)

    # Guard Gallant
    action('SetPosition(Guard Gallant, QueensCastle.Door)', False)
    action('Draw(Guard Gallant, GallantSword)', False)

    # King Phillip
    action('SetPosition(King Phillip, QueensCastle.LeftChair)')
    action('Sit(King Phillip, QueensCastle.LeftChair)')
    action('SetExpression(King Phillip, Happy)', False)

    # Witch Carlita
    action('SetPosition(Witch Carlita, QueensCastle.LeftWindow)', False)
    action('SetPosition(CarlitaBook, Witch Carlita)', False)
    action('SetSkinColor(Witch Carlita, 3)', False)

    # Noble Jeremy
    action('SetPosition(Noble Jeremy, QueensCastle.FrontRightChair)')
    action('Sit(Noble Jeremy, QueensCastle.FrontRightChair)', False)

    # Noble Cecilia
    action('SetPosition(Noble Cecilia, QueensCastle.FrontLeftChair)')
    action('Sit(Noble Cecilia, QueensCastle.FrontLeftChair)', False)

    # Merchant Bert
    action('SetPosition(Merchant Bert, QueensCastle.BackLeftChair)')
    action('Sit(Merchant Bert, QueensCastle.BackLeftChair)', False)
    action('SetSkinColor(Merchant Bert, 8)', False)

    # Chamber Maid Scarlet
    action('SetPosition(Chamber Maid Scarlet, QueensCastle.BackDoor)')
    action('MoveAway(QueensCastle.BackDoor)')
    #action('WalkToSpot(Chamber Maid Scarlet, 310.6, 0.1, -1.7)')
    action('Face(Chamber Maid Scarlet, QueensCastle.DiningTable)')

    # Tiana
    action('SetPosition(Tiana, QueensCastle.RightWindow)')
    action('Face(Tiana, QueensCastle.DiningTable)')
    action('SetExpression(Tiana, Disgusted)', False)

    # Grand Maester Purcell
    action('SetPosition(Maester Purcell, QueensCastle.Table)', False)
    #action('Face(Maester Purcell, QueensCastle.DiningTable)')

    #Create Items and position them
    action('CreateItem(QueensCup, GoldCup)')
    action('SetPosition(QueensCup, QueensCastle.DiningTable.Right)', False)
    action('CreateItem(JohnsCup, GoldCup)')
    action('SetPosition(JohnsCup, QueensCastle.DiningTable.BackRight)', False)
    action('CreateItem(BertsCup, GoldCup)')
    action('SetPosition(BertsCup, QueensCastle.DiningTable.BackLeft)', False)
    action('CreateItem(JeremysCup, GoldCup)')
    action('SetPosition(JeremysCup, QueensCastle.DiningTable.FrontRight)', False)
    action('CreateItem(KingsCup, GoldCup)')
    action('SetPosition(KingsCup, QueensCastle.DiningTable.Left)', False)
    action('CreateItem(CeciliasCup, GoldCup)')
    action('SetPosition(CeciliasCup, QueensCastle.DiningTable.FrontLeft)', False)
    action('CreateItem(GuestLedger, GreenBook)')
    action('SetPosition(GuestLedger, QueensCastle.Table)', False)
    action('CreateItem(ClosetKeyBag, Bag)')
    action('SetPosition(ClosetKeyBag, QueensCastle.Shelf)', False)
    action('CreateItem(ClosetKey, GreenKey)')

    # Enable Icons
    #action('EnableIcon(Sit, Chair, QueensCastle.BackRightChair, Sit, true)', False)
    action('EnableIcon(Talk, Talk, Maester Purcell, Talk to Maester Purcell, true)', False)
    action('EnableIcon(Talk, Talk, Guard Gallant, Talk to Guard, true)', False)
    action('EnableIcon(Talk, Talk, Queen Margerie, Talk to Queen Margerie, true)', False)
    action('EnableIcon(Talk, Talk, Witch Carlita, Talk to Witch Carlita, true)', False)
    action('EnableIcon(Talk, Talk, Tiana, Talk to Tiana, true)', False)
    action('EnableIcon(Talk, Talk, King Phillip, Talk to the King Phillip, true)', False)
    action('EnableIcon(ReadLedger, Research, GuestLedger, Read, true)', False)
    action('EnableIcon(CheckClosetKeyBag, Magnifyingglass, ClosetKeyBag, Inspect, true)', False)

    # EnableEffects
    action('EnableEffect(QueensCastle.Fireplace, Campfire)', False)

    # Starting Inventory
    action('CreateItem(Party Invitation, OpenScroll)')
    action('EnableIcon(ReadInvitation, Book, Party Invitation, Read, true)', False)

    # Start in black
    action('FadeOut()')
