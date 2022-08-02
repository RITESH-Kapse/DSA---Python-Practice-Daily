#Problem: https://www.geeksforgeeks.org/maximum-and-minimum-in-an-array/

'''
return minimum and maximum in an array. Your program should make the minimum number of comparisons. 

'''


# Approach 1 : Simple Linear Search

"""Initialize values of min and max as minimum and maximum of the first two elements respectively. 
Starting from 3rd, compare each element with max and min, and change max and min accordingly
(i.e., if the element is smaller than min then change min, else if the element is greater than max then change max, else ignore the element) 
"""

class Min_Max:

    def __init__(self):
        self.min = 0
        self.max = 0

#Using Function Annotation
# Refer :https://peps.python.org/pep-3107/
def getMinMax(arr : list, n : int) -> Min_Max:
    minmax = Min_Max()

    if n == 1:
        minmax.max = arr[0]
        minmax.min = arr[0]
        return minmax

    if arr[0] > arr[1]:
        minmax.max = arr[0]
        minmax.min = arr[1]
    else:
        minmax.max = arr[1]
        minmax.min = arr[0]

    for i in range(2, n):
        if arr[i] > minmax.max:
            minmax.max = arr[i]
        elif arr[i] < minmax.min:
            minmax.min = arr[i]

    return minmax

#Main function

if __name__ == "__main__":
    arr = [1000, 11, 445, 1, 330, 3000]
    arr_size = 6
    minmax = getMinMax(arr, arr_size)
    print("Minimum element is", minmax.min)
    print("Maximum element is", minmax.max)

'''

Approach 2 : Copied from GreekForGeeks

def getMinMax(arr):
     
    n = len(arr)
     
    # If array has even number of elements then
    # initialize the first two elements as minimum
    # and maximum
    if(n % 2 == 0):
        mx = max(arr[0], arr[1])
        mn = min(arr[0], arr[1])
         
        # set the starting index for loop
        i = 2
         
    # If array has odd number of elements then
    # initialize the first element as minimum
    # and maximum
    else:
        mx = mn = arr[0]
         
        # set the starting index for loop
        i = 1
         
    # In the while loop, pick elements in pair and
    # compare the pair with max and min so far
    while(i < n - 1):
        if arr[i] < arr[i + 1]:
            mx = max(mx, arr[i + 1])
            mn = min(mn, arr[i])
        else:
            mx = max(mx, arr[i])
            mn = min(mn, arr[i + 1])
             
        # Increment the index by 2 as two
        # elements are processed in loop
        i += 2
     
    return (mx, mn)
     
# Driver Code
if __name__ =='__main__':
     
    arr = [1000, 11, 445, 1, 330, 3000]
    mx, mn = getMinMax(arr)
    print("Minimum element is", mn)
    print("Maximum element is", mx)
     


'''