# https://practice.geeksforgeeks.org/problems/sort-an-array-of-0s-1s-and-2s4231/1

'''
Given an array which consists of only 0, 1 and 2. Sort the array without using any sorting algo

'''

# Solution :https://www.geeksforgeeks.org/sort-an-array-of-0s-1s-and-2s/

'''
Approach: Count the number of 0s, 1s and 2s in the given array. Then store all the 0s in the beginning followed by all the 1s then all the 2s.

Algorithm: 
Keep three counter c0 to count 0s, c1 to count 1s and c2 to count 2s
Traverse through the array and increase the count of c0 if the element is 0,increase the count of c1 if the element is 1 and increase the count of c2 if the element is 2
Now again traverse the array and replace first c0 elements with 0, next c1 elements with 1 and next c2 elements with 2.

'''

def printarr(arr,n):
    for i in range(n):
        print(arr[i], end=' ')

def sortarr(arr,n):
    c0 = 0
    c1 = 0
    c2 = 0

    for i in range(n):
        if arr[i] ==0:
            c0+=1
        elif arr[i]==1:
            c1+=1
        elif arr[i]==2:
            c2+=1

    i =0
    while c0>0:
        arr[i] = 0
        i+=1
        c0-=1

    while c1>0:
        arr[i]=1
        i+=1
        c1-=1

    while c2>0:
        arr[i]=2
        i+=1
        c2-=1

    printarr(arr,n)

arr = [0, 1, 1, 0, 1, 2, 1, 2, 0, 0, 0, 1]
n = len(arr)
  
sortarr(arr, n)