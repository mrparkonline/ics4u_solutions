# Project Euler (Q14) - Longest Collatz sequence

# Example: 13 > 40 > 20 > 10 > 5 > 16 > 8 > 4 > 2 > 1

''' Brute Force Solution Idea
Brute Force: The simplest way to solve a problem
1. do a for loop: look at all numbers from 1 to 1000000
2. for each number, generate the collatz sequence
    2a. if the current number's sequence is longer than the current maximum
    2b. update the longest length and the value that created the longest length
3. repeat all this until the end
'''

def collatzSequence(num):

    sequence = [num]

    while num != 1:
        if num % 2 == 0:
            num //= 2
        else:
            num *= 3
            num += 1

        sequence.append(num)

    return sequence
# end of collatzSequence

resulting_num = 0
max_length = 0

for num in range(1, 1000000):
    current_sequence = collatzSequence(num)
    current_length = len(current_sequence)

    if current_length > max_length:
        resulting_num = num
        max_length = current_length

print(resulting_num, 'generated the longest length of:', max_length)
# Answer: 837799 generated the longest length of: 525
