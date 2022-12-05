# -*- coding: utf-8 -*-
"""
Created on Tue Dec  6 00:03:09 2022

@author: Rami
"""

print("INPUT:")
x = int(input())
print("OUTPUT:")
while (True):
    s = 0
    
    while(x > 0):
        s = s + (x%10)**2
        x = x // 10
    
    if ( s == 1):
        print("true")
        break
    #if it is an infinity loop it will always has 37 in it
    elif(s == 37):
        print("false")
        break
    x = s
    s = 0