# -*- coding: utf-8 -*-
"""
Created on Fri Dec 16 09:16:31 2022

@author: Rami
"""

string = input()
string = [x for x in string]
ans= ""
for i in range(len(string)-1):
    if(string [i] == "."):
        ans += "0"
        string[i] = "D"
    elif(string[i] + string[i+1]== "-."):
        ans+= "1"
        string[i],string[i+1] = "D","D"
    elif(string[i] + string[i+1]=="--"):
        ans+="2"
        string[i],string[i+1] = "D","D"
    
if(len(ans)==0 or string[len(string)-1]=="."):
    ans+="0"
print(ans)