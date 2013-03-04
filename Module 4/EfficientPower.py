# -*- coding: utf-8 -*-
"""
Created on Mon Mar  4 15:18:09 2013

@author: Lars Vierbergen
"""

def power(x, n):
    """
    Raises x to the n-th power
    """
    # @require x is integer
    # @require n is positive integer
    # @return the n-th power of x
    # @loop:
    #   If n is a multiple of 2: x**n == (x*x)**(n/2)
    #   Else, just multiply once
    #   Stop when n is zero
    
    mult = 1
    while n > 0:
        if n&1: # n%2 == 1
            mult*=x
            n&=~1 # n-=1
        else:
            n>>=1 # n//=2
            mult*=power(x, n)

    return mult            
        