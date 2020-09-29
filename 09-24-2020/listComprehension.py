# Question 1
arr_a = [1,2,3]
arr_b = [3,1,4]

# Create the following from arr_a and arr_b
# [[1, 3], [1, 4], [2, 3], [2, 1], [2, 4], [3, 1], [3, 4]]

# Non Comprehensive Method:
result = []
for value_a in arr_a:
    for value_b in arr_b:
        if value_a != value_b:
           result.append([value_a, value_b])

print(result)

# List Comprehension Method:
result2 = [ [value_a, value_b] for value_a in arr_a for value_b in arr_b if value_a != value_b ]

print(result2)
# End of Q1

# Question 2
vec = [[1,2,3], [4,5,6], [7,8,9]]

# Flatten list vec to:
# [1,2,3,4,5,6,7,8,9]

# Non-comprehensive method:
result = []

for row in vec:
    for value in row:
        result.append(value)

print('Flattened vec:', result)

# List Comprehension
result2 = [value for row in vec for value in row]
print(result2)
# end of question 2

# List Comprehension with custom functions:
def isPrime(num):
    ''' isPrime determines if num is prime

    argument
    -- num : int

    return
    -- boolean
    '''
    if num < 2:
        return False
    elif num in [2,3]:
        return True
    elif num % 2 == 0:
        return False
    else:
        upper_limit = int(num ** 0.5) + 1
        for divisor in range(3, upper_limit, 2):
            if num % divisor == 0:
                return False

        return True
# end of isPrime

def factors(num):
    ''' factors() returns a list of factors of num

    argument
    -- num : integer

    return
    -- list
    '''

    # Initialize an upper limit
    upper_limit = int(num ** 0.5) + 1

    incremental_var = 0
    # Even vs Odd Check
    if num % 2 == 0:
        # we have an even number
        incremental_var = 1
    else:
        # we have an odd number
        incremental_var = 2

    result = [] # factor list container
    for divisor in range(1, upper_limit, incremental_var):
        if num % divisor == 0:
            # divisor is a factor
            the_other_factor = num // divisor
            if the_other_factor != divisor:
                # two distinct factor situation
                result += [divisor, the_other_factor]
            else:
                # perfect square situation
                result.append(divisor)
    # end of for

    return result
# end of factors

# Start Tutorial

primeList = [value for value in range(1,121) if isPrime(value)]
print(primeList)

factorsList = [[0]] + [factors(num) for num in range(1,20)]

print(factorsList)

from random import randrange

randomNumbers = [randrange(1,100) for i in range(20)]
print(randomNumbers)
