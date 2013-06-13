# -*- coding: utf-8 -*-
"""
Created on Sat Jun  1 16:59:33 2013

@author: lars
"""

def sort(lst):
    for lim in range(len(lst)-1,0, -1):
        for i in range(lim):
            if lst[i] > lst[i+1]:
                lst[i], lst[i+1] = lst[i+1], lst[i]
    return lst
    
print sort([1,5,3,4])
