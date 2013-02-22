# -*- coding: utf-8 -*-
"""
Created on Thu Feb 21 17:20:01 2013

@author: Lars Vierbergen
"""

# Imports the file 'sortedList.py' and registers all its functions under
# the namespace `sortedList`
import sortedList

def merge(lst1, lst2):
    """Merges two sorted lists `lst1` and `lst2`
    
    Returns a sorted list where `lst1` and `lst2` are merged and deduplicated
    """
    
    # Check if both lists are sorted (function sorted() in sortedList.py)
    # Return false if the lists are not sorted
    if not sortedList.sorted(lst1) or not sortedList.sorted(lst2):
        return False
    # The variable that will hold the merged list.
    ret = []
    # While both lists still have elements...
    while len(lst1) > 0 and len(lst2) > 0:
        # ...and the first number in `lst1` is greater than the first number
        # in `lst2`: append the first value of `lst2` to the `ret` list, but
        # only when the `ret` list does not yet contain that value
        # and remove the first number from `lst2`
        if lst1[0] > lst2[0]:
            append_if_not_exists(ret, lst2[0])
            lst2 = lst2[1:]
        # ...and the first number in `lst1` is smaller than the first number
        # in `lst2`: append the first value of `lst1` to the `ret` list, only
        # if the `ret` list does not yet contain that value.
        # Remove the first number from `lst1`
        elif lst1[0] < lst2[0]:
            append_if_not_exists(ret, lst1[0])
            lst1 = lst1[1:]
        # ...and both lists have the same first number: append the first
        # value of the lists to the `ret` list, if that list does not yet
        # contain the value.
        # Remove the first number from both lists
        elif lst1[0] == lst2[0]:
            append_if_not_exists(ret, lst1[0])
            lst1 = lst1[1:]
            lst2 = lst2[1:]
    # Else, when one or both lists have run out of elements...
    # ...if `lst1` is empty, append each value of `lst2` to the `ret` list,
    # but only if it is not yet in the `ret` list.
    if len(lst1) == 0:
        for i in lst2:
            append_if_not_exists(ret, i)
    # ... if `lst2` is empty, append each value of `lst1` to the `ret` list,
    # but only if it is not yet in that list.
    if len(lst2) == 0:
        for i in lst1:
            append_if_not_exists(ret, i)
    # Return the merged list
    return ret

def append_if_not_exists(lst, el):
    """Appends the element `el` to the list `lst` if it is not
    yet in the list. Does nothing if the element already is in the list.
    """
    if el not in lst:
        lst.append(el)
