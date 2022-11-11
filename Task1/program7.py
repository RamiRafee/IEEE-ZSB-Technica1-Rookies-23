x=int(input("INPUT:\n"))
string=str(x)
rev=string [::-1]
letter=[x for x in rev]
for i in range(len(letter)-1):
    if (letter[i]=="0"):
        del letter[i]
rev="".join(letter)
print("OUTPUT:")
print(rev)
if(string==string[::-1]):
    print("YES")
else :
    print ("NO")