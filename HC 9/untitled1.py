# -*- coding: utf-8 -*-
"""
Created on Tue Mar 26 10:40:57 2013

@author: Lars Vierbergen
"""
from SpecificationLibrary import *
# Ga na of de gegeven matrix een benedendriehoeksmatrix is.
#
# - De gegeven matrix moet een vierkante matrix zijn.
# - Waar indien en alleen indien alle elementen boven de hoofddiagonaal
#   gelijk zijn aan 0.
def is_benedendriehoeksmatrix(matrix):
    assert is_vierkante_matrix(matrix)
    row = 0
    is_beneden = True
    while row < nb_rows(matrix):
        # Alle elementen boven de hoofddiagonaal van de reeds behandelde
        # rijen zijn gelijk aan 0.
        col = row + 1 # Starten voorbij de hoofddiagonaal
        while col < nb_cols(matrix):
            # Alle elementen boven de hoofddiagonaal van de huidige rij tot 
            # aan de huidige kolom zijn 0.
            if matrix[row][col] != 0:
                is_beneden = False
            col += 1
        row += 1 
    assert is_beneden == for_all(range(0,nb_rows(matrix)), \
        lambda i: for_all(range(i+1, nb_cols(matrix)), \
            lambda j: matrix[i][j] == 0))
    return is_beneden
        
def nb_rows(matrix):
    return len(matrix)
    
def nb_cols(matrix):
    return len(matrix[0])

def is_vierkante_matrix(matrix):
    if not isinstance(matrix, list):
        return False
    for row in range(0,nb_rows(matrix)):
        if not isinstance(matrix[row], list):
            return False
        if len(matrix[row]) != nb_rows(matrix):
            return False
    return True
        
        
    
assert is_benedendriehoeksmatrix([[1,0,0],[2,3,0],[4,5,6]])
assert not is_benedendriehoeksmatrix([[1,0,-100],[2,3,0],[4,5,6]])
assert is_benedendriehoeksmatrix([[1]])