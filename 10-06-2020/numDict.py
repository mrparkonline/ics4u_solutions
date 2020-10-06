'''
Q4a) Write a Python program to sum all the items in a dictionary
Q4b) Write a Python program to multiply all the items in a dictionary

Q5a) Create a function that sorts a dictionary by key → Create a sorted list of keys.
Q5b) Create a function that sorts a dictionary by value → Create a sorted list of values.
'''

from random import seed
from random import randrange

seed(1) # this allow us to generate the same random numbers
# at every run
test = {randrange(1,1000000) : randrange(1,100) for x in range(20)}

print(test)

# q4a) Sum up all the values in a dictionary
total_sum = sum(test.values())
print('The total_sum is:', total_sum)

# q4b) Multiply all the number
def multiplyDict(table):
    ''' multiplyDict returns the total product of all values in table

    argument
    -- table : dictionary

    return
    -- integer
    '''

    total_product = 1
    for value in table.values():
        total_product *= value

    return total_product
# end of multiplyDict
print('The total product is:', multiplyDict(test))

# q5a) List of the keys sorted
sorted_test_keys = sorted(test.keys())
print('Keys of test sorted:', sorted_test_keys)

# q5b) List of the values sorted
sorted_test_values = sorted(test.values())
print('Values of test sorted:', sorted_test_values)
