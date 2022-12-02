# -*- coding: utf-8 -*-
"""
Created on Fri Dec  2 21:26:02 2022

@author: Rami
"""

print("INPUT:")
s1 = input()
s2 = input()
print("OUTPUT")
found = False
count = 0
for i in range(len(s2)):
    if(s1.count(s2[i])>0):
        count+=1
        if(count == len(s1)):
            found = True
            print("true")
            break
    else:
        count = 0
if( not found):
    print("false")