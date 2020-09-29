# Looking at different use cases of iterator functions
print(range(1,10))
print(type(range(1,10)))

for i in range(1,10):
    print(i)

def cube(x):
    return x ** 3

for value in map(cube, range(1,10)):
    print(value)

def isOdd(x):
    return x % 2 != 0

print('All odd numbers from 1 to 30:', list(filter(isOdd, range(1,30))))

# Create a program that creates a list of palindromic numbers from 1 to upper user limit

upper_limit = 100 # change this to int(input()) afterwards

def isPalindrome(word):
    return word == word[::-1] # word is equivalent to the reverse of itself

nums = list(range(1,upper_limit)) # this is our list of numbers
str_nums = list(map(str, nums)) # we are mapping the str() to all values in nums

palindromic_numbers = list(map(int, filter(isPalindrome, str_nums)))

print('Our palindromic numbers from 1 to 100:')
print(palindromic_numbers)
