# Berekent de score van het darts-spel

# 2013 02 14

import math
x = float(input('X coördinaat'))
y = float(input('Y coördinaat'))

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
    
    
    
