# -*- coding: utf-8 -*-
"""
Created on Thu Feb 21 17:00:07 2013

@author: Lars Vierbergen
"""

def remove_duplicates(lst):
    """Removes duplicate entries from list `lst`
    
    [!] Modifies `lst` directly
    Returns False on error, True on success
    """
    # Check if they passed a list in the variable `lst`
    if not isinstance(lst, list):
        return False
    # Holds all values that have already passed
    seen = []
    
    # For each element `i` in the list `lst`:
    for i in lst:
        # If `i` is not yet in the list `seen` (up until now, there has been
        # no occurence of `i` in the list `lst`):
        # Append the element `i` to the list `seen`
        if i not in seen:
            seen.append(i)
    # `lst = seen` will break the reference to the object. The variable `lst`
    # won't be modified outside this function.
    # I use a little 'trick' to set the splice of `lst` from the first to the
    # last position to the values in `seen`.
    # This effectively causes all values in `lst` to be replaced by all
    # values in the list `seen` without beaking the reference.
    lst[:] = seen
    return True
