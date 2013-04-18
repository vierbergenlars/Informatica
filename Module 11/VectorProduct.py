from SpecificationLibrary import *

# Compute the product of two sparse vectors.
def vector_product(left,right):
    result = 0
    for k in set(left.keys()) | set(right.keys()):
        sum_k = left.get(k, 0) * right.get(k, 0)
        if sum_k:
            result += sum_k
    return result

# Check whether the given vector is a sparse vector.
#
#   - True if and only if the given vector is a dictionary, with non-negative
#     integer values as keys.
def is_sparse_vector(vector):
    if not isinstance(vector,dict):
        return False
    for key in vector.keys():
        if not isinstance(key,int) or (key < 0):
            return False
    return True


# Return the length of a sparse vector.
def length(vector):
    if vector == {}:
        return 0
    return max(vector.keys())+1


vector1 = { 4:2, 10:7, 23:9}
vector2 = { 1:4, 10:3, 112:10}
assert vector_product(vector1,vector2) == 21

vector3 = { 4:-2, 10:1, 20:6}
assert vector_product(vector1,vector3) == 3

vector4 = { 5:6, 12:-7 }
assert vector_product(vector1,vector4) == 0

assert vector_product(vector1, {}) == 0


    
