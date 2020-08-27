'''
A positive integer number is given. You need to calculate how many 1 occurs
in the binary number of this number.

Print one number - the number of ones.
'''
from collections import Counter

number = int(input())


def binary_convert(number):
    binary_number = ''
    while number > 0:
        binary_number = str(number % 2) + binary_number
        number = number // 2
    return binary_number


def find_amount(binary_number):
    mydict = Counter(binary_number)
    count_one = mydict.get('1')
    print(count_one)


find_amount(binary_convert(number))
