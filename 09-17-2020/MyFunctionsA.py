# This is my collection of custom functions

def isEven(num):
    ''' isEven checks if the argument value is an even number

    argument
    -- num : integer

    return
    -- boolean
    '''

    return num % 2 == 0 # % --> remainder finder
# end of isEven

#print('Hello, this is MyFunctions')

def stringCleaner(word):
    ''' stringCleaner takes a string argument and it puts all alpha to lowercase and removes any non-alpha characters

    argument
    -- word : string

    returns
    string
    '''
    result = '' # empty string
    for character in word:
        if character.isalpha():
            result += character.lower()

    return result
# end of stringCleaner

def isPalindrome(word):
    ''' isPalindrome checks if the given argument is a palindrome (a word that is the same backwards)

    argument
    -- word : string

    returns
    -- boolean
    '''

    cleaned_word = stringCleaner(word)

    return cleaned_word == cleaned_word[::-1]
# end of isPalindrome

def isPrime(num):
    ''' isPrime checks if the given integer argument is a prime number

    argument
    -- num : integer

    return
    -- boolean
    '''
    if num < 2:
        return False
    elif num in [2,3]:
        # Base Case
        return True
    elif num % 2 == 0:
        return False
    else:
        for divider in range(3, int(num ** 0.5)+1):
            if num % divider == 0:
                # any time we find a factor, we return False
                return False
        # end of for
        return True # it should prime number here
# end of isPrime

def vowelCounter(word):
    ''' vowelCounter counts the number of vowels.
    This function assumes that vowels only a,e,i,o,u

    argument
    -- word : string

    return
    -- integer
    '''

    counter = 0

    for character in word:
        if character.lower() in 'aeiou':
            counter += 1

    return counter
# end of vowelCounter
