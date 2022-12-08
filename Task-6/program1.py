# -*- coding: utf-8 -*-
"""
Created on Thu Dec  8 08:43:00 2022

@author: Rami
"""
def findDigits(n):
    
    string = str(n)
    arr = list()
    for i in string:
        arr.append(int(i))
    count = 0
    for i in range(len(arr)):
        if(arr[i]!= 0 and n% arr[i] == 0):
            count += 1
    return count
    