from random import randrange

# Bubble Sort

def b_sort(arr):
    ''' python bubble sort implementation

    argument
    -- arr : list

    return
    -- list
    '''
    swapped = True

    while swapped:
        swapped = False

        for i in range(1,len(arr)):
            if arr[i-1] > arr[i]:
                # swap! a[i-1] and a[i]
                arr[i-1], arr[i] = arr[i], arr[i-1]
                swapped = True
        # end of for
    # end of while
# end of b_sort

def i_sort(arr):
    ''' Insertion Sort
    # Let A be a List, i and j both be indexes
    i = 1
    while i < length(A)
        j = i
        while j > 0 and A[j-1] > A[j]
            swap A[j] and A[j-1]
            j = j - 1
        i = i + 1

    '''

    i = 1
    while i < len(arr):
        j = i
        while j > 0 and arr[j-1] > arr[j]:
            arr[j], arr[j-1] = arr[j-1], arr[j]
            j -= 1
        # end inner while

        i += 1
    # end of while
# end of i_sort

def s_sort(arr, sorted_arr=[]):
    '''
    # Let A be the unsorted list, and let B be the sorted list
        repeat until A is empty
        Target = the smallest value from A
        Append Target to B
        Remove target from A
    '''
    if not arr:
        return sorted_arr
    else:
        target = min(arr)
        '''
        for i in range(1,len(arr)):
            if arr[i] < target:
                target = arr[i]
        '''

        arr.remove(target)

        return s_sort(arr, sorted_arr + [target])
# end of s_sort

test = [randrange(-10,10) for x in range(8)]
print('Unsorted List:', test)
test = s_sort(test)
print(test)

#test.sort()
#v = sorted(test)
