# -*- coding: utf-8 -*-
"""
Created on Fri Dec  2 22:33:43 2022

@author: Rami
"""
print("INPUT:")


num = input()
def prob6(num:str):
    if(len(num)<4):
        for i in range(len(num),4):
            num = list(num)
            num.append("0")
            num = "".join(num)
    if(int(num) == 6174):
        return 0
    num = list(num)
    num.sort()
    n1 = int("".join(num))
    num.sort(reverse=True)
    n2 = int("".join(num))
    return (1 + prob6(str(abs(n1 - n2))))
print("Output:")
print(prob6(num))


