# -*- coding: utf-8 -*-
"""
Created on Tue Feb 19 10:56:33 2013

@author: lars
"""

getal = raw_input("Geef een niet negatief geheel getal:")
while not getal.isdigit():
    getal = raw_input("Geef een niet negatief geheel getal:")
getal = int(getal)
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
while getal > 0:
    cijfer_som += (getal % 10)
    getal //= 10
    
print  cijfer_som