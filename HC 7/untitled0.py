# -*- coding: utf-8 -*-
"""
Created on Tue Mar  5 10:57:15 2013

@author: Lars Vierbergen
"""

# Say lambda functions!


# Define lambda function that returns the sum of the length of two strings
print (lambda str1, str2: len(str1) + len(str2))("Albert", "Paola")



import math
# Lambda function that returns one of the squares, is any of the equation
# ax^2 + bx + c = 0
print (lambda a,b,c: (-b + math.sqrt((b**2-4*a*c)/(2.0*a)))) (-1,4,5)



