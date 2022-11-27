test_string=input("enter the string:")
found=False
dup=False
string="hello"
index=0
i=0
while(index!=len(string)-1):
    if(string[index]==test_string[i] and not found):
        index+=1
        i+=1
        found=True
    elif(string[index]==test_string[i] and found):
        index+=1
        i+=1
    elif(string[index]!=test_string[i] and found and string[index-1]==test_string[i]):
        i+=1
    elif(string[index]!=test_string[i] and found and string[index-1]!=test_string[i]):
        i+=1
        index=0
        found=False
    else:
        i+=1
        
    if(i>=len(test_string)):
        break

if(index==len(string)-1):
    print("yes")
else:
    print("NO")
        