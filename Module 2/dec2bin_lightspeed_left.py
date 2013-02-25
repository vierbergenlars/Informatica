# -*- coding: utf-8 -*-
"""
Created on Mon Feb 25 22:39:20 2013

@author: Lars Vierbergen
"""

dec = int(raw_input('Geef een decimaal getal: '))

binary= ""
if dec < 0:
    # ~ is the NOT operator. It flips all bits from 0 to 1 and from 1 to 0
    # With decimal numbers, following effects occur: flip sign, decrement 1
    # We want to flip the sign, but not to decrement by one, so add one again
    # It is much faster than math.abs() or dec*-1
    dec = ~dec + 1
    sign = "-"
else:
    sign = ""

# `if dec` is a shorthand for `if dec != 0`. Makes use of type coercion
if dec:
    # The same again. Shorthand for `while dec != 0`. Since `dec` is always
    # positive over here, it is used instead of `while dec > 0`, which is slower
    while dec:
        # Gets the rightmost bit from the decimal representation.
        # & is the AND operator. Works like this:
        #     100101001
        #   & 101100101
        #    ----------
        #     100100001
        # Only setting the bits where bits of both numbers are 1
        # 
        # This operation discards all bytes but the rightmost one.
        # The result is stored in `rbit`
        rbit = dec & 1;
        
        # Prepend the bit we got to the binary.
        # Note the use of `str(rbit)' here that casts the int (0 or 1) in
        # `rbit` to str ("0" or "1"). Not sure if faster, but looks nicer,
        # don't you think? :p
        binary = str(rbit) + binary
        
        # Shift all bits in `dec` one place to the right, dividing the number
        # by two (but faster :D) Works like this:
        #     100101 --> 10010
        #     101010 --> 10101
        dec >>= 1;
# But when `dec` actually was 0, we still need a dirty hack to set the binary
# to str "0", or the final print will say "0b" instead of "0b0"
else:
    binary = "0"

# Now just put the whole thing together.
# The sign, "0b", and the binary are assembled and printed out.
print sign+"0b"+binary
    