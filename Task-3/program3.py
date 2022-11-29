# -*- coding: utf-8 -*-
"""
Created on Tue Nov 29 23:24:21 2022

@author: Rami
"""
print("input:")
n = int(input())
re_volume = 0
bottles = list()
for i in range(0,n):
    temp = input().split()
    re_volume += int(temp[0])
    bottles.append(int(temp[1]))
print("OUTPUT:")
bottles.sort(reverse=True)
if(re_volume > bottles[0] + bottles[1]):
    print("NO")
else:
    print("YES")