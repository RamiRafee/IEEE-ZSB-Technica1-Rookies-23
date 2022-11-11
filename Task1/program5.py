print("INPUT :")
x=int(input(""))
sum=0
for i in range(x+1):
   if(i%3==0 or i%5==0):sum+=i
print("OUTPUT:",sum,sep="\n")