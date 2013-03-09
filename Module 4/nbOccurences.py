# -*- coding: utf-8 -*-
"""
Created on Thu Mar  7 16:05:22 2013

@author: Lars Vierbergen
"""

def occurence(el, lst):
    count = 0
    index = 0
    # count = occurence(el, lst[0:index])
    
    while index < len(lst):
        #count = occurence(el, lst[0:index])
        if lst[index] == el:
            #count +1 = occurence(el, lst[0:index + 1])
            count+=1
            # count = occurence(el, lst[0:index+1])
        else:
            # count = occurence(el, lst[0:index+1])
            count = count
            # count = occurence(el, lst[0:index+1])
        
        # count = occurence(el, lst[0:index]) and index = len(lst)
        # count = occurence(el, lst)
        return count