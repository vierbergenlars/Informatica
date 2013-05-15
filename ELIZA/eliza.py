# -*- coding: utf-8 -*-
"""
Created on Wed May 15 08:40:53 2013

@author: lars
"""

def start_chat():
    print "Welkom";
    while True:
        a = raw_input('..>')
        r = generate_response()
        print r
        
def generate_response():
    s = "Ik begrijp het..."
    return s