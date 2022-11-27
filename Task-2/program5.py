arr=[1,2,50,9,8,10,2,4]
for i in range(1,len(arr)):
    val=arr[i]
    j=i-1
    while(j>-1 and arr[j]>val):
        arr[j+1]=arr[j]
        j-=1
    arr[j+1]=val
for i in arr:
    print(i,end=" ")
"""
it's like a deck of cards when you sort them in front of you 
you take the smaller value in a hand and keep moving the bigger cards with your other hand
until you find the right place for the card in your hand and (insert) it in the right spot
"""
"""
sorting 9 in detail:-->
1,2,50,9,8,10,2,4
1,2,50,50,8,10,2,4
1,2,9,50,8,10,2,4
"""
"""
sorting the second 2 in detail:-->
1,2,8,9,10,50,2,4
1,2,8,9,10,50,50,4
1,2,8,9,10,10,50,4
1,2,8,9,9,10,50,4
1,2,8,8,9,10,50,4
1,2,2,8,9,10,50,4
"""
"""
A stable algorithm is an algorithm that sorts the numbers in the same order that they appeared in
eg:
    (1),5,3,0,((1)) ------>> after sorting ------->> 0,(1),((1)),3,5
Insertion sort is a stable algorithm as we clearly see from the example written in the code the second 2
came after the first 2
"""