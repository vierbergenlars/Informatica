# -*- coding: utf-8 -*-
"""
Created on Sat Jun  1 14:58:23 2013

@author: lars
"""

def sort(lst):
    for i in range(len(lst)):
        for j in range(i,0,-1):
            if lst[j] < lst[j-1]:
                lst[j], lst[j-1] = lst[j-1], lst[j]
            else:
                break
    return lst
                
print sort([2,3,1])
