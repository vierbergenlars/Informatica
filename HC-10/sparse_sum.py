# -*- coding: utf-8 -*-
"""
Created on Wed Mar 27 10:19:48 2013

@author: Lars Vierbergen
"""

# Berekent de som van de gegeven sparse vectoren
#
# - Beide vectoren moeten sparse vectoren zijn
# - De resulterende vector is een sparse vector waarvan elk element gelijk is
#   aan de som van de corresponderende elementen uit de gegeven vectoren. De
#   resulterende vector heeft geen enkel koppel waarvan de waarde gelijk is aan
#   nul.
def vector_sum(left, right):
    result = {}
    for k in range(max(left.keys()+right.keys())+1):
        sum_k = left.get(k,0) + right.get(k, 0)
        if sum_k:
            result[k] = sum_k
    return result
 
assert vector_sum({3:10,5:-7,12:100}, {3:12,5:7,124:200}) == {3:22,12:100,124:200}
