# Berekent de ggd van twee getallen

try:
    a = int(raw_input("a="))
    b = int(raw_input("b="))
except ValueError:
    print "F*ck U, geef een fatsoenlijk getal!"

"""
Main loop
=========
Initialisation: a, b is user input
Continuation: a is not equal to b
Stop criterion: Hit the loop limit, looping for more than 30 seconds is quite stupid
Body:
    * When a < b: switch a and b ( a > b > 0, for this algorithm to work
    * Set a = a - b
"""
i = 0
while a != b:
    i+=1
    if i > 10000000:
        raise Warning, "Too many loops! Bailing."

    if a < b:
        a,b = b,a
    a-=b

print i, "loops. Antwoord:", a
    
