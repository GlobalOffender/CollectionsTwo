import random
Points = 0
# Dobbel
Dice = []
def RollDice():
    for x in range(6):
        Dobbel = random.randint(1,5)
        Dice.append(Dobbel)
    print(Dice)

def ClearDice():
    global Dice
    Dice = []

# Check wat er in RollDice zit
def CheckDice():
    global Points
    DiceCount1 = Dice.count(1)
    DiceCount2 = Dice.count(2)
    DiceCount3 = Dice.count(3)
    DiceCount4 = Dice.count(4)
    DiceCount5 = Dice.count(5)
    DiceCount6 = Dice.count(6)

    if ('1' in Dice and '2' in Dice and '3' in Dice and '4' in Dice and '5' in Dice) or ('2' in Dice and '3' in Dice and '4' in Dice and '5' in Dice and '6' in Dice):
        print('Long Straight')
        Points = Points + 20
    if DiceCount1 == 3 or DiceCount2 == 3 or DiceCount3 == 3 or DiceCount4 == 3 or DiceCount5 == 3 or DiceCount6 == 3:
        print('3 of a kind')
        Points = Points + 10
    if DiceCount1 == 4 or DiceCount2 == 4 or DiceCount3 == 4 or DiceCount4 == 4 or DiceCount5 == 4 or DiceCount6 == 4:
        print('4 of a kind')
        Points = Points + 15
    if DiceCount1 == 5 or DiceCount2 == 5 or DiceCount3 == 5 or DiceCount4 == 5 or DiceCount5 == 5 or DiceCount6 == 5:
        print('YAHTZEE')
        Points = Points + 25
    else:
        ClearDice()

# Continue
def Cont():
    conti = input("Continue? [Y/N] ").lower()
    if conti == 'n':
        exit()
    else:
        RollDice()
        CheckDice()
        ClearDice()
        print(Points)
        Cont()

# Command
# - RollDice()
# - CheckDice()
# - ClearDice()
# - Cont()

# Run

cont1 = input('Press any key to play')
RollDice()
CheckDice()
ClearDice()
print(Points)
Cont()


