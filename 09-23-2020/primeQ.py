
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

def numOfPrimes1(num):
    ''' numOfPrimes1 determines the number of primes under the given argument

    argument
    -- num : integer

    return
    -- integer
    '''

    from math import log

    # approximation function https://en.wikipedia.org/wiki/Prime-counting_function
    return int(num / log(num))
# end of numOfPrimes

def primesUnderN1(num):
    ''' primesUnderN1() returns a list of all prime numbers under num

    argument
    -- num : integer

    return
    -- list
    '''

    result = []
    for i in range(1,num):
        if isPrime(i): # if isPrime(i) == True:
            result.append(i)

    return result
# end of primesUnderN

def primesUnderN2(num):
    ''' Sieve's Algorithm

    algorithm Sieve of Eratosthenes is
    input: an integer n > 1.
    output: all prime numbers from 2 through n.

    let A be an array of Boolean values, indexed by integers 2 to n,
    initially all set to true.

    for i = 2, 3, 4, ..., not exceeding √n do
        if A[i] is true
            for j = i2, i2+i, i2+2i, i2+3i, ..., not exceeding n do
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
# end of primesUnderN

def primeFactors(num):
    ''' primeFactors() returns a list of prime factors of a number

    argument
    -- num : integer

    return
    -- list
    '''

    # Early Checks
    if num < 2:
        return []
    elif num in [2,3]:
        return [num]
    else:

        primes = []
        # First Check, is num divisible by 2?
        while num % 2 == 0:
            primes.append(2)
            num //= 2

        if num == 1:
            return primes
        else:
            divisor = 3

            while num != 1:
                if num % divisor == 0:
                    primes.append(divisor)
                    num //= divisor
                else:
                    divisor += 2 # increase divisor by 2 if it isn't divisible

            return primes
# end of primeFactors

def mostPrimeFactors(num):
    ''' From 2 to num, which first occurance of a number has the most prime factors?

    arguments
    -- num : integer

    return
    -- integer
    '''

    longest_length = 0
    result = 0

    for value in range(2,num):
        current_length = len(primeFactors(value)):
        if current_length > longest_length:
            longest_length = current_length
            result = value

    return result
# end of mostPrimeFactors

def goldbach(num):
    '''
    '''
# end of goldbach

''' Note on Twin Primes
We will actually revisit this question!
'''
