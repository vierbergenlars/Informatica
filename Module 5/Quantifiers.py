from SpecificationLibrary import *
import random

# Return a random list of integer numbers whose value is in between
# the given minimum and maximum value. The number of elements
# in the list is also chosen in a randam way, but will not exceed
# the given maximum number of elements.
def random_list(min_value, max_value, max_nb_elements):
    assert isinstance(min_value,int) and isinstance(max_value,int) and (min_value < max_value)
    assert isinstance(max_nb_elements,int) and (max_nb_elements > 0)
    nb_elements = random.randint(0,max_nb_elements)
    seq = []
    for i in range(0,nb_elements):
        assert len(seq) == i
        seq = seq + [int(random.randint(min_value,max_value))]
    assert (len(seq) == nb_elements)
    return seq

lst = random_list(-100,100,20)
print lst

# Write a boolean expression checking whether all elements in the list
# are negative, and print the result of that boolean expression.
print "All negative: ", for_all(lst, lambda x: x < 0)

# Write a boolean expression checking whether at least one element in
# the list is zero, and print the result of that boolean expression.
print "At least one zero:", for_some(lst, lambda x: x == 0)

# Write a boolean expression checking whether at least one element in
# the list is a mutliple of 10, and print the result of that boolean expression.
print "At least one mutiple of 10:", for_some(lst, lambda x: x%10 == 0)

# Write a boolean expression checking whether the largest element in
# the list exceeds 13, and print the result of that boolean expression.
print "At least one element exceeding 13:", for_some(lst, lambda x: x > 13)

# Write a boolean expression checking whether each positive element is
# not immediately followed by another positive element, and print the
# result of that boolean expression.
print "No two consecutive positives:", for_all(range(len(lst)-1), lambda i: not (lst[i] > 0 and lst[i+1] > 0))

# Write a boolean expression checking that odd numbers are only stored
# at odd positions in the list, and print the result of that boolean expression.
print "Odd numbers only at odd positions:", for_all(range(len(lst)), lambda i: not (lst[i]%2 ==1 and i%2 == 0))
