# -*- coding: utf-8 -*-
"""
Created on Fri Dec  2 20:59:09 2022

@author: Rami
"""
print( "INPUT:" )
l = input().split()
n = int(l[0])
k = int(l[1])
arr = input().split()
for i in range(n):
    arr[i] = int(arr[i])
f_arr = [0]*(max(arr) + 1)
for i in arr:
    f_arr[i]+=1
index = 0
for i in range(k):
    print(f_arr.index(max(f_arr)),end=" ")
    f_arr[f_arr.index(max(f_arr))] = 0
