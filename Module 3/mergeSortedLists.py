# -*- coding: utf-8 -*-
"""
Created on Thu Feb 21 17:20:01 2013

@author: Lars Vierbergen
"""

import sortedList

def merge(lst1, lst2):
    if not sortedList.sorted(lst1) or not sortedList.sorted(lst2):
        return False
    ret = []
    while len(lst1) > 0 and len(lst2) > 0: 
        if lst1[0] > lst2[0]:
            append_if_not_exists(ret, lst2[0])
            lst2 = lst2[1:]
        elif lst1[0] < lst2[0]:
            append_if_not_exists(ret, lst1[0])
            lst1 = lst1[1:]
        elif lst1[0] == lst2[0]:
            append_if_not_exists(ret, lst1[0])
            lst1 = lst1[1:]
            lst2 = lst2[1:]
    if len(lst1) == 0:
        for i in lst2:
            append_if_not_exists(ret, i)
    if len(lst2) == 0:
        for i in lst1:
            append_if_not_exists(ret, i)
    return ret
    
def append_if_not_exists(lst, el):
    if el not in lst:
        lst.append(el)