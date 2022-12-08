# -*- coding: utf-8 -*-
"""
Created on Thu Dec  8 10:51:43 2022

@author: Rami
"""

def hackerrankInString(s):
    # Write your code here
    string = "hackerrank"
    num = 0
    for i in range(len(s)):
        if(s[i] == string[num]):
            num += 1
        if(num == len(string)):
            break
    if(num == len(string)):
        return "YES"
    else:
        return "NO"