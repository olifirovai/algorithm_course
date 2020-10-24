'''
Given a list of non negative integers, arrange them such that they form the
largest number.

n - amount of integers
'''


class Comparator(str):
    def __lt__(x, y):
        return x + y > y + x


def largest_number(number_list):
    largest_num = ''.join(sorted(number_list, key=Comparator))
    return '0' if largest_num[0] == '0' else largest_num


if __name__ == "__main__":
    n = int(input())
    number_list = list(map(str, input().split()))
    number = largest_number(number_list)
    print(number)
