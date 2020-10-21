# Merge Sort
# Top Down Approach

'''
function: divider(A)
    Create two empty lists called Left and Right

    Get Midpoint at n/2 - 1,
        - all values before and include the midpoint is Left list
        - all values after midpoint is Right list

    Update Left to divider(Left) ... recursive call
    Update Right to divider(Right) ... recursive call

    return merge(Left, Right)
'''

# Let Divider Represent merge sort.
def divider(arr):
    # Base case
    if len(arr) <= 1:
        return arr

    left = []
    right = []

    midpoint = len(arr)//2 - 1

    left = arr[:midpoint+1] # We appended all the values to left of the midpoint
    right = arr[midpoint+1:] # We appended all the values to the right of the midpoint

    left = divider(left)
    right = divider(right)

    return merge(left, right)
# end of divider

'''
function: merge(X, Y)
    Create empty list called Sorted

    While both x and y are not empty
        if X and Y are both non empty
            compare X[0] and Y[0]
                add the smaller value to Sorted
                removed the respective

    if X is empty and Y is not empty
        add all Y values to Sorted

    if Y is empty and X is not empty
        add all X values to Sorted

    return Sorted

'''

def merge(arr1, arr2):
    sorted_arr = []

    while arr1 and arr2:
        if arr1[0] <= arr2[0]:
            ''' pop() takes a value from the given index and removes
            and it also returns the removed value
            '''
            sorted_arr.append(arr1.pop(0))
        else:
            sorted_arr.append(arr2.pop(0))
    # end of while

    if arr1:
        sorted_arr += arr1

    if arr2:
        sorted_arr += arr2

    return sorted_arr
# end of merge()

from random import randrange

test = [randrange(-15,15) for x in range(15)]
print('Unsorted List:', test)

print(divider(test))
