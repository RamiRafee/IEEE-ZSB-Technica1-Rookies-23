import random as rd
correct=rd.randint(0, 999)
#correct=427
correct_string=str(correct)
x=int(input("Enter a 3-digit number:"))
hits=0
misses=0
attempts=1
if(x==correct):
    print("You Guessed From The First Attempt,HOORAY!")
while(x!=correct):
    hits=0
    misses=0
    x_string=str(x)
    for i in range(0,len(x_string)):
        if(x_string[i]==correct_string[i]):
            hits+=1
        elif(correct_string.find(x_string[i])!=-1):
            misses+=1
    print(hits,"hit",misses,"miss",sep=" ")
    x=int(input())
    attempts+=1
    if(x==correct):
        print("HOORAY!! You Won after",attempts,"attempts!!",sep=" ")
        

    