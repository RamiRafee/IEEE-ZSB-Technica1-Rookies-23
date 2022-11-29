# -*- coding: utf-8 -*-
"""
Created on Tue Nov 29 22:35:26 2022

@author: Rami
"""
print("input:")
n = int( input() )
ls = []
for i in range(0,n):
    name = input()
    grade = float(input())
    ls.append([name,grade])
##we can use sort() to sort the second column only   
##using insertion

for i in range(1,n):
    j = i-1
    name=ls[i][0]
    grade = ls[i][1]
    while ( j >= 0 and ls[j][1]>grade):
        ls[j+1]=ls[j]
        j -= 1
    ls[j+1]=[name,grade]
    
temp_ls=list()
for a,b in ls:
    temp_ls.append(b)
s=set(temp_ls)
temp=list(s)
temp=min(temp)
for i in temp_ls:
    if(i != temp):
        temp = i
        break
for i in range(1,n):
    if(ls[i][1] == temp):
        print (ls[i][0])
