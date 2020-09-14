# 09/14/2020
# Factoring Program


num = int(input('Enter a number you want the factors for: '))

# While Loop Solution
divisor = 1
while divisor <= num:
    # we are checking all numbers from 1 to inputted num

    if num % divisor == 0:
        # when num is divided by divisor the remainder is 0
        # therefore, divisor is a factor of num
        print(divisor, 'is a factor of', num)

    divisor += 1
# end of while
print('I am outside of while loop')

# For Loop Solution
for i in range(1, num+1):
    if num % i == 0:
        print(i, 'is a factor of', num)
# end of for
print('I am now outside of the for loop')

# Thought: which is the better solution?
# Can I program a better solution?
