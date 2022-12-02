# -*- coding: utf-8 -*-
"""
Created on Fri Dec  2 21:40:42 2022

@author: Rami
"""
print("INPUT:")
n = int(input())
num = input().split()
arr = [0]*(n+1)
for i in range(1,n+1):
    arr[i] = int(num[i-1])
def add(arr:list,n:int):
    if(arr[n-1]!=9):
        arr[n-1] += 1
        return
    else:
        arr[n-1] = 0
        add(arr,n-1)
        return
add(arr,len(arr))
for i in range(1,len(arr)):
    print(arr[i],end=" ")
    