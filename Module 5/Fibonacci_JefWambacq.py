"""
@author Jef Wambacq
"""

from SpecificationLibrary import *

def fibonacci(n):
    assert n >= 0
    
    if n == 0:
        return []
    elif n == 1:
        return [0]

    # len([0,2]) == 2
    # [0,1] == [0,1]
    lst = [0, 1]
    # len(lst) == 2
    # lst[0:2] == [0,1]
  
    i = 2
    # len(lst) == i
    # for_all(range(2, i), lambda x: lst[x] == lst[x - 2] + lst[x - 1]) and lst[0:2] == [0,1]
    
    while i != n:
        assert len(lst) == i
        assert for_all(range(2, i), lambda x: lst[x] == lst[x - 2] + lst[x - 1])
        # len(lst) == i
        # for_all(range(2, i), lambda x: lst[x] == lst[x - 2] + lst[x - 1]) and lst[0:2] == [0,1]
        nEl = lst[i - 2] + lst[i - 1]
        # len(lst) == i
        # for_all(range(2, i), lambda x: lst[x] == lst[x - 2] + lst[x - 1]) and nEl == lst[-1] + lst[-2] and lst[0:2] == [0,1]
        lst.append(nEl)
        # len(lst) == i+1
        # for_all(range(2, i+1), lambda x: lst[x] == lst[x - 2] + lst[x - 1]) and lst[0:2] == [0,1]
        i += 1
        # len(lst) == i
        # for_all(range(2, i), lambda x: lst[x] == lst[x - 2] + lst[x - 1]) and lst[0:2] == [0,1]
        

    # INVARIANT: len(lst) == i
    # INVARIANT: for_all(range(2, i), lambda x: lst[x] == lst[x - 2] + lst[x - 1]) and lst[0:2] == [0,1]
    # LOOP: i == n

    # len(lst) == n
    # for_all(range(2, n), lambda x: lst[x] == lst[x - 2] + lst[x - 1])
    assert len(lst) == n
    assert for_all(range(2, n), lambda x: lst[x] == lst[x - 2] + lst[x - 1])
        
    return lst

