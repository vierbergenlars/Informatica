# Converts a decimal number to binary, starting from the left, working to the right
dec = int(raw_input("Decimaal getal: "))

"""
Main loop
=========
Initialisation:
    * p is set so 2**p the lowest number for which 2**p > dec
    * dec is user input
Continuation: p is not smaller than 0
Body:
    * If the decimal minus 2 to the power of p is greater than 0
        * Append 1 to the binary number
        * Reduce the decimal number by 2**p
    * else
        * Add 0 to the binary number
    * Recude the power of 2 by one

Maximum loop
============
Initialisation: dec is user input, p = 0
Continuation: 2**p is smaller than dec
Body:
    * Add one to p
"""

p = 0

negative = (dec < 0)
dec = abs(dec)

while 2**p < dec:
    p+=1


binary = ""

while p >= 0:
    if dec - 2**p >= 0:
        binary+="1"
        dec-=2**p
    else:
        binary+="0"
    p-=1
if negative:
    sign = "-"
else:
    sign = ""
print sign+"0b"+binary

