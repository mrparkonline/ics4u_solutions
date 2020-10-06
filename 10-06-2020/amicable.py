# amicable numbers

# Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n).

# If d(a) = b and d(b) = a, where a ≠ b, then a and b are an amicable pair and each of a and b are called amicable numbers.

def d(n):
    ''' d(n) be defined as the sum of proper divisors of n  '''

    total_sum = 1 # since 1 is a factor for all numbers, we initialize our sum with 1

    upper_limit = int(n**0.5) + 1

    for num in range(2,upper_limit):
        if n % num == 0:
            # currently num is a divisor
            if n // num == num:
                # we have a perfect square
                total_sum += num
            else:
                total_sum += num
                total_sum += (n // num)
    # end of for loop
    return total_sum
# end of d(n)

print('d(284):', d(284))
print('d(220):', d(220))

# Create set that holds all amicable numbers
amicable_numbers = set() # everytime we find amicable numbers, add them to the set

proper_divisor_table = {} # this dictionary will hold the result of d(n)

# Analyzing all numbers from 1 to 10000
for num in range(1,10000):
    if num not in proper_divisor_table:
        current_sum = d(num)
        proper_divisor_table[num] = current_sum

        # We only execute this code if we have not calculated current_sum's proper divisor sum
        if current_sum not in proper_divisor_table:
            proper_divisor_table[current_sum] = d(current_sum)

        if num == proper_divisor_table[current_sum] and num != current_sum:
            # we have an amicable pair!!!
            amicable_numbers.add(num)
            amicable_numbers.add(current_sum)
# end of for loop
print('Our amicable number set:', amicable_numbers)
print('Total sum under 10000:', sum(amicable_numbers))
