# Berekent de BMI aan de hand van het gewicht en de lengte van een persoon
# 2013 02 13

gewicht = float(input("Geef het gewicht: "))

if gewicht > 0 and gewicht < 300:
    lengte = float(input("Geef de lengte: "))

    if lengte > 0 and lengte < 3:

        bmi = gewicht/lengte**2


        if bmi < 18.5:
            cat = "Ondergewicht"
        elif bmi < 25.0:
            cat = "Normaal"
        elif bmi < 30.0:
            cat = "Overgewicht"
        else:
            cat = "Obesitas"

        print "De BMI bedraagt", bmi, "[",cat,"]"
    else:
        print lengte, "is een beetje vreemd... :/"
else:
    print gewicht, "wordt niet ondersteund"
