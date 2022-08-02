# Problem: https://practice.geeksforgeeks.org/problems/kth-smallest-element/0
# https://www.geeksforgeeks.org/kth-smallestlargest-element-unsorted-array/

'''

Input: arr[] = {7, 10, 4, 3, 20, 15}, k = 3 
Output: 7

Input: arr[] = {7, 10, 4, 3, 20, 15}, k = 4 
Output: 10 

'''

def kth_smallest_ele(arr, n, k):

    arr.sort()
    return arr[k-1]

if __name__== '__main__':
    arr = [12, 3, 5, 7, 19]
    n = len(arr)
    k = 3

    print(str(k) +"rd/th smallest ele in list is :", kth_smallest_ele(arr,n,k))



