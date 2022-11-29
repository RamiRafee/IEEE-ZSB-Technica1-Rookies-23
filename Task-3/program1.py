# -*- coding: utf-8 -*-
"""
Created on Tue Nov 29 22:07:14 2022

@author: Rami
"""
print("input:")
n = int(input())
matrix = []
main_diagonal = 0
second_diagonal = 0
for i in range(0,n):
    matrix.append([])
    temp = input().split()
    for j in range(0,n):
        element = int(temp[j])
        matrix [i].append(element)
        if(i == j):
            main_diagonal += element
        if(i + j == n - 1):
            second_diagonal += element
print(abs(main_diagonal - second_diagonal))
