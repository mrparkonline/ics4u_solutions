# 09.15.2020
# Anagram Question

''' Solution idea:
Sort both words and compare
Clean the string
Make sure the cases of the letters are the same
'''

word1 = input('Enter your first word: ')
word2 = input('Enter your second word: ')

# First clean each string --> removed any spaces before and after the word, and lowercased
# strip() removes spaces found in the beginning and in the end of the string
# lower() makes all characters lowercased
clean_word1 = word1.strip().lower()
clean_word2 = word2.strip().lower()

# we are constructing a new strings with only alpha characters with these two for loopss
word1 = ''
for c in clean_word1:
    if c.isalpha():
        word1 += c

word2 = ''
for c in clean_word2:
    if c.isalpha():
        word2 += c # word2 = word2 + c

# both word1 and word2 are composed of alphabetical characters
# sorted(string) --> will sort the strings into a list
sorted_word1 = sorted(word1)
sorted_word2 = sorted(word2)

# at this point we could have compared the two sorted list; however, I want to show you
# how to convert a list of characters to string
word1 = ''
for item in sorted_word1:
    word1 += item

word2 = ''
for item in sorted_word2:
    word2 += item
# word1 and word2 are sorted and are back to being strings

print('Are the two words anagrams?:', word1 == word2)
# HOMEWORk: Is there another way to solve this problem?
