# Write a program that reads a string and returns a table of the letters of the alphabet in alphabetical order which occur in the string together with the number of times each letter occurs. Case should be ignored.

def letterHistogram(word):
    ''' letterHistogram tracks the occurance of each alpha characters

    argument
    -- word : string

    return
    -- dictionary
    '''

    cleaned_word = list(map(str.lower, word))
    #cleaned_word = sorted(cleaned_word)
    cleaned_word.sort()
    # print(cleaned_word)

    table = {} # empty dictionar
    # Key --> each alpha letter
    # Value --> the number of occurance

    for item in cleaned_word:
        if item in table: # item/the alpha character is a key that exist in table
            table[item] += 1
        else:
            if item.isalpha():
                table[item] = 1
    # end for
    return table
# end of letterHistogram

table = letterHistogram("The quick brown fox jumps over the lazy dog")

for character, count in table.items():
    print(character, count)
