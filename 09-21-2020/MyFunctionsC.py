# All the functions from Exercise 3
# 09-21-2020

def fToC(temperature):
    ''' This is a fahrenheit to Celsius Convereter

    argument
    -- temperature : integer/float

    return
    -- integer/float
    '''
    # C = (F - 32) / 1.8
    return (temperature - 32) / 1.8
# end of fToC

def cToF(temperature):
    ''' This is a Celsius to Fahrenheit Convereter

    argument
    -- temperature : integer/float

    return
    -- integer/float
    '''

    # 1.8*C + 32 = F
    return (temperature*1.8) + 32
# end of cToF

def average(array):
    ''' average calculates the average from a list of a values

    argument
    -- array : list

    return
    -- float
    '''

    return sum(array) / len(array)
# end of average

def average2(array):

    total_sum = 0
    for value in array:
        total_sum += value

    counter = 0
    for value in array:
        counter += 1

    return total_sum / counter
# end of average2

def factorList(num):
    ''' factorList returns a list of all factors of num

    argument
    -- num : integer

    return
    -- list
    '''

    result = []
    for divisor in range(1,num+1):
        if num % divisor == 0:
            result.append(divisor)
            # result += [divisor]

    return result
# end of factorList

def fibN(n):
    ''' fibN returns the Nth fibonacci value from the fibonacci sequence

    argument
    -- n : integer >= 0

    return
    -- integer
    '''

    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        # This concept is called "recursion"
        # return fibN(n-1) + fibN(n-2)

        # Non Recursive Solution
        fib_0 = 0
        fib_1 = 1
        fib_n = 0 # We have not calculate the fibonacci number
        counter = 1 # we currently only know the fib(1)

        while counter != n:
            fib_n = fib_1 + fib_0 # We have found the next fibonacci number
            counter += 1

            fib_0 = fib_1
            fib_1 = fib_n

        return fib_n
# end of fibN

def randList(low, upper, size):
    ''' randList generate size many integer values from low to upper (non-including the upper limit)

    argument
    -- low : integer
    -- upper : integer
    -- size : integer

    return
    -- list
    '''

    from random import randrange

    result = []
    for i in range(size):
        result.append(randrange(low,upper))

    return result
# end of randList

def intInput(prompt=''):
    ''' intInput only allows integers greater than 0 to be inputted

    argument
    -- prompt : string

    return
    -- integer
    '''

    our_input = ''
    flag = True

    while flag:
        our_input = input(prompt)

        if our_input.isnumeric() and int(our_input) > 0:
            flag = False
            return int(our_input)
        else:
            print('Invalid input.')
# end of intInput

def minimum(sequence):
    ''' minimum function returns the smallest value from our sequence

    argument
    -- sequence : string/list

    return
    -- data value
    '''

    if not sequence:
        # sequence is empty therefore there is no minimum value
        return None
    else:

        result = sequence[0] # result initialized with the first value of our sequence

        for item in sequence[1:]:
            if item < result:
                result = item

        return result
# end of minimum

def maximum(sequence):
    ''' maximum() returns the largest value in the sequence

    argument
    -- sequence : string / integer

    return
    -- data type
    '''

    if not sequence:
        # if the sequence is empty, we return Nothing/None
        return None
    else:
        result = sequence[0] # initializing with the very first value in our sequence

        for item in sequence[1:]:
            if item > result:
                result = item

        return result
# end of maximum

def patternCounter(sequence, pattern):
    ''' patternCounter function returns how many times the pattern occurs in the sequence

    arguments
    -- sequence : string
    -- pattern : string

    return
    -- integer
    '''

    counter = 0
    while pattern in sequence:
        counter += 1
        sequence = sequence.replace(pattern, '', 1)

    return counter
# end of patternCounter
