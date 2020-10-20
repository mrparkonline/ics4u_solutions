# Binary Search Non recursive
def binSearch(data, target):

    left = 0
    right = len(data) - 1

    while left <= right:
        middle = (left + right) // 2

        if data[middle] == target:
            return middle
        elif data[middle] < target:
            left = middle + 1
        else:
            # data[middle] > target:
            right = middle - 1
    # end of while
    return -1
# end of binSearch

# Recursive Binary Search
def r_binSearch(data, target, i=0):

    if not data:
        return -1
    elif len(data) == 1 and data[0] != target:
            return -1
    else:
        middle = (len(data)-1) // 2

        if data[middle] == target:
            return middle+i
        elif data[middle] < target:
            return r_binSearch(data[middle+1:], target, middle+i+1)
        else:
            return r_binSearch(data[:middle], target, i)
# end of r_binSearch

from random import randrange
test = [randrange(-100,100) for i in range(20)]
test.sort()
print('Testing List:', test)

print(binSearch(test, 42))
print(r_binSearch(test, 42))
