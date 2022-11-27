class node:
   def __init__(self,data=None):
        self.data=data
        self.next=None
class linkedList:
   def __init__(self):
        ##type of head will be node
        self.head=None
linked=linkedList()
x=node(1)
y=node(2)
z=node(3)
y.next=z
x.next=y
linked.head=x
print(linked.head.data)
print(linked.head.next.data)
print(linked.head.next.next.data)
