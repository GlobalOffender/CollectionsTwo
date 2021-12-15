import random

# Values
Player1 = 0
Player2 = 0
CardPicked = ''

# Lists
AllCards = ['Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Knight', 'Queen', 'King']
Deck1 = []
Deck2 = []
# Card Grabber Player 1
def CardPlay1():
    global CardPicked
    CardPicked = random.choice(AllCards)
    Deck1.append(CardPicked)
    Selected = AllCards.index(CardPicked)
    AllCards.pop(Selected)
    print(CardPicked)
    CardCheck1()
    CardPlay2()
# Card Score Checker Player 1
def CardCheck1():
    global CardPicked
    global Player1
    if CardPicked == '2':
        Player1 = Player1 + 2
    if CardPicked == '3':
        Player1 = Player1 + 3
    if CardPicked == '4':
        Player1 = Player1 + 4
    if CardPicked == '5':
        Player1 = Player1 + 5
    if CardPicked == '6':
        Player1 = Player1 + 6
    if CardPicked == '7':
        Player1 = Player1 + 7
    if CardPicked == '8':
        Player1 = Player1 + 8
    if CardPicked == '9':
        Player1 = Player1 + 9
    if CardPicked == '10' or CardPicked == 'Knight' or CardPicked == 'Queen' or CardPicked == 'King':
        Player1 = Player1 + 10
    if CardPicked == 'Ace':
        if Player1 <= 10:
            Player1 = Player1 + 11
        else:
            Player1 = Player1 + 1
    if Player1 > 21:
        print('Player 1 Bust')
        exit()
    else:
        print(Player1)

# Card Grabber Player 2
def CardPlay2():
    global CardPicked
    # Selected = random.randint(0, len(AllCards))
    # CardPicked = AllCards[Selected]
    CardPicked = random.choice(AllCards)
    Deck1.append(CardPicked)
    Selected = AllCards.index(CardPicked)
    AllCards.pop(Selected)
    print(CardPicked)
    CardCheck2()
    CardPlay1()

# Card Score Checker Player 2
def CardCheck2():
    global CardPicked
    global Player2
    if CardPicked == '2':
        Player2 = Player2 + 2
    if CardPicked == '3':
        Player2 = Player2 + 3
    if CardPicked == '4':
        Player2 = Player2 + 4
    if CardPicked == '5':
        Player2 = Player2 + 5
    if CardPicked == '6':
        Player2 = Player2 + 6
    if CardPicked == '7':
        Player2 = Player2 + 7
    if CardPicked == '8':
        Player2 = Player2 + 8
    if CardPicked == '9':
        Player2 = Player2 + 9
    if CardPicked == '10' or CardPicked == 'Knight' or CardPicked == 'Queen' or CardPicked == 'King':
        Player2 = Player2 + 10
    if CardPicked == 'Ace':
        if Player2 <= 10:
            Player2 = Player2 + 11
        else:
            Player2 = Player2 + 1
    if Player2 > 21:
        print('Player 2 Bust')
        exit()
    else:
        print(Player2)

# Run
CardPlay1()