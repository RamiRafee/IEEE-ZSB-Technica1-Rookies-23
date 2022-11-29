# -*- coding: utf-8 -*-
"""
Created on Tue Nov 29 23:34:59 2022

@author: Rami
"""
print("input:")
n = int (input())
p = int (input())
print("OUTPUT:")

count = 0
if(p -1 < n - p and p != 1):
    for i in range(1,p+1):
        if( i % 2 == 0):
            count +=1
elif( p == 1 or p == n):
    count=0
elif( p - 1 > n - p and n%2 ==0):
    for i in range(n-1,p-1,-1):
        if(i %2 != 0 ):
            count += 1
elif( p - 1 >= n - p and n%2 !=0):
    for i in range(n-1 , p-1, -1):
        if(i%2 != 0):
            count += 1
print (count)
