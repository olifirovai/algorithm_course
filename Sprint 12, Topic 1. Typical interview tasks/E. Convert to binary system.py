'''
The input is given an integer number in the range from 0 to 10000.
Type in the binary form of this number.
'''


def binary_convert(number):
    binary_number = ''
    while number > 0:
        binary_number = str(number % 2) + binary_number
        number = number // 2
    print(binary_number)


binary_convert(int(input()))
