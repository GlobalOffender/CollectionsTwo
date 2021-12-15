import random
Characters = 24
# Types
klein = ['a', 'b', 'c','d', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
groot = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R','S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
cijfer = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
teken = ['@', '#', '$', '%', '&', '_', '?']
klein2 = []
groot2 = []
cijfer2 = []
teken2 = []
password1 = []
password2 = []
password3 = []
# Randomizer
def GrR():
    global Characters
    Gr = random.randint(2,6)
    for x in range(Gr):
        Gr2 = random.randint(0,25)
        groot2.append(groot[Gr2])
    Characters = Characters - Gr
def TeR():
    global Characters
    for x in range(3):
        Te = random.randint(0,6)
        teken2.append(teken[Te])
    Characters = Characters - Te
def CiR():
    global Characters
    Ci = random.randint(4,7)
    for x in range(Ci):
        Ci2 = random.randint(0,9)
        cijfer2.append(cijfer[Ci2])
    Characters = Characters - Ci
def KlR():
    global Characters
    for x in range(Characters):
        Kl = random.randint(0,25)
        klein2.append(klein[Kl])

# Collector
GrR()
TeR()
CiR()
KlR()

# Randomizer 2

# Eerste 3 - Grote + Kleine
for x in range(3):
    random1 = random.randint(0,1)
    if random1 == 0:
        if len(groot2) > 0:
            password1.append(groot2.pop(-1))
        else:
            password1.append(klein2.pop(-1))
    else:
        password1.append(klein2.pop(-1))

# Laatste 3 - Grote + Kleine + Cijfers
for x in range(3):
    random1 = random.randint(0,2)
    if random1 == 0:
        if len(groot2) > 0:
            password3.append(groot2.pop(-1))
        else:
            password3.append(klein2.pop(-1))
    elif random1 == 1:
        password3.append(klein2.pop(-1))
    else:
        if len(cijfer2) > 0:
            password3.append(cijfer2.pop(-1))
        else:
            password3.append(klein2.pop(-1))

# Midden - Alles
password2.append(groot2 + klein2 + teken2 + cijfer2)
random.shuffle(password2)

# Result
print(password1 + password2 + password3)
