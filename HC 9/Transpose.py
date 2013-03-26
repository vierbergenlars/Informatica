# -*- coding: utf-8 -*-
"""
Created on Tue Mar 26 11:21:54 2013

@author: Lars Vierbergen
"""
from SpecificationLibrary import *
# Transponeert een willekeurige matrix
#
# - Gegeven moet zijn een willekeurige matrix
# - Geeft de getransponeerde matrix terug. Kolommen zijn naar rijen omgezet.
def transpose(matrix):
    transpose = [[0]*nb_rows(matrix) for i in range(nb_cols(matrix))]
    
    for idx_row in range(nb_rows(matrix)):
        for idx_col in range(nb_cols(matrix)):
            transpose[idx_col][idx_row] = matrix[idx_row][idx_col]
    
    
    assert for_all(range(nb_rows(matrix)), lambda idx_row: \
        for_all(range(nb_cols(matrix)), lambda idx_col: \
            transpose[idx_col][idx_row] == matrix[idx_row][idx_col]
        )
    )
    assert nb_cols(matrix) == nb_rows(transpose)
    assert nb_rows(matrix) == nb_cols(transpose)
    return transpose

def nb_rows(matrix):
    return len(matrix)
    
def nb_cols(matrix):
    return len(matrix[0])
    
def is_matrix(matrix):
    if not isinstance(matrix, list):
        return False
    for row in range(0,nb_rows(matrix)):
        if not isinstance(matrix[row], list):
            return False
        if len(matrix[row]) != nb_rows(matrix):
            return False
    return True
    
