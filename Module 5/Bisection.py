# Ik heb zelf geen enkel idee waar ik dit vandaan gehaald heb....

from math import *
from inspect import *

# Returns an interval which contains at least one root of a given function in the given interval [low,high].
# - f is een routine
# - low is kleiner dan high
# - f(low) heeft een ander teken dan f(high)
def get_root_interval(f,low,high,precision):
    # PRECONDITION
    assert isroutine(f)
    assert isinstance(low, float) and isinstance(high, float) and low <= high
    assert isinstance(precision, float) and precision > 0.0
    assert sign(f(low)) != sign(f(high))
    lower_bound = low
    upper_bound = high
    
    while upper_bound-lower_bound > precision:
        assert sign(f(lower_bound)) != sign(f(upper_bound))
        assert low <= lower_bound <= upper_bound <= high
        
        middle = lower_bound + (upper_bound-lower_bound)/2
        if sign(f(middle)) == sign(f(lower_bound)):
            lower_bound = middle
        else:
            upper_bound = middle
        
        assert sign(f(lower_bound)) != sign(f(upper_bound))
        assert low <= lower_bound <= upper_bound <= high
        
    # POSTCONDITION
    assert sign(f(lower_bound)) != sign(f(upper_bound))
    assert low <= lower_bound <= upper_bound <= high
    assert 0 <= upper_bound-lower_bound <= precision
    return (lower_bound,upper_bound)



# Return the sign of the given value.
#   - The given value must be a floating point value different from NAN.
#   - If the given value is negative, -1 is returned. If it is positive, +1 is
#     returned. If it is zero, 0 is returned.
def sign(x):
    assert isinstance(x,float) and (not isnan(x))
    if x < 0.0:
        return -1
    elif x > 0.0:
        return +1
    else:
        return 0



#####################
# TESTS
#####################

EPS = 0.1E-10
(low,high) = get_root_interval(lambda x:x,-5.0,5.0,EPS)
assert -EPS <= low
assert high <= +EPS


EPS = 0.1E-05
(low,high) = get_root_interval(sin,3.0,4.0,EPS)
assert pi-EPS <= low
assert high <= pi+EPS

EPS = 0.1E-07
(a,b) = get_root_interval(lambda x: (x+2)*(x-4)*x,-20.0,6.0,EPS)
root = (a+b)/2
assert (-2.0-EPS <= root <= -2.0+EPS) or\
       (-0.0-EPS <= root <= +0.0+EPS) or\
       (+4.0-EPS <= root <= +4.0+EPS) 
