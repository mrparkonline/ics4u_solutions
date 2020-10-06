# Project Euler (Q14) - Longest Collatz sequence

# Example: 13 > 40 > 20 > 10 > 5 > 16 > 8 > 4 > 2 > 1

''' New programming technique: Memoization
Remember instances/solutions so that we dont repeat computation.

'''

collatz_table = {} # This will be a global dictionary, that we access in main.py

collatz_table[1] = [1]

def collatzSequence(num):
    if num in collatz_table: # num is a key; therefore, already has value in collatz_table ... we have already solved this number before
        return collatz_table[num]
    else:
        new_sequence = [num] # our new sequence starts at num

        next_num = 0
        if num % 2 == 0:
            next_num = num // 2
        else:
            next_num = num * 3 + 1

        while next_num not in collatz_table:
            # since next_num is not in the table,
            # we add it into our sequence and check the new next number
            new_sequence.append(next_num)

            if next_num % 2 == 0:
                next_num //= 2
            else:
                next_num *= 3
                next_num += 1
        else:
            new_sequence += collatz_table[next_num]
            collatz_table[num] = new_sequence
            # since next_num has already a sequence
            # i can extend my new_sequence with my next_num's sequence
        # end of while

        for i in range(1, len(new_sequence)):
            current_num = new_sequence[i]
            if current_num not in collatz_table and current_num < 1000000:
                collatz_table[current_num] = new_sequence[i:]
            else:
                break # end the loop here
        # end of for

        return collatz_table[num]
# end of collatzSequence

result = 0
max_len = 0

for num in range(1, 1000000):
    current_seq = collatzSequence(num)
    current_len = len(current_seq)

    if current_len > max_len:
        result = num
        max_len = current_len
# end of for

print(result, 'generated the longest length of:', max_len)
