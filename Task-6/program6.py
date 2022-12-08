# -*- coding: utf-8 -*-
"""
Created on Thu Dec  8 11:01:05 2022

@author: Rami
"""

def circularArrayRotation(a, k, queries):
    # Write your code here
    ans = [0]*len(a)
    res = []
    for i in range(len(a)):
        t = (i + k)%len(a)
        ans[t] = a[i]
        
    for i in queries:
        res.append(ans[i])
        print(ans[i])
    return res
print(circularArrayRotation([1, 2, 3], 2, [0,1,2]))