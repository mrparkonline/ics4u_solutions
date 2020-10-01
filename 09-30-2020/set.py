# Create a function that compares if two lists are unique, as in, both lists don’t have the same values

def isUnique(arr1, arr2):
    ''' isUnique returns True if items in arr1 and items in arr2 are unique from each other

    arguments
    -- arr1 : list
    -- arr2 : list

    return
    -- Boolean
    '''

    for item in arr1:
        if item in arr2:
            return False

    return True
# end of isUnique

def isUnique2(arr1, arr2):
    set_arr1 = set(arr1)
    set_arr2 = set(arr2)

    ''' Explanation
    1. If we intersect two sets together, we get a set of common values from the two sets
    2. If the intersection is empty, then there are no common values
    3. In python, emptiness is a Falsy value; therefore, not of False is True
    4. If the intersection is empty, we return True; otherwise, we return False
    5. & operator is the intersection operator for sets
    '''

    return not (set_arr1 & set_arr2)
# end of isUnique2

from random import randrange

arr1 = [randrange(1,20) for i in range(10)]
arr2 = [randrange(1,20) for j in range(10)]
arr3 = [randrange(20,30) for x in range(10)]
print(arr1)
print(arr2)
print(arr3)
print(isUnique(arr1, arr2))
print(isUnique2(arr1, arr2))
print(isUnique2(arr1, arr3))


def removeDuplicates(arr):
    ''' removeDuplicates preserves only single instances of each item

    argument
    -- arr : list

    return
    -- list
    '''

    result = []
    for item in arr:
        if item not in result:
            result.append(item)

    return result
# end of removeDuplicates

def removeDuplicates2(arr):
    return list(set(arr))

test = [randrange(1,20) for i in range(400)]

result1 = len(removeDuplicates(test))
print(result1)

result2 = len(removeDuplicates2(test))
print(result2)

# Implement the complement operation in Python 3

def complement(universe, a_set):
    ''' complement() is the function representation of the complement operator with sets

    argument
    -- universe : set
    -- a_set : set

    return
    -- set
    '''

    # checking to see if all the values in a_set exist in universe
    '''
    for item in a_set:
        if item not in universe:
            return set()
    # end of for
    if not a_set.issubset(universe):
        return set()

    if len(a_set) != len(a_set & universe):
        return set()
    '''

    return universe - a_set
# end of complement

uni = {'Mary', 'Mark', 'Fred', 'Angela', 'Frank', 'Laura', 'Jane'}
com = {'Mary', 'Mark', 'Angela', 'Frank', 'Laura'}

print('Complement of com:', complement(uni, com))

def setEven(low, upper):

    return {x for x in range(low, upper) if x % 2 == 0}

def setOdd(low, upper):

    return set(range(low,upper)) - setEven(low,upper)

print(setEven(1,30))
print(setOdd(1,30))
        
