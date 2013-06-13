# -*- coding: utf-8 -*-
"""
Created on Sat Jun  1 17:16:32 2013

@author: lars
"""

# Merge sort

def sort(lst):
    sortRec(lst, 0, len(lst)-1)
    return lst
    
def sortRec(lst, start, end):
    if start < end:
        mid = (start+end)//2
        sortRec(lst, start, mid)
        sortRec(lst, mid+1, end)
        merge(lst, start, mid, end)
        
def merge(lst, start, mid, end):
    cpy = lst[:]
    i = start # Index lijst 1
    j = mid+1 # Index lijst 2
    
    k = i # Samengevoegde lijst index
    while k <= end:
        if i > mid: # Lijst 1 uitgeput
            lst[k] = cpy[j]
            j+=1
        elif j > end: # Lijst 2 uitgeput
            lst[k] = cpy[i]
            i+=1
        elif cpy[i] < cpy[j]:
            # Volgend elem lijst 1 < dan volgend elem lijst 2
            lst[k] = cpy[i]
            i+=1
        elif cpy[i] > cpy[j]:
            # Volgend elem lijst 2 < dan volgend elem lijst 1
            lst[k] = cpy[j]
            j+=1
        k+=1
    
        