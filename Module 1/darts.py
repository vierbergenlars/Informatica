# Berekent de score van het darts-spel

# 2013 02 14

import math
x = float(input('X co�rdinaat'))
y = float(input('Y co�rdinaat'))

dist = math.hypot(x,y)
print "Score: ",

if dist < 0.5:
    print 10
else:
    dist-=0.5
    score = 9 - int(dist)
    if score < 0:
        score = 0
    print score
    
    
    
