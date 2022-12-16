# -*- coding: utf-8 -*-
"""
Created on Fri Dec 16 09:36:49 2022

@author: Rami
"""

found = False
year = int(input())
while(not found):
    temp = []
    year+=1
    string = str(year)
    string = [x for x in string]
    for i in range(len(string)):
        if(temp.count(string[i])==0):
            temp.append(string[i])
    if(len(temp)==len(string)):
        found=True
print(year)
