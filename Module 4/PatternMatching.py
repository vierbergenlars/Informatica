# -*- coding: utf-8 -*-
"""
Created on Mon Mar  4 19:35:28 2013

@author: Lars Vierbergen
"""

def matches(word, pattern):
    """
    Checks if a given word matches a pattern
    Operations:
        `=`: Matches the same char as the position before
        `!`: Matches all chars, except the char at the previous position
    """
    
    # @require word is a string
    # @require pattern is a string, starts with a normal char. Same number of
    #   letters as word
    # @require prev_char Is the previous char from the pattern
    # @return bool. True if the pattern matches, False if not
    # @loop:
    #   For each character in word, select the char at the same position in 
    #   pattern. If the char from pattern is "=", ensure that the char from word
    #   is the same as prev_char. If the char from pattern is "!", ensure that
    #   the char from word is not the same as prev_char. Else ensure the char from
    #   pattern is the same as the char from word, and set prev_char to the current
    #   char of pattern
    
    prev_char = None
    pos = 0
    while pos < len(word):
        word_char = word[pos]
        pat_char = pattern[pos]
        
        if pat_char == '=': # If the same char is required, just set it.
            pat_char = prev_char
            
        if pat_char == '!': # pattern says: must not match
            if word_char == prev_char: # So, if they match return False
                return False
        else: # pattern says: must match
            if word_char != pat_char: # So, if they don't match, return False
                return False
        prev_char = word_char
        pos+=1
    return True # If we got here, everything has matched
            