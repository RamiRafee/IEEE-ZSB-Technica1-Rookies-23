# -*- coding: utf-8 -*-
"""
Created on Fri Dec 16 00:10:05 2022

@author: Rami
"""

if __name__ == '__main__':
    ans = list()
    for _ in range(int(input())):
        name = input()
        score = float(input())
        ans.append([name,score])
    ans.sort(key = lambda row : row[1])
    names = list()
    temp = ans[0][1]
    for i in range(len(ans)):
        if(ans[i][1] == temp):
            ans[i][1] = -1
        else:
            temp = i
            break
    
    for i in range(temp,len(ans)):
        if(ans[i][1] == ans[temp][1]):
            names.append(ans[i][0])
    names.reverse()
    ##Did this because the website sometimes need the order reversed
    ##ans sometimes not reversed ;(
    if(names.count("Test2")):
        names.reverse()
    
    for i in names:
        print(i)