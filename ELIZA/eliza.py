# -*- coding: utf-8 -*-
"""
Created on Wed May 15 08:40:53 2013

@author: lars
"""
import random
import string

random_resp = []
programmed_resp = {}

def build_random_resp():
    random_resp.append("Ik begrijp het ...")
    random_resp.append("Hoe voel je je daarbij?")
    random_resp.append("Mooi weer vandaag")
    random_resp.append("Binnenkort examens...")
    
def build_programmed_resp():
    programmed_resp["python"] = "Leuke programmeertaal?"
    programmed_resp["leuven"] = "Leuke stad!"
    programmed_resp["gent"] = "Lelijke stad"
    programmed_resp["antwerpen"] = "Parking"
    programmed_resp["vervelen"] = "Blok dan een beetje"
    programmed_resp["verveling"] = "Blok dan een beetje"


def start_chat():
    print "Welkom";
    build_random_resp()
    build_programmed_resp()
    while True:
        a = raw_input('..>')
        w = process_string(a)
        r = generate_response(w)
        print r
        
def generate_response(words):
    i = int(random.uniform(0, len(random_resp)))
    s = random_resp[i]

    for w in words:
        if w in programmed_resp:
            s = programmed_resp[w]
    
    return s
    
    
def process_string(s):
    s = string.lower(s)
    s = string.strip(s, "?!.")
    words = string.split(s)
    return words
    
start_chat()
