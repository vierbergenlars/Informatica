# -*- coding: utf-8 -*-
"""
Created on Mon Mar  4 15:08:34 2013

@author: Lars Vierbergen
"""

def power(x, n):
    """
    Raises x to the power of n
    """
    # @require x is integer
    # @require n is a positive integer
    # @return The n-th power of x, integer
    # @loop Multiply x by itself, n times
    #       x*x*..*x 
    #           \ --> n times
    
    mult = 1
    while n > 0:
        mult*=x
        n-=1
    
    return mult