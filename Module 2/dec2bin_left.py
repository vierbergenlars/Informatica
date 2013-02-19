# Converts a decimal number to binary,  by continueing to add one to the binary value

try:
    dec = int(raw_input("Decimaal getal: "))
except ValueError:
    print "Een geheel nummer, aub!"
    raise

"""
Main loop
=========
Initialisation: dec is a decimal number entered by the user
Continuation: dec is not zero
Body:
    * set carry = True, start Carry loop

Carry loop
==========
Initialisation:
    * binary is a binary number (string representation)
    * pos is the bit position, counted from right
    * length is the length of the binary number
Continuation:
    * Carry flag is set OR pos <= length
Body:
    * If carry flag is set:
        * If pos in binary is not set
            * Set pos in binary to 1
            * Clear carry flag
        * If pos in binary is set
            * Set pos in binary to 0
            * Set carry flag
    * Set pos to pos +1
"""

"""
Gets the bit at the position pos
Args:
    * binary: a string representing a binary
    * pos: an integer representing the position of the bit counted from the right
Returns: bool
"""
def getpos(binary, pos):
    if pos < len(binary) and binary[-(pos+1)] == "1":
        return True
    return False

"""
Sets the bit at position pos
Args:
    * binary: a string representing a binary
    * pos: an integer representing the position of the bit counted from the right
    * bit: bool, the value to set the bit to
Returns: string, the new binary representation
"""
def setpos(binary, pos, bit):
    length = len(binary)
    if bit:
        num = "1"
    else:
        num = "0"

    if pos < length:
        return binary[:length - (pos+1)] + num + binary[length - (pos+1) +1:]
    else:
        fill = ""
        while pos > length:
            fill += "0"
            length += 1
        return num + fill + binary
    
def add_one(binary):
    carry = True
    length = len(binary)
    pos = 0

    # Carry loop
    while pos <= length or carry:
        if carry:
            if not getpos(binary, pos):
                binary = setpos(binary, pos, True)
                carry = False
            else:
                binary = setpos(binary, pos, False)
                carry = True
        pos += 1
    return binary



global dec
binary = "0"
negative = (dec < 0)
# Main loop
while dec != 0:
    binary = add_one(binary)
    if negative:
        dec += 1
    else:
        dec -= 1

if negative:
    sign = "-"
else:
    sign = ""
print sign+"0B"+binary

        
        
