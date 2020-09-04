'''
Given a number ‘n’, write a function that prints the last digit of n’th
Fibonacci number.
'''
b = int(input())
last_digit = [1, 1, 2, 3, 5, 8, 3, 1, 4, 5, 9, 4, 3, 7, 0, 7, 7, 4, 1, 5, 6, 1,
              7, 8, 5, 3, 8, 1, 9, 0, 9, 9, 8, 7, 5, 2, 7, 9, 6, 5, 1, 6, 7, 3,
              0, 3, 3, 6, 9, 5, 4, 9, 3, 2, 5, 7, 2, 9, 1, 0]


def find_fibonacci_numbers(index, last_digit):
    if index > 60:
        index -= 60
        find_fibonacci_numbers(index, last_digit)
    else:
        print(last_digit[index])


find_fibonacci_numbers(b, last_digit)
