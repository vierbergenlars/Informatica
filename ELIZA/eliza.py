# -*- coding: utf-8 -*-
"""
Created on Wed May 15 08:40:53 2013

@author: lars
"""
import random

random_resp = []

def build_random_resp():
    random_resp.append("Ik begrijp het ...")
    random_resp.append("Hoe voel je je daarbij?")
    random_resp.append("Mooi weer vandaag")
    random_resp.append("Binnenkort examens...")

def start_chat():
    print "Welkom";
    build_random_resp()
    while True:
        a = raw_input('..>')
        r = generate_response()
        print r
        
def generate_response():
    i = int(random.unform(0, len(random_resp)))
    s = random_resp[i]
    return s
    
    
start_chat()
