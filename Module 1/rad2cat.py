# -*- coding: cp1252 -*-
# Zet polaire co�rdinaten om in cartesische co�rdinaten

# 2013 02 14

import cmath
r = float(raw_input('r='))
theta = float(raw_input('theta='))

z=cmath.rect(r, theta)

print "x=", z.real, "y=", z.imag
