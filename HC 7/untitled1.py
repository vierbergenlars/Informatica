# -*- coding: utf-8 -*-
"""
Created on Tue Mar  5 11:01:58 2013

@author: Lars Vierbergen
"""

from SpecificationLibrary import *

lst = ["Kanji", "Maarten", "Jeroen", "Sibren", "Elke", "!Elke", "Helen",
       "Louis", "Bram", "Jeroen", "Pieter", "Niels", "Wannes", "Viktor"]

# List has at least 10 elements
assert len(lst) >=10

# At least one name occurs more than one time in the list
assert for_some(lst, lambda x: lst.count(x) > 1)

# All the first names are at least 5 chars long
assert for_all(lst, lambda x: len(x) >=5)

# At least one first name occurs at 2 successive positions in the list.
assert for_some(range(len(lst)-1), lambda i: lst[i] == lst[i+1])

# Exactly 3 first names in the list terminate with a vowel
assert for_n(lst,3, lambda x: x[-1] in 'aeiou')

# All first names at the opposite positions in the list (0,-1), (1,-2)
# differ from each other.
assert for_all(range(len(lst)), lambda i: lst[i] != lst[-i-1])