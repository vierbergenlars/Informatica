from SpecificationLibrary import *

# Return the flattened form of a set of tuples.
#    The flattened form of a set of tuples is the set of all elements that are
#    part of at least one of the tuples of the given set. 
#
#   - The given sett must be a set of tuples.
#   - The resulting set is equal to the union of all the tuples in the given set.
def flatten(sett):
    assert isinstance(sett, set)
    assert for_all(sett, lambda x: isinstance(x, tuple))
    copy = sett.copy()
    flattened = set()
    removed_tuples = []
    while len(copy) != 0:
        assert for_all(removed_tuples, lambda x: for_all(x, lambda x: x in flattened))
        i = 0
        elem = copy.pop()
        removed_tuples.append(elem)
        while i != len(elem):
            flattened.add(elem[i])
            i+=1
        assert for_all(elem, lambda x: x in flattened)

    return flattened

assert flatten({(1,2),(3,4,2),(1,6,5)}) == {1,2,3,4,5,6}

assert flatten(set([])) == set([])

assert flatten({ ((2,3),5),("abc","def"),((2,3),"abc")}) == {(2,3),5,"abc","def"}
