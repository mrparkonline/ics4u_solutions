# 09/14/2020
# Practice Questions
# Sorting a String Alphabetically

def cleaner(word):
    '''
    cleaner() helps us remove non alpha characters and makes everything lowercased

    arguments
    -- word : string

    return
    -- string : the cleaned result
    '''

    cleaned_word = ''
    for character in word:
        if character.isalpha():
            # our current character is found in the alphabet
            cleaned_word += character # cleaned_word = cleaned_word + character
    # cleaned_word is now just filled with alpha characters

    cleaned_word = cleaned_word.lower()
    # this help us put all alpha characters to lowercase

    return cleaned_word
# end of cleaner()

'''
1. Convert it to a list then use the sort() function
2. Use ascii value of a letter
3. Bubble Sort
'''

def sorter1(word):
    '''
    sorter1() returns the word alphabetically sorted

    argument
    -- word : string

    return
    -- string
    '''

    word = cleaner(word) # making sure to clean the word
    list_word = list(word)
    list_word.sort()

    result = '' # empty string to add our values in
    for item in list_word:
        result += item
    # end of for loop

    return result
# end of sorter1

'''
print('sorted version of hello:', sorter1('hello'))
print('sorted version of goodbye world:', sorter1('goodbye world'))
'''

def sorter2(word):
    ''' use the ascii values! Bubble Sort'''

    # since we are using the ASCII values, we don't need to clean them
    # however, this might leave it ASCII sorted value instead of alphabetical

    list_word = list(word)
    swap = True

    while swap:
        # As long as the variable swap is True, we are gonna loop :)
        swap = False

        for i in range(1, len(list_word)):
            # compare list_word[i] vs list_word[i-1]

            if ord(list_word[i]) < ord(list_word[i-1]):
                # SWAP
                # Normal way
                temp = list_word[i]
                list_word[i] = list_word[i-1]
                list_word[i-1] = temp

                # python way ...
                #list_word[i], list_word[i-1] = list_word[i-1], list_word[i]
                swap = True
        # end of inner for
    # end of outer while

    result = ''
    for item in list_word:
        result += item

    return result
# end of sorter2

print('sorted version of hello:', sorter2('hello'))
print('sorted version of goodbye world:', sorter2('goodbye world'))
