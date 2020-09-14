# 09/14/2020

# Vowels and Consonant Solution
# A program that counts the vowels and consonsonts from a string
'''
Solution Thoughts:
- Check only for alphabetical characters
- Create two lists, one with vowels the other with consonants
- Maybe have one list for vowels
- For loop
- len(word) then remove the number of vowels
'''

def vowelCounter(word):
    '''
    vowelCounter counts the number of vowels word has

    argument
    -- word : string
    return
    -- integer : the number of vowels
    '''

    word = word.lower()
    vowel_counter = 0

    for character in word:
        if character in 'aeiou':
            vowel_counter += 1
    # end of for loop

    return vowel_counter
# end of vowelCounter()

def consonantCounter(word):

    target = ''
    for character in word:
        if character.isalpha() == True:
            target += character

    return len(target) - vowelCounter(word)
# end of consonantCounter

word = input('Enter a word to count the number of vowels and consonants')
print(word, 'has', vowelCounter(word), 'vowels.')
print(word, 'has', consonantCounter(word), 'consonants.')
