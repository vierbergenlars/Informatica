# -*- coding: utf-8 -*-
"""
Created on Tue Mar  5 11:59:15 2013

@author: Lars Vierbergen
"""

from SpecificationLibrary import *

def rearrange(lst):
    assert isinstance(lst, list)
    assert (len(lst) % 2 == 0)
    assert for_all(lst, lambda x:  isinstance(x, int) and x !=0)
    # Even veel jongens als meisjes
    assert for_n(lst, len(lst)/2, lambda x: x>0)
    
    # Alle elementen op een even positie moeten een ander teken hebben dan
    # het element op de volgende positie
    assert for_all(range(len(lst),2), lambda i: lst[i] * lst[i+1] < 0)
    