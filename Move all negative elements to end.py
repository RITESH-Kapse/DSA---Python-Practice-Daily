# Move all negative numbers to beginning and positive to end with constant extra space

#Solution : https://www.geeksforgeeks.org/move-negative-numbers-beginning-positive-end-constant-extra-space/

'''
Input: -12, 11, -13, -5, 6, -7, 5, -3, -6
Output: -12 -13 -5 -7 -3 -6 11 6 5

'''

def move(arr):
    arr.sort()

arr = [ -1, 2, -3, 4, 5, 6, -7, 8, 9 ]

move(arr)

for i in arr:
    print(i, end = ' ')