# -*- coding: utf-8 -*-
"""
Created on Mon Dec  5 23:28:49 2022

@author: Rami
"""
open_ref = ['(', '{',  '[']
close_ref = [')','}',']']
valid = True
print("INPUT:")
string = input()
ls = list()
for i in string:
    ls.append(i)
stack = list()
stack.append(ls[0])
if close_ref.count(stack[0])>0:
    valid = False
for i in range(1,len(ls)):
    if len(stack)<= 0:
        stack.append(ls[i])
        continue
    temp = stack.pop()
    #3,4 trivial value
    close_index = 3
    open_index = 4
    if open_ref.count(temp)>0:
        open_index = open_ref.index(temp)
    if close_ref.count(ls[i])>0:
        close_index = close_ref.index(ls[i])
    if close_index != open_index and open_ref.count(ls[i])>0:
        stack.append(temp)
        stack.append(ls[i])
    elif close_index != open_index and open_ref.count(ls[i])==0:
        valid = False
        break

if (len (stack)>0):
    valid = False
print("OUTPUT",valid,sep="\n")
        