# Recursion Problem Set 1

'''
Q1. Factorial ( O(n) → Complexity )
--
Write a recursive solution to the Factorial Problem.
Recall That:
5! = 5 x 4! (4 x 3 x 2 x 1) = 120

'''

def factorial(num):
    if num in {0,1}: # {0,1} is a set of two values of 0 and 1
    # Because membership is faster with set, we put those two values in a set
        return 1

    else:
        return num * factorial(num-1)

    '''
    if num == 0:
        return 1
    elif num == 1:
        return 1
    '''

#print(factorial(5))

# Tail Recursion w. Factorial
def factorial_t(num, tail=1):
    if num == 0:
        return tail
    else:
        return factorial_t(num-1, tail*num)

#print(factorial_t(5))

# Exponentiation /non-tail version
def power(base, exponent):
    if exponent == 0:
        return 1
    elif exponent == 1:
        return base
    else:
        return base * power(base, exponent-1)

'''
2^4 = 2 * 2^3 == (2 * 2 * 2)
'''

#print(power(2,4))

# Exponentiation tail recursion
def power_t(base, exponent, tail=1):
    if exponent == 0:
        return tail
    else:
        return power_t(base, exponent-1, tail*base)

#print(power_t(2,4))

# Palindrome / non-tail
def isPalindrome(word):
    if len(word) == 0:
        # Empty Strings are palindromes
        return True
    elif len(word) == 1:
        # single characters are palindromes
        return True
    elif len(word) == 2:
        # two characters are palindromes if they are equal
        # to each other
        return word[0] == word[1]
    else:
        return word[0] == word[-1] and isPalindrome(word[1:-1])

#print(isPalindrome('park'))
#print(isPalindrome('tacoCat'))

# palindrome w/ Tail Recursion
def isPalindrome_t(word, tail=True):
    if not tail: # tail is False!
        return False
    elif not word: # pythonic way of writing len(word) == 0
        return True and tail
    else:
        return isPalindrome_t(word[1:-1], (word[0] == word[-1]) and tail)

#print(isPalindrome_t('park'))
#print(isPalindrome_t('tacocat'))

# Reverse string/list recursively
def reverser(word):
    if len(word) in {0,1}: # empty string or a single character
        return word
    else:
        return reverser(word[1:]) + word[0]

# print(reverser('park'))

# Tail Recursion: Reverser
def reverser_t(word, tail=''):
    if not word:
        return tail
    else:
        return reverser_t(word[:-1], tail+word[-1])

# print(reverser_t('park'))

def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)

print(10, fib(10))
print(20, fib(20))

def fib2(n):
    ''' non-recursive fib '''
    fib_dict = {0:0, 1:1}

    if n in fib_dict:
        return fib_dict[n]
    else:
        for value in range(2,n+1):
            fib_dict[value] = fib_dict[value-1] + fib_dict[value-2]

        return fib_dict[n]

print(10, fib2(10))

def fib_t(n, t1=1, t2=0):
    if n == 0:
        return t2
    elif n == 1:
        return t1
    else:
        return fib_t(n-1, t1+t2, t1)

print(10, fib_t(10))
