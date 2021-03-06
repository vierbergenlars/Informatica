# Maakt een willekeurig getal aan en laat de gebruiker het getal raden.
# Getallen liggen in het bereik 1 - 100
# De gebruiker begint met 25 punten. Bij elke nieuwe poging wordt het resultaat gehalveerd (en naar boven afgerond)
# Wanneer er geen punten meer over zijn, is het spel verloren
# Wanneer het getal geraden is voordat de punten 0 zijn, heeft de gebruiker gewonnen

import random

# random() genereert getallen van 0.0 tot 1.0
# Omdat 0 niet tot de mogelijkheden behoort, doen we +1
# De gegenereerde getallen zijn altijd < 1.0, dus we kunnen *100 doen
# (na int() wordt het toch naar beneden afgerond)
random = random.randint(1, 100)
# random = int(random.random()*100+1)

points = 25

"""
Diminish the points.
Be fair. Don't round down, but round up!
"""
def minpoints():
    global points
    if points %2 and points != 1:
        points = points//2 + 1
    else:
        points = points//2
    print "Nog", points, "punten over"


"""
Main loop
=========
Initialisation: points = 25
Continuation: points > 0
Stop criterion: correct guess
Body:
    * Ask user for a guess
    * Error when input is no integer, or smaller than 1 or greater than 100
    * Check guess
        * Correct guess --> Tell user he won, quit loop
        * Bad guess --> print higher/lower and diminish points

"""


# Game loop
while points > 0:
    usr_input = raw_input("Geef een getal: ")
    try:
        usr_input = int(usr_input)
    except ValueError:
        print "Een geheel getal AUB!",
        minpoints()
    else:
        if usr_input < 1 or usr_input > 100:
            print "Een getal tussen 1 en 100, AUB!",
            minpoints()
        elif usr_input == random:
            break
        elif usr_input < random:
            print "Hoger.",
            minpoints()
        elif usr_input > random:
            print "Lager.",
            minpoints()
        else:
            raise Exception, "Dafuq?!"
    
if points > 0:
    print "Proficiat! Uw punten zijn", points
else:
    print "Jammer,... Het getal was", random

        
