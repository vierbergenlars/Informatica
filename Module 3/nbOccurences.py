# -*- coding: utf-8 -*-
"""
Created on Thu Feb 21 16:25:07 2013

@author: Lars Vierbergen
"""

def nb_occurences(el, lst):
    """Counts the number of occurences of `el` in the list `lst`
    
    Returns 0 if `lst` is not a list
    """
    
    # # Loop invariant
    # @require `lst` is a list
    # @require `cnt` is zero
    # @return The number of occurences of `el` in the list
    # @loop:
    #   @while There are still unprocessed entries in the list
    #   @do Add one to the counter `cnt`
    
    # If `lst` is not a list, return 0.
    # Returning causes the function to stop now and return control to the
    # calling code.
    if not isinstance(lst, list):
        return 0
    # Initialize the times `el` was encountered to 0
    cnt = 0
    # For each element `lst_el` in the list `lst`
    for lst_el in lst:
        # If `lst_el` is the same thing as `el`, we have an occurence of the
        # element. Increase `cnt` by one
        if lst_el == el:
            cnt+=1
    # The for loop has ended. Return the number of occurences of `el`
    return cnt
