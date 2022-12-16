# -*- coding: utf-8 -*-
"""
Created on Fri Dec 16 00:51:06 2022

@author: Rami
"""
def  chocolateFeast(n, c, m):
    Sum =0
    Wrap=0
    
    if(n%c == 0):
        Sum = n/c
        Wrap = Sum
    else:
        n = n- n%c
        Sum = n/c
        Wrap = Sum
        
    while(Wrap != 0 and Wrap >= m):
        temp = 0
        if(Wrap%m == 0):temp = Wrap/m
        else: temp = (Wrap - Wrap%m)/m
        Sum += temp
        Wrap = Wrap%m
        Wrap += temp
    return int(Sum)