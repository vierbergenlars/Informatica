# -*- coding: utf-8 -*-
"""
Created on Tue Feb 19 11:37:42 2013

@author: lars
"""

getal = float(raw_input("Geef getal: "))

"""
Main loop
=========
Body:
    * Vervang huidige benadering door een betere benadering op basis van de 
      formule van Heron
Init:
    * Initialiseer benadering op waarde tussen 0 en getal
Cont:
Stop:
    * Gewenste precisie is bereikt
"""

benadering = getal/2.0
oude_benadering = benadering

while ((benadering*benadering-getal) > 1.0E-10) and (oude_benadering != benadering):
    oude_benadering = benadering
    benadering = (benadering + getal/benadering)/2.0

print benadering