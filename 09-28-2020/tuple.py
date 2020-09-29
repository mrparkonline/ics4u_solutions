# Question related to Tuple Slide Deck
# Q1) Create a list of tuples containing (a,b,c). Where b = a^2 and c = a^3. Let a be integers of 2 to user_input upper limit

upper_limit = 30

result = [(a, a**2, a**3) for a in range(1,upper_limit)]
print(result)

# Q2) Create a deck of cards using tuples. Creating a function to shuffle it as well.

suits = ('Spade', 'Heart', 'Club', 'Diamond')
numeric_values = tuple(range(2,11))
letter_values = ('Jack', 'Queen', 'King', 'Ace')
value = numeric_values + letter_values

deck = [(suit, num) for suit in suits for num in value]
print(deck)
print(len(deck))

def shuffler(seq):
    '''
    from random import shuffle

    shuffle(seq)
    '''
    from random import choice

    seq_copy = seq.copy()
    result = []

    while seq_copy:
        # while our list is not empty
        current = choice(seq_copy)
        result.append(current)
        seq_copy.remove(current)

    return result

print(shuffler(deck))

# Q3) Create a function that converts a string into a list of tuples. A single tuple holds two values: the character and the number of occurance. Sort the list.

def charCount(word):
    ''' charCount returns the occurance of each character from word

    argument
    -- word : string

    return
    -- list
    '''

    result = []
    tracker_string = ''

    for c in word:
        # let c be character
        if c not in tracker_string:
            tracker_string += c
            result.append((word.count(c), c))

    result.sort()
    return result
# end of charCount

print(charCount('hello goodbye'))
