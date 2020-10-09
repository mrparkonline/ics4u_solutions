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

def primesUnderN(num):
    ''' primesUnderN1() returns a list of all prime numbers under num
    argument
    -- num : integer
    return
    -- list
    '''

    result = [2]
    for i in range(3,num,2):
        if isPrime(i): # if isPrime(i) == True:
            result.append(i)

    return result
# end of primesUnderN

def sieve(num):
    '''
    algorithm Sieve of Eratosthenes is
    input: an integer n > 1.
    output: all prime numbers from 2 through n.
    let A be an array of Boolean values, indexed by integers 2 to n,
    initially all set to true.
    for i = 2, 3, 4, ..., not exceeding √n do
        if A[i] is true
            for j = i^2, i^2+i, i^2+2i, i^2+3i, ..., not exceeding n do
                A[j] := false
    return all i such that A[i] is true.
    '''

    # Array of Boolean Values of num length
    result = [False, False] # Index of 0 and 1 is going to be False
    result += [True] * (num - 1)

    upper_limit = int(num ** 0.5) + 1

    for i in range(2, upper_limit):
        if result[i]: # if result[i] == True:
            for j in range(i*i, num+1, i):
                result[j] = False
    # end of double for loops

    prime_locations = []

    # return all i such that A[i] is true.
    for i in range(len(result)):
        if result[i]:
            prime_locations.append(i)

    return prime_locations
# end of sieve

# We have functions:
# - primesUnderN()
# - sieve()

from timeit import default_timer as timer

num = int(input('Set the input size of num: '))
print('----')

# Testing primesUnderN()
runtimes = []

for x in range(5):
    start = timer()
    result = primesUnderN(num)
    end = timer()
    current_runtime = end - start
    runtimes.append(current_runtime)

print('Testing primesUnderN()')
print('Our run time results:', runtimes)
average_runtime = sum(runtimes) / len(runtimes)
print('Our average run time is: %.6f seconds.' % average_runtime)
print('----\n')

# Testing sieve()
runtimes = []

for x in range(5):
    start = timer()
    result = sieve(num)
    end = timer()
    current_runtime = end - start
    runtimes.append(current_runtime)

print('Testing sieve()')
print('Our run time results:', runtimes)
average_runtime = sum(runtimes) / len(runtimes)
print('Our average run time is: %.6f seconds.' % average_runtime)
print('----\n')
