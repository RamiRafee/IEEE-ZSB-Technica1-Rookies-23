# -*- coding: utf-8 -*-
"""
Created on Mon Dec  5 23:03:02 2022

@author: Rami
"""

#ls = [81,13,77,24,35,61,48,3,23,87,92,95,74,57,99,86,28,15,55,7,51]
print("INPUT:")
string = input().split()
ls = list()
for i in range(len(string)):
   ls.append(int(string[i])) 
def max_heapify(ls:list , i:int):
    left = ((i+1)*2)-1
    right = ((i+1)*2)
    if right >=len(ls):
        right = i
    if left >=len(ls):
        left = i
    maximum = i
    if ls[left] > ls [i]:
        maximum = left
    #every parent must have a left node so
    #we compare the right with maximum not the parent node
    if ls [right] > ls[maximum]:
        maximum = right
    if maximum != i:
        ls[maximum],ls[i] = ls[i],ls[maximum]
        max_heapify(ls, maximum)
def build_max_heap(ls:list):
    l = len(ls)
    for i in range((l//2),-1,-1):
        max_heapify(ls, i)
build_max_heap(ls)
print("OUTPUT:")
for i in ls:
    print(i,end=" ")