# -*- coding: utf-8 -*-
"""
Created on Sat Jun  1 13:46:19 2013

@author: lars
"""

def exch(lst, a, b):
    lst[a], lst[b] = lst[b], lst[a]
    
# -----------------------------------------------------------------------------

# Selection sort
       
def sort(lst):
    sorted_end_idx = 0
    while sorted_end_idx < len(lst):
        smallest_idx = sorted_end_idx
        i = sorted_end_idx
        while sorted_end_idx < len(lst):
            if lst[i] < lst[smallest_idx]:
                smallest_idx = i
            i+=1
        exch(lst, sorted_end_idx, smallest_idx)
        sorted_end_idx += 1
    return lst

# -----------------------------------------------------------------------------

# Insertion sort
def sort(lst):
    i=0
    while i < len(lst):
        j = i
        while i > 0:
            if lst[j] < lst[j-1]:
                exch(lst, j, j-1)
            else:
                break
            j-=1
        i+=1
    return lst
                
# -----------------------------------------------------------------------------

# Bubble sort
def sort(lst):
    lim = len(lst)-1
    while lim > 0:
        i = 0
        while i < lim:
            if lst[i] > lst[i+1]:
                exch(lst, i, i+1)
            i+=1
        lim-=1
    return lst