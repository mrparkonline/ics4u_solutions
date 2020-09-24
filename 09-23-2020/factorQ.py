# Solutions and Functions related to factoring

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

def mostFactors(low, upper):
    ''' mostFactors() returns the first occurance of a number that had the most factors in the given range

    arguments
    -- low : integer
    -- upper : integer

    return
    -- integer
    '''

    largest_count = 0 # tracking variables initialized
    resulting_num = 0 # tracking variables initialized

    for num in range(low,upper):
        current_count = len(factors(num))
        if current_count > largest_count:
            largest_count = current_count
            resulting_num = num

    return resulting_num
# end of mostFactors

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
