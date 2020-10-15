# Recursion Set 2

def gcd1(num1, num2):
    answer = 0

    for divisor in range(1, min(num1,num2)+1):
        if num1 % divisor == 0 and num2 % divisor == 0:
            answer = divisor

    return answer
# end of gcd1
print(gcd1(54,24))

# Recursive GCD
def r_gcd(num1, num2):
    # Euclidean Algorithm
    # https://en.wikipedia.org/wiki/Euclidean_algorithm

    if num2 == 0:
        return num1
    else:
        return r_gcd(num2, num1 % num2)

print(r_gcd(54,24))

# Linear Search
def r_search(arr, target, i=0):
    if not arr: # array is empty
        return -1
    else:
        if arr[0] == target:
            return i
        else:
            return r_search(arr[1:], target, i+1)

from random import randrange

test = [randrange(-20,20) for x in range(20)]
print('Random List:', test)

print(r_search(test,10))

# Linear Search without Tail Recursion
def linSearch(arr, target):
    if not arr:
        return -1
    elif arr[0] == target:
        return 0
    else:
        return 1 + linSearch(arr[1:], target)
'''
One Flaw w/ linSearch()

By design, it cannot return -1 when the target doesn't exist in arr
'''

print(linSearch(test ,10))

# Linear Search with different design :S
def linSearch2(arr, target):
    def inner(i=0):
        if i >= len(arr):
            return -1
        elif arr[i] == target:
            return i
        else:
            return inner(i+1)
    # end of inner

    if not arr:
        return -1
    else:
        return inner() # returns the result of the recursive function called "inner"
# end of linSearch2

print(linSearch2(test ,10))

# Twenty Questions
def twenty(start, end):
    ''' twenty() will try to guess your number between start to end inclusively.'''

    middle = (start + end) // 2

    print('Is', middle, 'your value?')
    user_input = input('Y/N: ')

    if user_input in 'Yy':
        return middle
    else:
        print('Is your number higher or lower?')
        user_input = input('H/L: ')

        if user_input in 'Hh':
            return twenty(middle, end)
        else:
            return twenty(start, middle)
# end of twenty

# We are thinking of 76
# print(twenty(1,100))

# Single Sequence of Collatz Recursive
def sequence(start, arr=[]):
    if start == 1:
        return arr + [1]
    else:
        if start % 2 == 0:
            return sequence(start // 2, arr + [start])
        else:
            return sequence((start*3)+1, arr + [start])

print(13, sequence(13))
print(29, sequence(29))
