# -*- coding: utf-8 -*-
"""
Created on Thu Dec 15 23:07:09 2022

@author: Rami
"""

class Solution:
    def kClosest(self, points: list[list[int]], k: int) -> list[list[int]]:
        points.sort(key = lambda row: row[0]**2+row[1]**2 )
        ans = list(list())
        for i in range(k):
            ans.append(points[i])
        return ans
    """ Another solution but will LTE
        # final = list(list())
        # if(k==len(points)):
        #         return points
        # for j in range(k):
        #     d = points[0][0] *points[0][0] + points[0][1] * points[0][1]
        #     ans = list(list())
        #     t = 0
        #     while(t<len(points)):
        #         temp = points[t][0] *points[t][0] + points[t][1] *points[t][1]
        #         # if(final.count(points[t])>0 ):
        #         #     if(t<len(points)-1):
        #         #         d = points[t+1][0] *points[t+1][0] + points[t+1][1] * points[t+1][1]
        #         #     t+=1
        #         #     continue
        #         if(temp == d):
        #             ans.append(points[t])
        #         elif(temp<d):
        #             d = temp
        #             ans = list(list())
        #             ans.append(points[t])
        #         t+=1
        #     for i in range(len(ans)):
        #         final.append(ans[i])
        #         points.remove(ans[i])
        #         print(points)
        # ans = list(list())
        # for i in range(k):
        #     ans.append(final[i])
        # return ans
        """
        