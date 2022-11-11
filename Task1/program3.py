
def for_func(l:list)->int:
    sum=0
    for i in range(len(l)):
        sum+=l[i]
    return sum
def while_func(l:list)->int:
    sum=0
    i=len(l)
    while(i>0):
        sum+=l[i-1]
        i-=1
    return sum
def rec_func(l:list,x:int)->int:
    
    if(x<0):
        return 0
    else:
        sum=l[x]+ rec_func(l,x-1)
        return sum
    
l=int (input("input the length of the list:"))
list1=list()
for i in range(l):
    list1.append(int(input()))
print("WITH FOR",for_func(list1),sep="=")
print("WITH WHILE",while_func(list1),sep="=")
print("WITH RECURSION",rec_func(list1,l-1),sep="=")