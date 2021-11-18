# Stap 1 - List - Boodschappen opslaan
list = {}
# Stap 2 - Order - Boodschappen opvragen
def order():
    vraag1 = str(input("Wat wilt u kopen? "))
    if vraag1 in list:
        list[vraag1] = list[vraag1] +1
    else:
        list[vraag1] = 1

# Stap 3 - Continue - Verder gaan
    vraag2 = input("Wilt u meer kopen? [Y/N]")
    if vraag2 == "y":
        order()
    else:
        print(list)
order()
# Stap 4  - Result - Bon
