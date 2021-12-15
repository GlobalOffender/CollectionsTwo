
import random
num = 1
def card():
    Deck = ['Joker 1', 'Joker 2', 'Ace of Spades', '2 Spades', '3 Spades', '4 Spades', '5 Spades', '6 Spades', '7 Spades', '8 Spades', '9 Spades', ' 10 Spades', 'Knight of Spades', 'Queen of Spades', 'King of Spades', 'Ace of Diamonds', '2 Diamonds', '3 Diamonds', '4 Diamonds', '5 Diamonds', '6 Diamonds', '7 Diamonds', '8 Diamonds', '9 Diamonds', ' 10 Diamonds', 'Knight of Diamonds', 'Queen of Diamonds', 'King of Diamonds', 'Ace of Hearts', '2 Hearts', '3 Hearts', '4 Hearts', '5 Hearts', '6 Hearts', '7 Hearts', '8 Hearts', '9 Hearts', ' 10 Hearts', 'Knight of Hearts', 'Queen of Hearts', 'King of Hearts', 'Ace of Clubs', '2 Clubs', '3 Clubs', '4 Clubs', '5 Clubs', '6 Clubs', '7 Clubs', '8 Clubs', '9 Clubs', ' 10 Clubs', 'Knight of Clubs', 'Queen of Clubs', 'King of Clubs']
    Number = random.randint(0, 54)
    print('Card ' + str(num) + ' : ' + Deck[Number])
    Deck.pop(Number)
Amount = int(input("How many cards do you want? "))
for x in range(0, Amount):
    card()
    num = num + 1