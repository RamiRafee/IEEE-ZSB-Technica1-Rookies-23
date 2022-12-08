# -*- coding: utf-8 -*-
"""
Created on Thu Dec  8 11:44:35 2022

@author: Rami
"""

def insert(self, val):
        #Enter you code here.
        if(self.root == None):
            self.root = Node(val)
            self.root.level = 0
            return self.root
        
        else:
            node = Node(val)
            parent = None
            current = self.root
             
            while (current != None):
                if(node.info <current.info):
                    if(current.left == None):
                        current.left  = node
                        return 
                    else:
                      current = current.left  
                else:
                    if(current.right == None):
                        current.right = node
                        return
                    else:
                        current=current.right