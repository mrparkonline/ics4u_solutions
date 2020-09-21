def isPrime1(num):
    ''' isPrime() returns True if the given number is a prime number

    argument
    -- num : integer

    return
    -- boolean
    '''

    factor_counter = 0
    for divisor in range(1,num+1):
        if num % divisor == 0:
            factor_counter += 1 # factor_counter = factor_counter + 1 -OR- factor_counter++
    # end of for

    if factor_counter != 2:
        return False
    else:
        return True

# end of isPrime2()

def isPrime2(num):

    if num < 2:
        return False

    for divisor in range(2,num):
        if num % divisor == 0:
            # prime cannot have factors in between 2 to num
            return False
    # end of for loop
    return True
# end of isPrime2()

def isPrime3(num):

    if num < 2:
        return False
    elif num in [2,3]:
        return True
    elif isEven(num):
        return False
    else:
        upper_limit = int(num**0.5) + 1

        for divisor in range(2, upper_limit):
            if num % divisor == 0:
                return False

        return True
# end of isPrime3()
