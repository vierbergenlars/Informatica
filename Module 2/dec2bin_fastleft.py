# Calculates the binary value of a decimal number from right to left

dec = int(raw_input("Decimaal getal: "))

"""
Main loop
=========
Initialisation:
    * dec is the absolute value of the input
    * binary is empty
Continuation: dec is not smaller than 0
Body:
    * Prepend the remainder of dec/2 to the binary number
    * Divide dec by 2
"""

binary = ""
negative = (dec < 0)
dec = abs(dec)
while dec >= 0:
    if dec%2:
        binary = "1" + binary
    else:
        binary = "0"+binary
    dec//=2

if negative:
    sign = "-"
else:
    sign = ""
print sign+"0b"+binary

    
