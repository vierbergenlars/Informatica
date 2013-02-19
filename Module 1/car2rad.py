# Zet cartesische coordinaten om in polaire coordinaten

# 2013 02 14

import cmath

x = float(raw_input('x='))
y = float(raw_input('y='))

z = complex(x, y)

(r, theta) = cmath.polar(z)

print "r=", r, "theta=", theta
