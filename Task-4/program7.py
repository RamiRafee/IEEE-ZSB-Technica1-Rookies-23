# -*- coding: utf-8 -*-
"""
Created on Fri Dec  2 23:03:48 2022

@author: Rami
"""
#input
print("INPUT:")
n = int (input())
ls = list()

for i in range(n):
    ls.append(input())
#checking algorithm
#had to use while cuz range is fixed
i = 0   
while(i<len(ls)):
    s1 = set(ls[i])
    s1_len = len(ls[i])
    j = i + 1
    while(j<len(ls)):
        s2 = set(ls[j])
        s2_len = len(ls[j])
        if (s2.difference(s1) == set() and s2_len == s1_len):
            ls[i] = ls[i] + " " + ls[j]
            ls.remove(ls[j])
            j -= 1
        j += 1
    i += 1
#Output      
print("OUTPUT:")
for i in ls:
    print(i)
#had to comment the test case for me ;(
"""
6
eat
tea
tan
ate
nat
bat
"""