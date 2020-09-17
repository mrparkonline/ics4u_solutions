# 09.16.2020
# Collatz Conjecture Question

'''
Let N represent a positive integer from user input.
- If N is even, divide by 2: N/2
- If N is odd, multiply by 3 then add 1: 3N + 1

The collatz conjecture states that any N that is a positive integer will end up at 1.

13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
Create a list that will contain the collatz sequence starting from N.
'''

user_input = int(input('Enter a positive integer: '))

collatz_sequence = [] # empty list initialized so that we can add values

collatz_sequence.append(user_input)
print(collatz_sequence)

while collatz_sequence[-1] != 1:
    new_num = 0 # reset + initialization

    if collatz_sequence[-1] % 2 == 0:
        new_num = collatz_sequence[-1] // 2
    else:
        new_num = (collatz_sequence[-1] * 3) + 1

    collatz_sequence.append(new_num)
# end of while

print('The sequence starting at %s is %s.' % (user_input, collatz_sequence))
