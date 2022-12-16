# -*- coding: utf-8 -*-
"""
Created on Fri Dec 16 09:44:25 2022

@author: Rami

"""
def toggle(arr,i,j):
    if arr[i][j] == "0":
         arr[i][j]="1"
    else:
         arr[i][j]="0"

init = [["1","1","1"],
        ["1","1","1"],
        ["1","1","1"]]

matrix = [[int(x) for x in input().split()]
          ,[int(x) for x in input().split()]
          ,[int(x) for x in input().split()]]

test = [0,1,2]

for i in range(3):
    for j in range(3):
        for k in range(matrix[i][j]):
            up = i - 1
            left = j - 1
            right = j+ 1
            down = i + 1
            toggle(init,i,j)
            if up in test:
               toggle(init,up,j)
            if(left in test):
                toggle(init,i,left)
            if(right in test):
                toggle(init,i,right)
            if(down in test):
                toggle(init,down,j)
for i in range(3):
    print("".join(init[i]))
        
