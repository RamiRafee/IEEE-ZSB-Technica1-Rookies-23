# -*- coding: utf-8 -*-
"""
Created on Thu Dec  8 10:28:21 2022

@author: Rami
"""

def acmTeam(topic):
    Max = 0
    count = 0
    for i in range(len(topic)):
        Sum = 0
        for j in range(i+1,len(topic)):
            Sum = 0
            for k in range(len(topic[i])):
                if((topic[i][k] == "1") or (topic[j][k] == "1")):
                    Sum += 1
            if(Sum > Max):
                Max = Sum
                count = 1
            elif(Sum ==Max):
                count += 1
    return[Max,count]