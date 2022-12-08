# -*- coding: utf-8 -*-
"""
Created on Thu Dec  8 16:16:49 2022

@author: Rami
"""
SECONDS = 86400
days=0
n,t = input().split()
n = int(n)
t = int(t)
temp=0
arr = input().split()
for i in range(n):
    arr[i] = int(arr[i])
    temp += SECONDS - arr[i]
    days += 1
    
    if(temp>=t ):
        print(days)
        break;
        
