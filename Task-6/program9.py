# -*- coding: utf-8 -*-
"""
Created on Thu Dec  8 14:07:00 2022

@author: Rami
"""

from collections import defaultdict
class DetectSquares:
    def __init__(self):
        self.coor = dict()
    
    def add(self, point):
        x, y = point
        if x in self.coor.keys():
            self.coor[x][y] += 1
        else:
            self.coor[x] = defaultdict(int) ##used defaultdict cuz it will always have a key (default Value: 0)
            self.coor[x][y] += 1
            
    
    
    def count(self, point):
        x, y = point
        if x not in self.coor.keys(): 
            return 0
        
        ans = 0
        for y0 in self.coor[x].keys():
            if y0 == y:
                continue
            side_len = abs(y - y0)
            #count left squares
            if (x - side_len) in self.coor.keys():
                u1 = self.coor[x][y0] ##number of points above or under
                u2 = self.coor[x - side_len][y] ##number of points left above or under
                u3 = self.coor[x - side_len][y0] ##number of points left under of above
                ans += u1 * u2 * u3
            #count right squares
            if (x + side_len) in self.coor.keys():
                u1 = self.coor[x][y0] ##number of points above or under
                u2 = self.coor[x + side_len][y] ##number of points right above or under
                u3 = self.coor[x + side_len][y0] ##number of points right under of above
                ans += u1 * u2 * u3
        return ans


        


# Your DetectSquares object will be instantiated and called as such:
# obj = DetectSquares()
# obj.add(point)
# param_2 = obj.count(point)