# -*- coding: utf-8 -*-
"""
Created on Thu Dec  8 11:26:19 2022

@author: Rami
"""

def beautifulTriplets(d, arr):
    # Write your code here
    num = 0
    for i in range(len(arr)):
        for j in range(i+1,len(arr)):
            if(arr[j] - arr[i] != d ):continue
            for k in range(j+1,len(arr)):
                if( arr[k] - arr[j]  == d):
                    num += 1
    return num
