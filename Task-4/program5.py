# -*- coding: utf-8 -*-
"""
Created on Fri Dec  2 21:49:53 2022

@author: Rami
"""
 ##input

print("input:")
n = int(input())
arr = [" "]*n
temp = [""]*n
for i in range(n):
    inpu = input().split()
    #had to cast it to change the reference 
    arr[i] = list(inpu)
    temp[i] = list(inpu)

for i in range(n):
    for j in range(n):
        num = int(arr[i][j])
        arr[i][j] = num
        temp[i][j] = num
        
 ##rotate 90 
for i in range(n):
    for j in range(n):
        arr[j][n - 1 -i] = temp [i][j]
 ##Output
print("OUTPUT:")
for i in range(n):
    for j in range(n):
        print(arr[i][j],end=" ")
    print()
