# -*- coding: utf-8 -*-
"""
Created on Tue Feb 19 10:56:33 2013

@author: lars
"""

getal = raw_input("Geef een niet negatief geheel getal:")
while not getal.isdigit():
    getal = raw_input("Geef een niet negatief geheel getal:")

"""
Main loop
=========

Body:
    * Verhoog de voorlopige som met de waarde van het huidige cijfer
Init:
    * Zet de voorlopige som op 0
Cont:
    * Neem het huidige cijfer weg uit het getal
Stop:
    * Er zijn geen cijfers meer
"""

print "De som van de cijfers van", getal, "bedraagt:",
cijfer_som = 0
positie = 0
while positie < len(getal):
    cijfer_som += int(getal[positie])
    positie += 1    
print  cijfer_som