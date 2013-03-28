# -*- coding: utf-8 -*-
"""
Created on Wed Mar 27 09:25:08 2013

@author: Lars Vierbergen
"""
# Bereken de machtsverzameling van de gegeven verzameling
#
# - The given sett must be set or frozen set
# - The resulting set will have as elements all possible subsets that
#   can be taken from the given sett
from SpecificationLibrary import *
def power_set(sett):
    result = set([()])
    for element in sett:
      new_tuples = set()
    	for tup in result:
    	    new_tuples.add(tup+(element,))
	    result = result | new_tuples # union
    # Het element moet een deelverzameling zijn van sett
    assert for_all(results, lambda element: sett.issuperset(element))
    assert len(result) = 2**len(sett)
    return result


print power_set(set([1,2,5]))
