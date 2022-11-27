x=input("input:")
x=x.split()
x=set(x)
x=list(x)
x.sort()
print("Output:")
for i in x:
    print(i,end=" ")