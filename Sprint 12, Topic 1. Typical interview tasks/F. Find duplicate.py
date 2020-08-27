'''
The given is an array of numbers consisting of n integers.
One number occurs more than once. You need to find this number.

The first line contains the number n.
The next line contains n integers through a space.
'''


def find_duplicate():
    n = int(input())
    list_numbers = list(map(int, input().split()))
    duplicate_list = set(
        [x for x in list_numbers if list_numbers.count(x) > 1])
    print(*duplicate_list)


find_duplicate()
