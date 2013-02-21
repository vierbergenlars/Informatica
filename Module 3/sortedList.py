# -*- coding: utf-8 -*-
"""
Created on Thu Feb 21 16:42:57 2013

@author: Lars Vierbergen
"""

def sorted(lst):
    if not len(lst):
        return True
    smallest = lst[0]
    for el in lst:
        if el < smallest:
            return False
        smallest = el
    return True