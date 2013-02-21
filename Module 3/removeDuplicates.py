# -*- coding: utf-8 -*-
"""
Created on Thu Feb 21 17:00:07 2013

@author: Lars Vierbergen
"""

def remove_duplicates(lst):
    if not isinstance(lst, list):
        return False
    seen = []
    for i in lst:
        if i not in seen:
            seen.append(i)
    lst[:] = seen
    return True