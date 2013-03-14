# -*- coding: utf-8 -*-
"""
Created on Thu Mar 14 16:29:14 2013

@author: Lars Vierbergen
"""


a=40
assert 2*30 == 20 + a
b = 20
assert 2*30 == b +a
c = 30
assert 2*c == b + a
a,b,c = b,c,a
assert 2*b == a + c