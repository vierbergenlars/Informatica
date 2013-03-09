# -*- coding: utf-8 -*-
"""
Created on Mon Mar  4 15:08:34 2013

@author: Lars Vierbergen
"""

def power(x, p):
    """
    Raises x to the power of p
    """
    # @require x is integer
    # @require n is a positive integer
    # @return The n-th power of x, integer
    
    mult = 1
    n=p
    while n > 0:
        # mult*(x**n) = (x**p)
        mult*=x
        n-=1
    
    return mult