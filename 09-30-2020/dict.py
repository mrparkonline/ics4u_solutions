# For each numbers from 2 to N (N → integer user input)
# Create a key, value pair of its Factors

# Key 16 would have the List of → 1,2,4,8,16

def factors(num):
    return [x for x in range(1,num+1) if num % x == 0]

print(factors(16))

user_input = int(input('Enter a value: '))

factor_pairs = {}

for i in range(2, user_input):
    factor_pairs[i] = factors(i)

for key, value in factor_pairs.items():
    print('%s: %s' % (key, value))
