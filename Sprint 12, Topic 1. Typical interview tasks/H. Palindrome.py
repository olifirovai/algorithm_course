'''
Now help Tom to understand if the phrase will be a palindrome.
Only letters and numbers are counts, uppercase and lowercase letters are
considered to be the same.

Given one line with the phrase or word. Letters can only be Latin.
'''


def define_palindrome():
    phrase_line = ''.join(x for x in (str(input())) if x.isalpha()).lower()
    reversed_line = ''.join(
        x for x in phrase_line[::-1] if x.isalpha()).lower()
    if phrase_line == reversed_line:
        print('This phrase or word is a palindrome')
    else:
        print('This phrase or word is not a palindrome')


define_palindrome()
