'''
Two words are anagrams, if one can be created from the other by rearranging the
letters. A palindrome is a word or phrase that can be read equally if you read
from left to right and from right to left. You need to make a function that
defines whether or not an anagrams are words.

There are two words in the input - each on a separate line. Words consist of
lowercase letters of the Latin and Russian alphabets.
'''


def define_anagrams():
    first_word = "".join(sorted(list(str(input()))))
    second_word = "".join(sorted(list(str(input()))))
    if first_word == second_word:
        print('These two words are anagrams')
    else:
        print('These two words are not anagrams')


if __name__ == '__main__':
    define_anagrams()
