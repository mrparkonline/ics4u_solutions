# Sieve of Eratosthenes Algorithm

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
