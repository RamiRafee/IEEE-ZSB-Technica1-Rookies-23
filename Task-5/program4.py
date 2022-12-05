# -*- coding: utf-8 -*-
"""
Created on Tue Dec  6 00:14:33 2022

@author: Rami
"""

print("input:")
x = int(input())
print("OUTPUT:")
i = 2
while(i <= x **(1/2)):
    while(x%i == 0):
        print(i,end=" ")
        x = x /i
    i += 1
#if x is prime
if x:
    print(int(x))

