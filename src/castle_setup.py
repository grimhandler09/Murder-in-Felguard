from action import action

def castle_setup():
    #Set at Night
    action('SetNight()')

    # Setup and position John
    action('SetClothing(John, Noble)')
    action('SetPosition(John, QueensCastle.BackRightChair)')
    action('Sit(John, QueensCastle.BackRightChair)')

    # Queen Margerie Setup
    action('SetExpression(Queen Margerie, Happy)')
    action('SetPosition(Queen Margerie, QueensCastle.RightChair)')
    action('Sit(Queen Margerie, QueensCastle.RightChair)')

    # Guard Gallant
    action('SetPosition(Guard Gallant, QueensCastle.Door)')
    action('Draw(Guard Gallant, GallantSword)')

    # King Phillip
    action('SetPosition(King Phillip, QueensCastle.LeftChair)')
    action('Sit(King Phillip, QueensCastle.LeftChair)')
    action('SetExpression(King Phillip, Happy)')

    # Witch Carlita
    action('SetPosition(Witch Carlita, QueensCastle.LeftWindow)')
    action('SetPosition(CarlitaBook, Witch Carlita)')

    # Noble Jeremy
    action('SetPosition(Noble Jeremy, QueensCastle.FrontRightChair)')
    action('Sit(Noble Jeremy, QueensCastle.FrontRightChair)')

    # Noble Cecilia
    action('SetPosition(Noble Cecilia, QueensCastle.FrontLeftChair)')
    action('Sit(Noble Cecilia, QueensCastle.FrontLeftChair)')

    # Merchant Bert
    action('SetPosition(Merchant Bert, QueensCastle.BackLeftChair)')
    action('Sit(Merchant Bert, QueensCastle.BackLeftChair)')

    # Chamber Maid Scarlet
    action('SetPosition(Chamber Maid Scarlet, QueensCastle.BackDoor)')
    action('WalkToSpot(Chamber Maid Scarlet, 310.6, 0.1, -1.7)')
    action('Face(Chamber Maid Scarlet, QueensCastle.DiningTable)')

    # Tiana
    action('SetPosition(Tiana, QueensCastle.Window)')
    action('Face(Tiana, QueensCastle.DiningTable)')
    action('SetExpression(Tiana, Disgusted)')

    # Grand Maester Purcell
    action('SetPosition(Maester Purcell, QueensCastle.Table)')
    #action('Face(Maester Purcell, QueensCastle.DiningTable)')

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
    action('CreateItem(GuestLedger, GreenBook)')
    action('SetPosition(GuestLedger, QueensCastle.Table)')
    action('CreateItem(ClosetKeyBag, Bag)')
    action('SetPosition(ClosetKeyBag, QueensCastle.Shelf)')
    action('CreateItem(ClosetKey, GreenKey)')

    # Enable Icons
    action('EnableIcon(Sit, Chair, QueensCastle.BackRightChair, Sit, true)')
    action('EnableIcon(Talk, Talk, Maester Purcell, Talk to Maester Purcell, true)')
    action('EnableIcon(Talk, Talk, Guard Gallant, Talk to Guard, true)')
    action('EnableIcon(Talk, Talk, Queen Margerie, Talk to Queen Margerie, true)')
    action('EnableIcon(Talk, Talk, Witch Carlita, Talk to Witch Carlita, true)')
    action('EnableIcon(Talk, Talk, Tiana, Talk to Tiana, true)')
    action('EnableIcon(Talk, Talk, King Phillip, Talk to the King Phillip, true)')
    action('EnableIcon(ReadLedger, Research, GuestLedger, Read, true)')
    action('EnableIcon(CheckClosetKeyBag, Magnifyingglass, ClosetKeyBag, Inspect, true)')

    # EnableEffects
    action('EnableEffect(QueensCastle.Fireplace, Campfire)')

    # Starting Inventory
    action('CreateItem(Party Invitation, OpenScroll)')
    action('EnableIcon(ReadInvitation, Book, Party Invitation, Read, true)')

    # Start in black
    action('FadeOut()')
