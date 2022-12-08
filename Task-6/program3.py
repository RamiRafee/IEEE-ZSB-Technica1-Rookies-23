# -*- coding: utf-8 -*-
"""
Created on Thu Dec  8 08:58:20 2022

@author: Rami
"""

def climbingLeaderboard(ranked, player):
    rank = []
    [rank.append(i) for i in ranked if i not in rank]
    ans = [0]*len(player)
    minimum = min (rank)
    maximum = max(rank)
    index = len(rank)-1
    for i in range(len(player)):
        temp = player[i]
        
        if(temp < minimum):
            ans[i] = len(rank) + 1
            continue
        
        elif(temp > maximum):
            ans[i] = 1
            continue
        
        for j in range(index,-1,-1):
            if (temp>=rank[j]):
                ans[i] = j + 1 
                index = j          
    return ans