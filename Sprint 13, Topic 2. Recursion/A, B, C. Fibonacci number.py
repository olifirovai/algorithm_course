'''
You need to write the recursive realization of the function defining by number
the value of n-th Fibonacci number.

Input format
N - an integer in the range from 0 to 30.

Output format
You need to print the n-th Fibonacci number.
'''
start_numbers = [0, 1]

a = open('input.txt')
b = int(a.readline())


def find_fibonacci_numbers(list, index):
    new_number = list[-1] + list[-2]
    list.append(new_number)
    if len(list) < 30:
        find_fibonacci_numbers(list, index)
    else:
        list.remove(0)
        print(list[index])


find_fibonacci_numbers(start_numbers, b)