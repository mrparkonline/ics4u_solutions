# Q8) Project Euler (Q23) - Non-abundant Numbers

# Find all non-abundant sums from 12 to 28123
# Well, what numbers are abundant from 12 to 28123?

# create a dict with key being the num and boolean value for whether they are nonabundant or abundant

# find all the factors and add them, if they are larger than the number,  append them to a list

# Well how do we determine if N is abundant?

# If i have number X, how can i determine if i grab two values from a list/database to add up to X?

def isAbundant(num):
    ''' isAbundant() determines if a num is an abundant number

    argument
    -- num : integer

    return
    -- boolean
    '''

    upper = int(num ** 0.5) + 1
    total_sum = 1

    for divisor in range(2,upper):
        if num % divisor == 0:
            if num // divisor == divisor:
                total_sum += divisor
            else:
                total_sum += num // divisor
                total_sum += divisor

    return total_sum > num # if this is True, we have an abundant number!!!
# end of is abundant

nums = {x: isAbundant(x) for x in range(1,28123)}
#print(nums)

ab_nums = list(filter(isAbundant, range(1,28123)))
set_ab = set(ab_nums)

impossible = list(range(1,24)) # all numbers from 1 to 23 cannot be made as two abundant numbers

for num in range(24,28123):
    for ab_num in ab_nums:
        if ab_num >= num:
            # if this sitution arises, we cannot create
            # the current num with two abundant numbers
            impossible.append(num)
            break
        else:
            difference = num - ab_num

            if difference in set_ab:
                # current num can be made by two abundant numbers
                # therefore, we don't add it to our impossible list
                break

            # if difference is not in set_ab, we need to check until ab_num >= num

print(sum(impossible))
