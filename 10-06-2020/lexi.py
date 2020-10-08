# Wikipedia - Lexicographic Permutation Order Solution
# Q9) Project Euler (Q24) - Lexicographic permutations

''' Algorithm for generating permutation in lexicographic order

let a represent the smallest possible permutation lexicographic order
if our digits were 0,1,2 ... the smallest one is: 012

1. Find the largest index k such that a[k] < a[k + 1]. If no such index exists, the permutation is the last permutation.
2. Find the largest index l greater than k such that a[k] < a[l].
3. Swap the value of a[k] with that of a[l].
4. Reverse the sequence from a[k + 1] up to and including the final element a[n].

'''

permutations = [] # This is a list to contain all of our permutation
smallest_object = list('012') # we can change this to 0123456789 after
permutations.append(smallest_object)

def find_k(pattern):
    ''' returns the largest index k such that a[k] < a[k + 1]. If no index exist, we return -1'''

    k = -1

    for location in range(len(pattern)-1):
        if pattern[location] < pattern[location+1]:
            k = location

    return k
# end of find_k

def find_x(target, pattern):

    x = -1
    for location, value in enumerate(pattern):
        if value > target:
            x = location

    return x
# end of find_X

k = 0

while k != -1:
    # our latest permutation is found at permutations[-1] (aka, the last value in our list)
    current_permutation = permutations[-1].copy()
    print('My Current Object:', current_permutation)
    # 1. Find the largest index k such that a[k] < a[k + 1]. If no such index exists, the permutation is the last permutation.
    k = find_k(current_permutation)

    if k != -1:
        # 2. Find the largest index l greater than k such that a[k] < a[l].
        # note we've changed l to x for better readability
        x = find_x(current_permutation[k], current_permutation)

        # 3. Swap the value of a[k] with that of a[l]/a[x].
        current_permutation[k], current_permutation[x] = current_permutation[x], current_permutation[k]

        # 4. Reverse the sequence from a[k + 1] up to and including the final element a[n].
        current_permutation = current_permutation[:k+1] + current_permutation[k+1:][::-1]

        print('My Current Object became:', current_permutation)
        permutations.append(current_permutation)
    else:
        # end the loop
        break
# end of while loop

print('Our Permutations:', permutations)
