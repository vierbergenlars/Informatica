# Approximates e


"""
Main loop
=========
Initialisation: e = 0, mult = 1.0
Continuation: Do it for all numbers from 1 to 50
Body:
    * Multiply mult by the number of loops that have been run
      (The 1st time, this calculates 1!, the 2nd time 2!, 3rd 3!, ...)
    * Add 1/mult to the approximation of e
      ( 1st time 1, 2nd time +1/2!, 3rd time +1/3!, ...)
"""
e = 1.0
mult= 1.0
for num in range(1,50):
    mult *= num
    e += 1.0/mult

print e
