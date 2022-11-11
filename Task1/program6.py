print("INPUT:")
x=int(input())
y=int(input())
gcd=0
if(x>y):
    temp=x
    x=y
    y=temp
if(y%x==0):gcd=x
lis=list()
for i in range(1,x):
    if(x%i==0):
        lis.append(i)
res=list()
for i in lis:
    if(y%i==0):
        res.append(i)
print("OUTPUT:")
print(max(res))