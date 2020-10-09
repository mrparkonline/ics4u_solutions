# Counting Sort
'''
Counting Sort Algorithm:

let A be a given list of integers (unsorted);
let D be a dictionary;
let R be a resulting list, set to []

1. Create keys for D from min(A) to max(A) inclusively
2. for each value in A:
    if D[value] is null:
        D[value] = 1
    else:
        D[value] += 1
3. for key, value pair in D:
    result += [key] * value
'''

from random import randrange

test = [randrange(-10, 10) for x in range(15)] # 15 integers unsorted ... A
print('Unsorted List:', test)
print('----')

# Step 1: Create keys for D from min(A) to max(A) inclusively
histogram = {key: 0 for key in range(min(test), max(test)+1)} # let histogram represent D

# Step 2: Populate our histogram
for value in test:
    histogram[value] += 1

# Step 3: Iterate through our histogram and build a sorted list

result = [] # let result be our sorted list
for key, occurence in histogram.items():
    result += [key] * occurence

    # print('our result currently:', result)
    # input()
print('Sorted List:', result)
# counting sort was an example of O(n+m)
# where m is the number of keys not in the unsorted list
