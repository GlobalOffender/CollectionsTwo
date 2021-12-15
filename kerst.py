import random

# Lijsten
NameList = []

# Naam Invoeren
def NameAdding():
    NameAdd = input("Name: ")
    if NameAdd in NameList:
        print("Name has already been used.")
        NameAdding()
    if NameAdd == '' or NameAdd == ' ':
        print("Please enter something.")
        NameAdding()
    NameList.append(NameAdd)
    NameContinue = input('Add more? [Y/N]').lower()
    if NameContinue == 'n':
        print(NameList)
    else:
        NameAdding()

# Lottery
def Lottery():
    Number = len(NameList)
    while Number > 0:
        Num = random.randint(0, len(NameList))
        print(NameList[Num - 1])
        NameList.pop(Num - 1)
        Number = Number - 1
    print('lole')


# Commands

NameAdding()
print(NameList)
Lottery()

