'''
Write a function that recursively outputs the English alphabet to the specified
letter included.

Input format
A small letter of the English alphabet.

Output format
You need to print the alphabet from the beginning to the specified letter
into a line with a space.
'''

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
            'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def print_alphabet(letter, alphabet):
    if letter != alphabet[-1]:
        alphabet.pop()
        print_alphabet(letter, alphabet)
    else:
        print(*alphabet)


a = open('input.txt')
letter = str(a.readline())
print_alphabet(letter, alphabet)