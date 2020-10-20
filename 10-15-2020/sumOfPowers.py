''' Sum of Powers

Target = 100
Exponent = 3

If I had collection of powers with exponent of 3 ...
- What number do I need to stop at?
- Our upper limit is the nth root of our target ... where n is the exponent

We stop at: 100 ^ (1/3)

'''
target = 100
exponent = 2

upper_limit = int(target ** (1/exponent)) + 1
powers = [i**exponent for i in range(1, upper_limit)]

print('our powers:', powers)

# Generate all subsets from our list of powers
def subset(arr):
    ''' subset() returns all the possible subsets of given arr

    argument:
    -- arr : list

    return
    -- 2D list ... lists within a list
    '''

    # Base Case 1: arr is empty
    if not arr:
        # we return a list of an empty list
        return [arr] # basically [[]]

    #Base Case 2: arr has length of one ... only a single item in the list
    elif len(arr) == 1:
        return [[]] + [arr]

    # Recursive calls:
    else:
        ''' finding the subset of arr[1:]

        if arr was: [1,2,3,4], we must find all the subsets of [2,3,4] then add [1] to all such subsets.
        '''
        next_subset = subset(arr[1:]) # this is our recursive call

        current_subset = [] # Have not created current arr's subset

        for sub in next_subset:
            temp = [arr[0]]
            temp += sub
            current_subset.append(temp)

        return next_subset + current_subset
# end of subset

#print(subset([1,2,3,4]))
power_subsets = subset(powers)

counter = 0

for sub in power_subsets:
    if sum(sub) == target:
        counter += 1

print('There are', counter, 'ways to add up to', target)
