# -*- coding: utf-8 -*-
"""
Created on Thu Mar 14 17:09:51 2013

@author: Lars Vierbergen
"""

def get_fib_at(n):
    # 0 + 1 is 1e fib getal, 0 = 0-e fibon getal
    prev1 = 1
    prev2 = 0
    # 0 + prev1 is 1e fib getal, 0 = 0-e fibon getal
    fib = 0
    # fib + prev1 is 1e fib getal, fib = 0-e fibon getal
    i = 0
    # fib + prev1 is i+1e fib getal, fib = i-e fibon getal, prev1 = i-1e fibon getal
    while i != n:
        # fib + prev1 is i+1e fib getal, fib = i-e fibon getal, prev1 = i-1e fibon getal
        prev2 = prev1
        # fib + prev2 is i+1e fib getal, fib = i-e fibon getal, prev2 = i-1e fibon getal
        prev1 = fib
        # prev1 + prev2 is i+1e fib getal, prev1 = i-e fibon getal, prev2 = i-1e fibon getal
        fib = prev1 + prev2
        # fib is i+1e fib getal, prev1 = i-e fibon getal, prev2 = i-1e fibonacci getal
        i+=1
        # fib is i-e fibonacci getal, prev1 = i-1e fibon getal, prev2 = i-2e fibonacci getal
        
    return fib

def fibonacci(n):
    fibon = [0,1]
    # fibon[2-1] + fibon[2-2] is het 2-e fibonacci getal
    # ==> fibon[1]+ fibon[0] is het 2-de fibonacci getal (== 1)
    i = 2 # Skip the first two, since they are already known
    # fibon[i-1] + fibon[i-2] is het i-e fibonacci getal
    while i < n:
        # fibon[i-1] + fibon[i-2] is het i-e fibonacci getal (definitie fibonacci-getal)
        fibon.append(fibon[i-1] + fibon[i-2]) # Because fibon[i] = fibon[i-1] + fibon[i-2] raises an IndexError.
        # fibon[i+1] is het i+1-e fibonacci getal => fibon[i] is het i-e fibonacci getal
        i+=1
        # fibon[i] is i-e fibonacci getal
    return fibon[:n] # When n < 2, we need only the first n elements.
    
        