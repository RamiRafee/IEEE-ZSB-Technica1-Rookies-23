# -*- coding: utf-8 -*-
"""
Created on Thu Dec 15 22:28:26 2022

@author: Rami
"""

# Definition for singly-linked list.
class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next
class Solution:
    def mergeTwoLists(self, list1: ListNode, list2: ListNode) -> ListNode:
        
        ans =list()
       
        while(list1 and list2):
            if(list1.val < list2.val):
                ans.append(list1.val)
                list1=list1.next
            else:
                ans.append(list2.val)
                list2=list2.next
        while(list1):
            ans.append(list1.val)
            list1=list1.next
        while(list2):
            ans.append(list2.val)
            list2=list2.next

        print(ans)
        if(not ans):
            return 
        answer = ListNode(ans[0])
        node = answer.next
        for i in range(1,len(ans)):
            if(not node):
                answer.next = ListNode(ans[i])
                node = answer.next
            else:
                node.next=ListNode(ans[i])
                node = node.next
        return answer