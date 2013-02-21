# -*- coding: utf-8 -*-
"""
Created on Thu Feb 21 16:25:07 2013

@author: Lars Vierbergen
"""

def nb_occurences(el, lst):
    if not isinstance(lst, list):
        return 0
    cnt = 0    
    for lst_el in lst:
        if lst_el == el:
            cnt+=1
    return cnt