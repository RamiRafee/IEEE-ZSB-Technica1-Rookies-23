# -*- coding: utf-8 -*-
"""
Created on Fri Dec  2 21:34:05 2022

@author: Rami
"""
print("INPUT:")
ls = input().split()
print("OUTPUT:")
for i in range(len(ls)):
    ls[i] = int(ls[i])
ans = len(ls)
for i in range(len(ls)):
    for j in range(i+1,len(ls)):
        if (ls[i] == ls[j] and j - i <ans):
            ans = j - i
print(ans)