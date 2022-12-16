# -*- coding: utf-8 -*-
"""
Created on Thu Dec 15 22:50:23 2022

@author: Rami
"""

class Solution:
    def lastStoneWeight(self, stones: list[int]) -> int:
        stones.sort(reverse=True)
        
        while(len(stones)-1):
            if(stones[0]==stones[1]):
                stones.remove(stones[0])
                stones.remove(stones[0])
                if(len(stones)<=1):
                    break
                stones.sort(reverse=True)
            else:
                stones[1] = stones[0] - stones[1]
                stones.remove(stones[0])
                stones.sort(reverse=True)
            print(stones)
        if(len(stones)):
            return stones[0]
        else:
            return 0