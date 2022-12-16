# -*- coding: utf-8 -*-
"""
Created on Fri Dec 16 00:27:59 2022

@author: Rami
"""

def libraryFine(d1, m1, y1, d2, m2, y2):
    # Write your code here
    fine = 0
    if (y1 > y2):
        fine = 10000
    elif(y1<y2):
        return fine
    elif(m1 > m2):
        fine = 500 * (m1 - m2)
    elif(m1 < m2):
        return fine
    elif(d1 > d2):
        fine = 15 * (d1 - d2)
    return fine  