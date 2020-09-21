# All the functions from Exercise 2
# 09-18-2020

def spaceRemover(word):
    ''' spaceRemover() removes all whitespaces from a given string

    argument
    -- word : string

    return
    -- string
    '''
    cleaned_word = ''

    for character in word:
        if character != ' ':
            cleaned_word += character

    return cleaned_word

    # return word.replace(' ','') # solution 1: one line answer
# end spaceRemover()

def consonantCounter(word):
    ''' consonantCounter() counts the number of consonants

    argument
    -- word : string

    returns
    -- integer
    '''

    counter = 0
    for character in word:
        if character.isalpha() and character.lower() not in 'aeiou':
            counter += 1 # counter = counter + 1 // counter++

    return counter
# end of consonantCounter

def duplicates(sequence):
    ''' duplicates() returns a list of items that exists more than once

    argument
    -- sequence : list/string

    return
    -- list
    '''

    if not sequence: # The most pythonic way to check if anything is empty/null/none
        return []
    else:
        # our sequence is not empty
        resulting_list = []

        for item in sequence:
            if sequence.count(item) >= 2 and item not in resulting_list:
                # item count is greater than 2
                # item is not found in resulting_list
                resulting_list.append(item)
        # end of for

        return resulting_list
# end of duplicates()

def search(sequence, target):
    ''' search() looks for the target's location in the sequence. It finds only the first occurance

    argument
    -- sequence : string/list
    -- target : potential item

    return
    -- integer
    '''

    for i in range(len(sequence)):
        if sequence[i] == target:
            return i
    # end for
    return -1
# end of search()
