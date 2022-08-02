#Problem : https://www.geeksforgeeks.org/write-a-program-to-reverse-an-array-or-string/

"""
    
    Write a program to reverse an array or string
    Given an array (or string), the task is to reverse the array/string.
    Examples : 
    

    Input  : arr[] = {1, 2, 3}
    Output : arr[] = {3, 2, 1}

    Input :  arr[] = {4, 5, 1, 2}
    Output : arr[] = {2, 1, 5, 4}

"""
# array = input("Enter the array or string")
# array_list = array.split()


#Approach 1 : List slicing

'''
def reverseList(X):
    print(X[::-1])

X = [1, 2, 3]
print("Reverse Output List is below :")
reverseList(X)

'''

#Approach 2 : Iteration

def reverse(input_array, start, end):
    while start < end:
        input_array[start],input_array[end] = input_array[end],input_array[start]
        start = start + 1
        end = end - 1


input_array = [1,2,3,4,5]

reverse(input_array, 0, 4)

print(input_array)