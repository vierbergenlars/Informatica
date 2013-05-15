# -*- coding: utf-8 -*-
"""
Created on Wed May 15 08:40:53 2013

@author: lars
"""

random_resp = []

def build_random_resp():
    random_resp.append('Ik begrijp het ...")
    random_resp.append("Hoe voel je je daarbij?")
    random_resp.append("Mooi weer vandaag")

def start_chat():
    print "Welkom";
    while True:
        a = raw_input('..>')
        r = generate_response()
        print r
        
def generate_response():
    s = "Ik begrijp het..."
    return s