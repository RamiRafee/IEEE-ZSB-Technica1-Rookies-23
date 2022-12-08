# -*- coding: utf-8 -*-
"""
Created on Thu Dec  8 14:30:09 2022

@author: Rami
"""
from sys import stdin, stdout
class Node:
 
    
    def __init__(self, data):
        self.data = data  # Assign data
        self.next = None  # Initialize next as null
 
 

class LinkedList:
 
    
    def __init__(self):
        self.head = None
 
 
    
    def push(self, new_data):
 
        
        new_node = Node(new_data)
 
        
        new_node.next = self.head
 
        
        self.head = new_node
 
 
    
    def insertAfter(self, prev_node, new_data):
 
        
        if prev_node is None:
            return
 
        
        new_node = Node(new_data)
 
        
        new_node.next = prev_node.next
 
        prev_node.next = new_node
 
 
    
    def append(self, new_data):
 
        
        new_node = Node(new_data)
 
        
        if self.head is None:
            self.head = new_node
            return
 
        
        last = self.head
        while (last.next):
            last = last.next
 
        
        last.next =  new_node
 

    def deleteNode(self, key):
         
       
        temp = self.head
 
        
        if (temp is not None):
            if (temp.data == key):
                self.head = temp.next
                temp = None
                return
 
        
        while(temp is not None):
            if temp.data == key:
                break
            prev = temp
            temp = temp.next
 
        
        if(temp == None):
            return
 
        
        prev.next = temp.next
 
        temp = None
    def printList(self):
        temp = self.head
        while (temp):
            print(temp.data,end=" ")
            temp = temp.next
 

t = int(stdin.readline())
i=0
while(i<t):
    
    l = stdin.readline().split()
    n=int(l[0])
    k=int(l[1])
    pop = stdin.readline().split()
    #pop.reverse()
    llist = LinkedList()
    
    for i in range(n-1,-1,-1) :
        llist.push(int(pop[i]))
    
    for j in range(k):
        dele = False
        temp1 = llist.head
        
        while(temp1.next):
            if(temp1.data<temp1.next.data):
                llist.deleteNode(temp1.data)
                dele = True
                break
            elif(temp1.next == None and not dele):
                llist.deleteNode(temp1.data)
                
            temp1=temp1.next
            
    llist.printList()
    stdout.write("\n")
    i+=1
        
