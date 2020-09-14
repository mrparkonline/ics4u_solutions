# 09/14/2020
# Practice Questions

# Palindrome Checking Solution
'''
- Removing spaces/non-alpha characters
- Flipping the text backwards
- Make everything lowercased
- Front & back at the same time
- Output if it is a palindrome or not
'''

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

def isPalindrome1(word):
    ''' isPalindrome1 checks if the given argument is a palindrome

    argument
    -- word : string

    return
    -- boolean : True if the word is indeed a palindrome
    '''

    our_target = cleaner(word)

    return our_target == our_target[::-1]
# end of isPalindrome1

def isPalindrome2(word):
    '''
    check the first character vs the last character
    '''

    word = cleaner(word)
    end_index = len(word) - 1
    mid_point = len(word) // 2

    i = 0 # index variable to help us index our string

    while i < mid_point:
        if word[i] != word[end_index]:
            return False
        else:
            i += 1
            end_index -= 1

    return True
# end of isPalindrome2

print('Is racecar a palindrome?: ', isPalindrome2('racecar'))
print('Is nurses run a palindrome?: ', isPalindrome2('nurses run'))
print('Is Mr. Park a palindrome?:', isPalindrome2('Mr. Park'))
