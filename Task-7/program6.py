# -*- coding: utf-8 -*-
"""
Created on Fri Dec 16 00:28:48 2022

@author: Rami
"""

def kaprekarNumbers(p, q):
    # Write your code here
    ans = []
    for i in range(p,q+1):
        r = len(str(i))
        temp = i**2
        string = str(temp)
        l = len(string) - r
        left = []
        right = []
        for j in range(l):
            left.append(string[j])
        if(left):
            left="".join(left)
            left = int(left)
        for j in range(l,len(string)):
            right.append(string[j])
        if(right):
            right="".join(right)
            right = int(right)
        if( left and right and left + right == i or i==1):
            ans.append(i)
    if(ans):
        for i in ans:
            print(i,end=" ")
    else:
        print("INVALID RANGE")