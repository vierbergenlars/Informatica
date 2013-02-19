# Programma dat bepaald of een getal even, oneven of nul is
#
# 2013 02 14

number = float(raw_input('Getal: '))

if not number.is_integer():
    print "Geef een geheel getal!"

elif number == 0:
    print "Nul"
elif number%2:
    print "Oneven"
else:
    print "Even"
