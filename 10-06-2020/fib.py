# Fibonacci Sequence

target = 10 # Finding the 10th fibonacci number or fib(10)

fib = {} # This is initializing an empty dictionary
# key : the sequence location
# value : the fibonacci at the sequence location

fib[0] = 0
fib[1] = 1
# fib(x) = fib(x-1) + fib(x-2)

for x in range(2,target+1):
    fib[x] = fib[x-1] + fib[x-2]

print('Fib of 10:', fib[target])
print('Our current fib dictionary:', fib)
