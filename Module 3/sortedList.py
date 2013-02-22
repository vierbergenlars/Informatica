# -*- coding: utf-8 -*-
"""
Created on Thu Feb 21 16:42:57 2013

@author: Lars Vierbergen
"""

def sorted(lst):
    """Checks if a list `lst` is sorted
    
    Returns True if the list is sorted in increasing order, False if not
    """
    
    # If the length of the list is 0, the list is regarded as sorted.
    # This is a shortcut which uses boolean casting. `0`, `''` and `None` are
    # casted to `False`, all other values are casted to `True`
    # It is equivalent to `if not (len(lst) != 0)`, which is equivalent to
    # `if len(lst) == 0`
    if not len(lst):
        return True
    # Set the greatest value we have already encountered to the first value
    # of the list.
    greatest = lst[0]
    # For each element `el` in the list `lst`: ...
    for el in lst:
        # ... if the element is strictly smaller than the greatest element we
        # have already encountered, the list is not in increasing order.
        # Stop early and return False. Nothing in this function is executed
        # after this moment.
        if el < greatest:
            return False
        # Else, set the greatest number we have encountered to this element.
        # This is possible because `el` is either equal to or greater than
        # `greatest`. Smaller elements are already caught the line above.
        greatest = el
    # The function has not yet returned False, and the for loop has ended,
    # so we are sure the list is in increasing order. Return True.
    return True
