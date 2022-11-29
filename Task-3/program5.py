# -*- coding: utf-8 -*-
"""
Created on Tue Nov 29 23:56:42 2022

@author: Rami
"""
print("INPUT:")

temp = input().split()
city = [0] * int (temp[0])
n = int(temp[1])
station = input().split()
answer = [len(city)] * len(city)
for i in range(n):
    city[int(station[i])] = 1
for i in range(len(city)):
    if( city[i] == 1):
        for j in range(len(city)):
            if(city[j] != 1):
                if(abs(j-i)<answer[j]):
                    answer [j] = abs(j-i)
            else:
                answer[j]=0
print("OUTPUT:",max(answer),sep="\n")