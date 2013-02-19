# -*- coding: utf-8 -*-
"""
Created on Tue Feb 19 15:02:18 2013

@author: lars
"""

data_list = [0,0,0,0,0,0,0,0,0]

def getData(num):
    return data_list[num]

def setData(i, data):
    print "Set", i, "to ", data
    data_list[i] = not not data

def main():
    for i in range(1,7):
        setData(i, i == 7)
    led7 = getData(1)
    for j in range(2):
        for i in range(7,2, -1):
             setData(i, getData(i+1))
        setData(7, led7)
main()
        